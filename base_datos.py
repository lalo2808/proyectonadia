
import sqlite3
from datetime import datetime

from utilidades import (
    hash_password,
    verificar_password,
)

DB_NAME = "educacion.db"


class BaseDatos:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.crear_tablas()

    # ============================================================
    # CONEXIÓN
    # ============================================================
    def conectar(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    # ============================================================
    # CREACIÓN DE TABLAS
    # ============================================================
    def crear_tablas(self):
        conn = self.conectar()
        cursor = conn.cursor()

        # ------------------------
        # Usuarios
        # ------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                fecha_registro TEXT NOT NULL,
                ultimo_login TEXT,
                activo INTEGER DEFAULT 1
            )
        """)

        # ------------------------
        # Progreso
        # ------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS progreso (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                curso TEXT NOT NULL,
                modulo TEXT NOT NULL,
                completado INTEGER DEFAULT 0,
                mejor_puntaje INTEGER DEFAULT 0,
                intentos INTEGER DEFAULT 0,
                ultima_fecha TEXT,
                UNIQUE(usuario_id, curso, modulo),
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
            )
        """)

        # ------------------------
        # Intentos
        # ------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS intentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                curso TEXT NOT NULL,
                modulo TEXT NOT NULL,
                puntaje INTEGER NOT NULL,
                porcentaje REAL NOT NULL,
                fecha TEXT NOT NULL,
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
            )
        """)

        # ------------------------
        # Certificados de módulo
        # ------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS certificados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                curso TEXT NOT NULL,
                modulo TEXT NOT NULL,
                puntaje INTEGER NOT NULL,
                porcentaje REAL NOT NULL,
                folio TEXT NOT NULL UNIQUE,
                hash_certificado TEXT NOT NULL,
                ruta_pdf TEXT NOT NULL,
                fecha_emision TEXT NOT NULL,
                fecha_actualizacion TEXT NOT NULL,
                UNIQUE(usuario_id, curso, modulo),
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
            )
        """)

        # ------------------------
        # Certificados finales
        # ------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS certificados_curso (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                curso TEXT NOT NULL,
                promedio REAL NOT NULL,
                folio TEXT NOT NULL UNIQUE,
                hash_certificado TEXT NOT NULL,
                ruta_pdf TEXT NOT NULL,
                fecha_emision TEXT NOT NULL,
                fecha_actualizacion TEXT NOT NULL,
                UNIQUE(usuario_id, curso),
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
            )
        """)

        conn.commit()
        conn.close()

    # ============================================================
    # USUARIOS
    # ============================================================
    def registrar_usuario(self, nombre, correo, password):
        conn = self.conectar()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO usuarios (
                    nombre,
                    correo,
                    password_hash,
                    fecha_registro
                )
                VALUES (?, ?, ?, ?)
            """, (
                nombre.strip(),
                correo.strip().lower(),
                hash_password(password),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))

            conn.commit()
            return True, "Usuario registrado correctamente"

        except sqlite3.IntegrityError:
            return False, "Ese correo ya está registrado"

        except Exception as e:
            return False, f"Error: {e}"

        finally:
            conn.close()

    def login_usuario(self, correo, password):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM usuarios
            WHERE correo = ?
        """, (correo.strip().lower(),))

        usuario = cursor.fetchone()

        if not usuario:
            conn.close()
            return False, "Usuario no encontrado", None

        if not verificar_password(password, usuario["password_hash"]):
            conn.close()
            return False, "Contraseña incorrecta", None

        cursor.execute("""
            UPDATE usuarios
            SET ultimo_login = ?
            WHERE id = ?
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            usuario["id"]
        ))

        conn.commit()
        conn.close()

        return True, "Login correcto", dict(usuario)

    def obtener_usuario(self, usuario_id):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM usuarios
            WHERE id = ?
        """, (usuario_id,))

        usuario = cursor.fetchone()
        conn.close()

        return dict(usuario) if usuario else None

    # ============================================================
    # PROGRESO
    # ============================================================
    def guardar_progreso(
        self,
        usuario_id,
        curso,
        modulo,
        puntaje
    ):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM progreso
            WHERE usuario_id = ?
            AND curso = ?
            AND modulo = ?
        """, (usuario_id, curso, modulo))

        registro = cursor.fetchone()
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if registro:
            mejor = max(registro["mejor_puntaje"], puntaje)

            cursor.execute("""
                UPDATE progreso
                SET completado = 1,
                    mejor_puntaje = ?,
                    intentos = intentos + 1,
                    ultima_fecha = ?
                WHERE usuario_id = ?
                AND curso = ?
                AND modulo = ?
            """, (
                mejor,
                ahora,
                usuario_id,
                curso,
                modulo
            ))

        else:
            cursor.execute("""
                INSERT INTO progreso (
                    usuario_id,
                    curso,
                    modulo,
                    completado,
                    mejor_puntaje,
                    intentos,
                    ultima_fecha
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                usuario_id,
                curso,
                modulo,
                1,
                puntaje,
                1,
                ahora
            ))

        conn.commit()
        conn.close()

    def obtener_progreso_usuario(self, usuario_id):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM progreso
            WHERE usuario_id = ?
            ORDER BY curso, modulo
        """, (usuario_id,))

        datos = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return datos

    def obtener_progreso_modulo(self, usuario_id, curso, modulo):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM progreso
            WHERE usuario_id = ?
            AND curso = ?
            AND modulo = ?
        """, (usuario_id, curso, modulo))

        row = cursor.fetchone()
        conn.close()

        return dict(row) if row else None

    # ============================================================
    # INTENTOS
    # ============================================================
    def guardar_intento(
        self,
        usuario_id,
        curso,
        modulo,
        puntaje,
        porcentaje
    ):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO intentos (
                usuario_id,
                curso,
                modulo,
                puntaje,
                porcentaje,
                fecha
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            usuario_id,
            curso,
            modulo,
            puntaje,
            porcentaje,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        conn.close()

    def obtener_intentos_usuario(self, usuario_id):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM intentos
            WHERE usuario_id = ?
            ORDER BY fecha DESC
        """, (usuario_id,))

        datos = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return datos

    # ============================================================
    # CERTIFICADOS
    # ============================================================
    def guardar_o_actualizar_certificado(
        self,
        usuario_id,
        curso,
        modulo,
        puntaje,
        porcentaje,
        folio,
        hash_certificado,
        ruta_pdf
    ):
        conn = self.conectar()
        cursor = conn.cursor()

        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            SELECT * FROM certificados
            WHERE usuario_id = ?
            AND curso = ?
            AND modulo = ?
        """, (usuario_id, curso, modulo))

        existente = cursor.fetchone()

        if existente:
            cursor.execute("""
                UPDATE certificados
                SET puntaje = ?,
                    porcentaje = ?,
                    folio = ?,
                    hash_certificado = ?,
                    ruta_pdf = ?,
                    fecha_actualizacion = ?
                WHERE usuario_id = ?
                AND curso = ?
                AND modulo = ?
            """, (
                puntaje,
                porcentaje,
                folio,
                hash_certificado,
                ruta_pdf,
                ahora,
                usuario_id,
                curso,
                modulo
            ))

        else:
            cursor.execute("""
                INSERT INTO certificados (
                    usuario_id,
                    curso,
                    modulo,
                    puntaje,
                    porcentaje,
                    folio,
                    hash_certificado,
                    ruta_pdf,
                    fecha_emision,
                    fecha_actualizacion
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                usuario_id,
                curso,
                modulo,
                puntaje,
                porcentaje,
                folio,
                hash_certificado,
                ruta_pdf,
                ahora,
                ahora
            ))

        conn.commit()
        conn.close()

    def obtener_certificados_usuario(self, usuario_id):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM certificados
            WHERE usuario_id = ?
            ORDER BY fecha_actualizacion DESC
        """, (usuario_id,))

        datos = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return datos

    # ============================================================
    # ESTADÍSTICAS
    # ============================================================
    def resumen_usuario(self, usuario_id):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total_modulos
            FROM progreso
            WHERE usuario_id = ?
            AND completado = 1
        """, (usuario_id,))
        total_modulos = cursor.fetchone()["total_modulos"]

        cursor.execute("""
            SELECT COUNT(*) AS total_certificados
            FROM certificados
            WHERE usuario_id = ?
        """, (usuario_id,))
        total_certificados = cursor.fetchone()["total_certificados"]

        cursor.execute("""
            SELECT AVG(mejor_puntaje) AS promedio
            FROM progreso
            WHERE usuario_id = ?
        """, (usuario_id,))
        promedio = cursor.fetchone()["promedio"] or 0

        conn.close()

        return {
            "modulos_completados": total_modulos,
            "certificados": total_certificados,
            "promedio": round(promedio, 2)
        }


# Instancia global
db = BaseDatos()


if __name__ == "__main__":
    print("Base de datos creada correctamente.")