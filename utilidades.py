
import os
import re
import uuid
import hashlib
from datetime import datetime


# =========================
# CONFIGURACIÓN GENERAL
# =========================
NOMBRE_APP = "Cursos de Regularización CECyTEM"
CARPETA_RECURSOS = "recursos"
CARPETA_CERTIFICADOS = "certificados"
CARPETA_CERTIFICADOS_MODULOS = os.path.join(CARPETA_CERTIFICADOS, "modulos")
CARPETA_CERTIFICADOS_CURSOS = os.path.join(CARPETA_CERTIFICADOS, "cursos")
CARPETA_RESPALDOS = "respaldos"

LOGO_CECYTEM = os.path.join(CARPETA_RECURSOS, "logo_cecytem.png")
BANNER = os.path.join(CARPETA_RECURSOS, "banner.jpg")
FONDO_CERTIFICADO = os.path.join(CARPETA_RECURSOS, "fondo_certificado.png")
AVATAR_DEFAULT = os.path.join(CARPETA_RECURSOS, "avatar_default.png")

CALIFICACION_MINIMA = 7


# =========================
# CARPETAS
# =========================
def crear_carpetas():
    """
    Crea automáticamente la estructura de carpetas
    necesaria para la aplicación.
    """
    carpetas = [
        CARPETA_RECURSOS,
        CARPETA_CERTIFICADOS,
        CARPETA_CERTIFICADOS_MODULOS,
        CARPETA_CERTIFICADOS_CURSOS,
        CARPETA_RESPALDOS,
    ]

    for carpeta in carpetas:
        os.makedirs(carpeta, exist_ok=True)


# =========================
# FECHAS
# =========================
def fecha_actual():
    """
    Devuelve fecha actual completa.
    """
    return datetime.now()


def fecha_formateada():
    """
    Ejemplo:
    07/05/2026 19:45
    """
    return datetime.now().strftime("%d/%m/%Y %H:%M")


def fecha_para_archivo():
    """
    Ejemplo:
    20260507_194501
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")


# =========================
# HASH CONTRASEÑAS
# =========================
def hash_password(password: str) -> str:
    """
    Convierte contraseña a SHA256.
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def verificar_password(password: str, password_hash: str) -> bool:
    """
    Verifica contraseña.
    """
    return hash_password(password) == password_hash


# =========================
# HASH CERTIFICADOS
# =========================
def generar_hash_certificado(
    nombre: str,
    curso: str,
    modulo: str,
    calificacion: float,
    folio: str
) -> str:
    """
    Genera hash único para certificado.
    """
    texto = f"{nombre}|{curso}|{modulo}|{calificacion}|{folio}|{fecha_formateada()}"
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


# =========================
# FOLIOS
# =========================
def limpiar_texto(texto: str) -> str:
    """
    Limpia texto para archivos y folios.
    """
    texto = texto.strip()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("Á", "A")
    texto = texto.replace("É", "E")
    texto = texto.replace("Í", "I")
    texto = texto.replace("Ó", "O")
    texto = texto.replace("Ú", "U")
    texto = texto.replace("ñ", "n")
    texto = texto.replace("Ñ", "N")

    texto = re.sub(r"[^a-zA-Z0-9_ ]", "", texto)
    texto = texto.replace(" ", "_")

    return texto


def generar_folio(tipo="MOD"):
    """
    Ejemplo:
    MOD-20260507-AB12CD
    CUR-20260507-X91QWE
    """
    fecha = datetime.now().strftime("%Y%m%d")
    codigo = uuid.uuid4().hex[:6].upper()
    return f"{tipo}-{fecha}-{codigo}"


# =========================
# VALIDACIONES
# =========================
def validar_correo(correo: str) -> bool:
    """
    Valida formato simple de correo.
    """
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(patron, correo))


def validar_password(password: str) -> tuple[bool, str]:
    """
    Validación sencilla.
    """
    password = password.strip()

    if len(password) < 6:
        return False, "La contraseña debe tener mínimo 6 caracteres"

    return True, "OK"


def validar_nombre(nombre: str) -> tuple[bool, str]:
    """
    Valida nombre.
    """
    nombre = nombre.strip()

    if len(nombre) < 3:
        return False, "El nombre es demasiado corto"

    if len(nombre) > 100:
        return False, "El nombre es demasiado largo"

    return True, "OK"


# =========================
# ARCHIVOS
# =========================
def nombre_archivo_certificado(nombre, curso, modulo):
    """
    Genera nombre limpio de PDF.
    """
    nombre = limpiar_texto(nombre)
    curso = limpiar_texto(curso)
    modulo = limpiar_texto(modulo)

    timestamp = fecha_para_archivo()

    return f"{nombre}_{curso}_{modulo}_{timestamp}.pdf"


def ruta_certificado_modulo(nombre, curso, modulo):
    archivo = nombre_archivo_certificado(nombre, curso, modulo)
    return os.path.join(CARPETA_CERTIFICADOS_MODULOS, archivo)


def ruta_certificado_curso(nombre, curso):
    nombre = limpiar_texto(nombre)
    curso = limpiar_texto(curso)
    timestamp = fecha_para_archivo()

    archivo = f"{nombre}_{curso}_FINAL_{timestamp}.pdf"
    return os.path.join(CARPETA_CERTIFICADOS_CURSOS, archivo)


def eliminar_archivo(ruta):
    """
    Elimina archivo si existe.
    """
    try:
        if ruta and os.path.exists(ruta):
            os.remove(ruta)
            return True
    except Exception:
        pass

    return False


# =========================
# CÁLCULOS
# =========================
def calcular_porcentaje(aciertos, total):
    if total <= 0:
        return 0

    return round((aciertos / total) * 100, 2)


def aprobo(aciertos, total=10):
    return aciertos >= (CALIFICACION_MINIMA * total / 10)


# =========================
# TEXTO
# =========================
def truncar_texto(texto, limite=50):
    if len(texto) <= limite:
        return texto

    return texto[:limite] + "..."


def capitalizar(texto):
    return texto.strip().title()


# =========================
# DEBUG
# =========================
def imprimir_banner():
    print("=" * 60)
    print(NOMBRE_APP)
    print("Sistema iniciado correctamente")
    print("=" * 60)


# =========================
# INICIALIZACIÓN
# =========================
crear_carpetas()


if __name__ == "__main__":
    imprimir_banner()
    print("Fecha:", fecha_formateada())
    print("Folio ejemplo:", generar_folio())
    print("Hash ejemplo:", hash_password("123456"))
    print("Correo válido:", validar_correo("correo@ejemplo.com"))