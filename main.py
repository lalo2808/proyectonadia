
import os
import webbrowser

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition
from kivymd.uix.label import MDIcon
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.toast import toast  # Usamos toast en lugar de Snackbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from utilidades import (
    NOMBRE_APP,
    BANNER,
    CALIFICACION_MINIMA,
    validar_correo,
    validar_password,
    validar_nombre,
    calcular_porcentaje,
    aprobo,
)

from base_datos import db
from preguntas import CURSOS, obtener_cursos, obtener_modulos, obtener_preguntas
from certificados import generar_certificado_modulo


# ============================================================
# VARIABLES GLOBALES
# ============================================================

def mostrar_mensaje(texto):
    toast(texto)  # Mensaje emergente simple

def abrir_archivo(ruta):
    if os.path.exists(ruta):
        webbrowser.open(ruta)

# ============================================================
# SCREENS
# ============================================================

class SplashScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

class CoursesScreen(Screen):
    pass

class ModulesScreen(Screen):
    pass

class QuizScreen(Screen):
    pass

class ResultScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class CertificatesScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# ============================================================
# CARDS
# ============================================================

class CourseCard(MDCard):
    titulo = StringProperty("")
    descripcion = StringProperty("")
    progreso = NumericProperty(0)
    imagen = StringProperty("")
    curso = StringProperty("")

class ModuleCard(MDCard):
    titulo = StringProperty("")
    estado = StringProperty("")
    puntaje = NumericProperty(0)
    intentos = NumericProperty(0)
    modulo = StringProperty("")

class QuestionCard(MDCard):
    pregunta_numero = NumericProperty(0)
    pregunta_texto = StringProperty("")
    opcion_a = StringProperty("")
    opcion_b = StringProperty("")
    opcion_c = StringProperty("")
    opcion_d = StringProperty("")
    respuesta_correcta = NumericProperty(0)
    respuesta_usuario = NumericProperty(-1)

class CertificateCard(MDCard):
    titulo = StringProperty("")
    subtitulo = StringProperty("")
    descripcion = StringProperty("")
    ruta_pdf = StringProperty("")

# ============================================================
# KV LANGUAGE (sin propiedades obsoletas)
# ============================================================

KV = """
#:import dp kivy.metrics.dp

<CourseCard>:
    orientation: "vertical"
    ripple_behavior: True
    radius: [22, 22, 22, 22]
    md_bg_color: 1, 1, 1, 1

    Image:
        source: root.imagen
        size_hint_y: None
        height: dp(125)

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(14)
        spacing: dp(8)

        MDLabel:
            text: root.titulo
            bold: True
            font_style: "H6"
            theme_text_color: "Primary"

        MDLabel:
            text: root.descripcion
            font_style: "Caption"
            theme_text_color: "Secondary"

        MDProgressBar:
            value: root.progreso

        MDLabel:
            text: "Progreso general: " + str(root.progreso) + "%"
            halign: "right"
            font_style: "Caption"

<ModuleCard>:
    ripple_behavior: True
    md_bg_color: .98, .99, 1, 1

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(15)
        spacing: dp(8)

        MDLabel:
            text: root.titulo
            bold: True
            font_style: "H6"

        MDLabel:
            text: "Estado: " + root.estado
            theme_text_color: "Secondary"

        MDLabel:
            text: "Mejor puntaje: " + str(root.puntaje) + "/10"
            theme_text_color: "Secondary"

        MDLabel:
            text: "Intentos: " + str(root.intentos)
            theme_text_color: "Secondary"

<QuestionCard>:
    md_bg_color: 1, 1, 1, 1

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(12)
        padding: dp(15)

        MDLabel:
            text: "Pregunta " + str(root.pregunta_numero)
            bold: True
            font_style: "Subtitle1"

        MDLabel:
            text: root.pregunta_texto
            theme_text_color: "Primary"
            size_hint_y: None
            height: self.texture_size[1]

        MDBoxLayout:
            adaptive_height: True
            spacing: dp(10)

            MDCheckbox:
                id: chk_a
                on_active:
                    if self.active: app.seleccionar_respuesta(root, 0)

            MDLabel:
                text: root.opcion_a
                valign: "middle"

        MDBoxLayout:
            adaptive_height: True
            spacing: dp(10)

            MDCheckbox:
                id: chk_b
                on_active:
                    if self.active: app.seleccionar_respuesta(root, 1)

            MDLabel:
                text: root.opcion_b
                valign: "middle"

        MDBoxLayout:
            adaptive_height: True
            spacing: dp(10)

            MDCheckbox:
                id: chk_c
                on_active:
                    if self.active: app.seleccionar_respuesta(root, 2)

            MDLabel:
                text: root.opcion_c
                valign: "middle"

        MDBoxLayout:
            adaptive_height: True
            spacing: dp(10)

            MDCheckbox:
                id: chk_d
                on_active:
                    if self.active: app.seleccionar_respuesta(root, 3)

            MDLabel:
                text: root.opcion_d
                valign: "middle"

<CertificateCard>:
    ripple_behavior: True
    md_bg_color: 1, 1, 1, 1

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(15)
        spacing: dp(6)

        MDLabel:
            text: root.titulo
            bold: True
            font_style: "Subtitle1"

        MDLabel:
            text: root.subtitulo
            theme_text_color: "Secondary"

        MDLabel:
            text: root.descripcion
            theme_text_color: "Secondary"

<SplashScreen>:
    MDFloatLayout:
        md_bg_color: .96, .98, 1, 1

        Image:
            source: "recursos/logo_cecytem.png"
            size_hint: .35, .35
            pos_hint: {"center_x": .5, "center_y": .62}

        MDLabel:
            text: "Cursos de Regularización CECyTEM"
            halign: "center"
            bold: True
            font_style: "H5"
            pos_hint: {"center_y": .35}

<LoginScreen>:
    MDFloatLayout:
        md_bg_color: .97, .98, 1, 1

        MDCard:
            size_hint: .88, None
            height: dp(430)
            pos_hint: {"center_x": .5, "center_y": .5}
            padding: dp(25)
            spacing: dp(18)
            orientation: "vertical"
            radius: [25, 25, 25, 25]
            elevation: 5

            Image:
                source: "recursos/logo_cecytem.png"
                size_hint_y: None
                height: dp(95)

            MDLabel:
                text: "Iniciar Sesión"
                halign: "center"
                bold: True
                font_style: "H5"

            MDTextField:
                id: login_correo
                hint_text: "Correo electrónico"
                helper_text_mode: "on_focus"

            MDTextField:
                id: login_password
                hint_text: "Contraseña"
                password: True

            MDRaisedButton:
                text: "Ingresar"
                pos_hint: {"center_x": .5}
                on_release: app.login()

            MDTextButton:
                text: "Crear cuenta"
                pos_hint: {"center_x": .5}
                on_release: app.cambiar_pantalla("register")

<RegisterScreen>:
    MDFloatLayout:
        md_bg_color: .97, .98, 1, 1

        MDCard:
            size_hint: .88, None
            height: dp(500)
            pos_hint: {"center_x": .5, "center_y": .5}
            padding: dp(25)
            spacing: dp(18)
            orientation: "vertical"
            radius: [25, 25, 25, 25]
            elevation: 5

            MDLabel:
                text: "Registro"
                halign: "center"
                bold: True
                font_style: "H5"

            MDTextField:
                id: reg_nombre
                hint_text: "Nombre completo"

            MDTextField:
                id: reg_correo
                hint_text: "Correo electrónico"

            MDTextField:
                id: reg_password
                hint_text: "Contraseña"
                password: True

            MDRaisedButton:
                text: "Registrarme"
                pos_hint: {"center_x": .5}
                on_release: app.registrar()

            MDTextButton:
                text: "Volver"
                pos_hint: {"center_x": .5}
                on_release: app.volver("login")

<DashboardScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(18)

        MDTopAppBar:
            title: "CECyTEM"
            elevation: 3

        MDLabel:
            id: bienvenida
            text: "Bienvenido"
            bold: True
            font_style: "H5"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDRaisedButton:
            text: "Entrar a Cursos"
            on_release: app.abrir_cursos()
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDRaisedButton:
            text: "Mi Perfil"
            on_release: app.abrir_perfil()
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDRaisedButton:
            text: "Certificados"
            on_release: app.abrir_certificados()
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDRaisedButton:
            text: "Ajustes"
            on_release: app.abrir_ajustes()
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        Widget:

        MDRaisedButton:
            text: "Cerrar Sesión"
            on_release: app.cerrar_sesion()
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
<CoursesScreen>:
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Cursos"
            left_action_items: [["arrow-left", lambda x: app.volver("dashboard")]]

        ScrollView:
            MDList:
                id: lista_cursos
                padding: dp(10)
                spacing: dp(14)
                size_hint_y: None
                height: self.minimum_height

<ModulesScreen>:
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            id: titulo_modulos
            title: "Módulos"
            left_action_items: [["arrow-left", lambda x: app.volver("courses")]]

        ScrollView:
            MDList:
                id: lista_modulos
                padding: dp(10)
                spacing: dp(12)
                size_hint_y: None
                height: self.minimum_height

<QuizScreen>:
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(10)

        MDTopAppBar:
            title: "Evaluación"
            left_action_items: [["arrow-left", lambda x: app.volver("modules")]]
            elevation: 4

        MDBoxLayout:
            orientation: "vertical"
            padding: dp(15)
            spacing: dp(8)
            size_hint_y: None
            height: dp(80)
            md_bg_color: 0.95, 0.97, 1, 1

            MDLabel:
                id: titulo_quiz
                text: ""
                halign: "center"
                bold: True
                font_style: "H6"
                color: 0.2, 0.2, 0.2, 1

            MDLabel:
                id: subtitulo_quiz
                text: ""
                halign: "center"
                theme_text_color: "Secondary"
                font_style: "Subtitle2"

        ScrollView:
            do_scroll_x: False
            MDCard:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                radius: [20, 20, 20, 20]
                elevation: 6
                padding: dp(20)
                spacing: dp(15)
                md_bg_color: 1, 1, 1, 1

                MDLabel:
                    id: contador_preguntas
                    text: "Pregunta 1 de 10"
                    bold: True
                    font_style: "Subtitle2"
                    theme_text_color: "Primary"

                MDLabel:
                    id: pregunta_texto
                    text: ""
                    font_style: "Body1"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDBoxLayout:
                    adaptive_height: True
                    spacing: dp(10)

                    MDCheckbox:
                        id: chk_a
                        group: "quiz_opciones"
                        on_active:
                            if self.active: app.respuesta_seleccionada(0)

                    MDLabel:
                        id: opcion_a
                        text: ""
                        valign: "middle"

                MDBoxLayout:
                    adaptive_height: True
                    spacing: dp(10)

                    MDCheckbox:
                        id: chk_b
                        group: "quiz_opciones"
                        on_active:
                            if self.active: app.respuesta_seleccionada(1)

                    MDLabel:
                        id: opcion_b
                        text: ""
                        valign: "middle"

                MDBoxLayout:
                    adaptive_height: True
                    spacing: dp(10)

                    MDCheckbox:
                        id: chk_c
                        group: "quiz_opciones"
                        on_active:
                            if self.active: app.respuesta_seleccionada(2)

                    MDLabel:
                        id: opcion_c
                        text: ""
                        valign: "middle"

                MDBoxLayout:
                    adaptive_height: True
                    spacing: dp(10)

                    MDCheckbox:
                        id: chk_d
                        group: "quiz_opciones"
                        on_active:
                            if self.active: app.respuesta_seleccionada(3)

                    MDLabel:
                        id: opcion_d
                        text: ""
                        valign: "middle"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: dp(60)
            spacing: dp(20)
            padding: dp(15)

            MDRaisedButton:
                id: btn_anterior
                text: "Anterior"
                disabled: True
                on_release: app.anterior_pregunta()
                md_bg_color: 0.4, 0.6, 0.9, 1
                text_color: 1, 1, 1, 1

            MDRaisedButton:
                id: btn_siguiente
                text: "Siguiente"
                on_release: app.siguiente_pregunta()
                md_bg_color: 0.2, 0.7, 0.3, 1
                text_color: 1, 1, 1, 1

<ResultScreen>:
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(10)

        MDTopAppBar:
            title: "Resultados"
            left_action_items: [["arrow-left", lambda x: app.volver("modules")]]
            elevation: 4

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(15)
                spacing: dp(15)
                size_hint_y: None
                height: self.minimum_height

                MDCard:
                    orientation: "vertical"
                    padding: dp(15)
                    spacing: dp(10)
                    radius: [20, 20, 20, 20]
                    elevation: 4
                    md_bg_color: 1, 1, 1, 1

                    MDLabel:
                        text: "Resumen del módulo"
                        bold: True
                        font_style: "H6"
                        halign: "center"

                    MDLabel:
                        id: resultado_curso
                        text: ""
                        halign: "center"
                        font_style: "Subtitle1"

                    MDLabel:
                        id: resultado_modulo
                        text: ""
                        halign: "center"
                        font_style: "Subtitle1"

                    MDSeparator:

                    MDLabel:
                        id: resultado_puntaje
                        text: ""
                        halign: "center"
                        bold: True
                        font_style: "H5"

                    MDLabel:
                        id: resultado_porcentaje
                        text: ""
                        halign: "center"
                        font_style: "H6"

                    MDLabel:
                        id: resultado_estado
                        text: ""
                        halign: "center"
                        bold: True
                        font_style: "H4"

                MDLabel:
                    text: "Detalle por pregunta"
                    bold: True
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: dp(30)

                MDBoxLayout:
                    id: detalles_container
                    orientation: "vertical"
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height

        MDBoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: dp(60)
            spacing: dp(15)
            padding: dp(15)

            MDRaisedButton:
                text: "Generar certificado"
                on_release: app.generar_certificado_si_aplica()
                md_bg_color: 0.2, 0.6, 0.9, 1

            MDRaisedButton:
                text: "Abrir certificado"
                on_release: app.abrir_ultimo_certificado()
                md_bg_color: 0.4, 0.4, 0.4, 1

            MDRaisedButton:
                text: "Repetir módulo"
                on_release: app.repetir_modulo()
                md_bg_color: 0.9, 0.5, 0.1, 1

<ProfileScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)

        MDTopAppBar:
            title: "Perfil"
            left_action_items: [["arrow-left", lambda x: app.volver("dashboard")]]

        MDLabel:
            id: perfil_nombre
            bold: True
            font_style: "H5"

        MDLabel:
            id: perfil_correo

        MDLabel:
            id: perfil_promedio

        MDLabel:
            id: perfil_modulos

        MDLabel:
            id: perfil_certificados

<CertificatesScreen>:
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Certificados"
            left_action_items: [["arrow-left", lambda x: app.volver("dashboard")]]

        ScrollView:
            MDList:
                id: lista_certificados
                padding: dp(10)
                spacing: dp(12)
                size_hint_y: None
                height: self.minimum_height

<SettingsScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)

        MDTopAppBar:
            title: "Ajustes"
            left_action_items: [["arrow-left", lambda x: app.volver("dashboard")]]

        MDLabel:
            text: "Configuración básica"

        MDRaisedButton:
            text: "Limpiar campos"
            on_release: app.limpiar_campos()

        MDRaisedButton:
            text: "Cerrar sesión"
            on_release: app.cerrar_sesion()
"""

# ============================================================
# APLICACIÓN PRINCIPAL
# ============================================================

class RegularizacionApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.usuario = None
        self.curso_actual = None
        self.modulo_actual = None
        self.puntaje_actual = 0

    def build(self):
        self.title = NOMBRE_APP
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.accent_palette = "Amber"

        Builder.load_string(KV)

        sm = ScreenManager(transition=FadeTransition(duration=0.35))
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(CoursesScreen(name="courses"))
        sm.add_widget(ModulesScreen(name="modules"))
        sm.add_widget(QuizScreen(name="quiz"))
        sm.add_widget(ResultScreen(name="result"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(CertificatesScreen(name="certificates"))
        sm.add_widget(SettingsScreen(name="settings"))

        Clock.schedule_once(self.ir_login, 2.5)
        return sm

    def on_start(self):
        mostrar_mensaje("Bienvenido a Cursos de Regularización CECyTEM")

    # ============================================================
    # NAVEGACIÓN
    # ============================================================
    def cambiar_pantalla(self, pantalla):
        self.root.transition = SlideTransition(direction="left")
        self.root.current = pantalla

    def volver(self, pantalla):
        self.root.transition = SlideTransition(direction="right")
        self.root.current = pantalla

    def ir_login(self, *args):
        self.root.current = "login"

    # ============================================================
    # LOGIN Y REGISTRO
    # ============================================================
    def login(self):
        pantalla = self.root.get_screen("login")
        correo = pantalla.ids.login_correo.text.strip()
        password = pantalla.ids.login_password.text.strip()

        if not correo or not password:
            mostrar_mensaje("Completa todos los campos")
            return

        ok, mensaje, usuario = db.login_usuario(correo, password)
        if not ok:
            mostrar_mensaje(mensaje)
            return

        self.usuario = usuario
        dashboard = self.root.get_screen("dashboard")
        dashboard.ids.bienvenida.halign = "center"
        dashboard.ids.bienvenida.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        dashboard.ids.bienvenida.text = f"Bienvenido, {usuario['nombre']}"

        mostrar_mensaje("Inicio de sesión correcto")
        self.cambiar_pantalla("dashboard")

    def registrar(self):
        pantalla = self.root.get_screen("register")
        nombre = pantalla.ids.reg_nombre.text.strip()
        correo = pantalla.ids.reg_correo.text.strip()
        password = pantalla.ids.reg_password.text.strip()

        valido, msg = validar_nombre(nombre)
        if not valido:
            mostrar_mensaje(msg)
            return
        if not validar_correo(correo):
            mostrar_mensaje("Correo inválido")
            return
        valido, msg = validar_password(password)
        if not valido:
            mostrar_mensaje(msg)
            return

        ok, mensaje = db.registrar_usuario(nombre, correo, password)
        mostrar_mensaje(mensaje)
        if ok:
            pantalla.ids.reg_nombre.text = ""
            pantalla.ids.reg_correo.text = ""
            pantalla.ids.reg_password.text = ""
            self.volver("login")

    # ============================================================
    # DASHBOARD
    # ============================================================
    def abrir_cursos(self):
        self.cargar_cursos()
        self.cambiar_pantalla("courses")

    def abrir_perfil(self):
        resumen = db.resumen_usuario(self.usuario["id"])
        pantalla = self.root.get_screen("profile")
        pantalla.ids.perfil_nombre.text = self.usuario["nombre"]
        pantalla.ids.perfil_correo.text = self.usuario["correo"]
        pantalla.ids.perfil_promedio.text = f"Promedio: {resumen['promedio']}"
        pantalla.ids.perfil_modulos.text = f"Módulos completados: {resumen['modulos_completados']}"
        pantalla.ids.perfil_certificados.text = f"Certificados: {resumen['certificados']}"
        self.cambiar_pantalla("profile")

    def abrir_certificados(self):
        contenedor = self.root.get_screen("certificates").ids.lista_certificados
        contenedor.clear_widgets()
        certificados = db.obtener_certificados_usuario(self.usuario["id"])
        if not certificados:
            mostrar_mensaje("Aún no tienes certificados")
            self.cambiar_pantalla("certificates")
            return
        for cert in certificados:
            card = CertificateCard(
                titulo=cert["modulo"],
                subtitulo=cert["curso"],
                descripcion=f"Calificación: {cert['puntaje']}/10",
                ruta_pdf=cert["ruta_pdf"],
                size_hint_y=None,
                height=dp(145),
                radius=[18, 18, 18, 18],
                elevation=2,
                padding=dp(10),
            )
            card.bind(on_release=lambda x, r=cert["ruta_pdf"]: abrir_archivo(r))
            contenedor.add_widget(card)
        self.cambiar_pantalla("certificates")

    def abrir_ajustes(self):
        self.cambiar_pantalla("settings")

    def cerrar_sesion(self):
        self.limpiar_campos()
        self.usuario = None
        self.root.current = "login"
        mostrar_mensaje("Sesión finalizada correctamente")

    def limpiar_campos(self):
        login = self.root.get_screen("login")
        register = self.root.get_screen("register")
        login.ids.login_correo.text = ""
        login.ids.login_password.text = ""
        register.ids.reg_nombre.text = ""
        register.ids.reg_correo.text = ""
        register.ids.reg_password.text = ""

    # ============================================================
    # CURSOS Y MÓDULOS
    # ============================================================
    def cargar_cursos(self):
        contenedor = self.root.get_screen("courses").ids.lista_cursos
        contenedor.clear_widgets()
        cursos = obtener_cursos()
        banners = {
            "Primaria": "recursos/banner_primaria.jpg",
            "Secundaria": "recursos/banner_secundaria.jpg",
            "Preparatoria": "recursos/banner_prepa.jpg",
            "Universidad": "recursos/banner_universidad.jpg",
            "Cultura General": "recursos/banner_cultura.jpg",
        }
        resumen = db.resumen_usuario(self.usuario["id"])
        progreso_global = min(int((resumen["modulos_completados"] / 25) * 100), 100)

        for nombre in cursos:
            descripcion = CURSOS[nombre]["descripcion"]
            card = CourseCard(
                titulo=nombre,
                descripcion=descripcion,
                progreso=progreso_global,
                imagen=banners.get(nombre, BANNER),
                curso=nombre,
                size_hint_y=None,
                height=dp(210),
                radius=[22, 22, 22, 22],
                elevation=4,
                padding=0,
                spacing=0,
            )
            card.bind(on_release=lambda x, curso=nombre: self.abrir_modulos(curso))
            contenedor.add_widget(card)

    def abrir_modulos(self, curso):
        self.curso_actual = curso
        pantalla = self.root.get_screen("modules")
        pantalla.ids.titulo_modulos.text = curso
        self.cargar_modulos()
        self.cambiar_pantalla("modules")

    def cargar_modulos(self):
        contenedor = self.root.get_screen("modules").ids.lista_modulos
        contenedor.clear_widgets()
        modulos = obtener_modulos(self.curso_actual)

        for modulo in modulos:
            progreso = db.obtener_progreso_modulo(self.usuario["id"], self.curso_actual, modulo)
            if progreso:
                estado = "Completado"
                puntaje = progreso["mejor_puntaje"]
                intentos = progreso["intentos"]
            else:
                estado = "Pendiente"
                puntaje = 0
                intentos = 0

            card = ModuleCard(
                titulo=modulo,
                estado=estado,
                puntaje=puntaje,
                intentos=intentos,
                modulo=modulo,
                size_hint_y=None,
                height=dp(150),
                radius=[18, 18, 18, 18],
                elevation=3,
                padding=dp(10),
            )
            card.bind(on_release=lambda x, m=modulo: self.iniciar_modulo(m))
            contenedor.add_widget(card)

    def iniciar_modulo(self, modulo):
        self.modulo_actual = modulo
        self.cargar_quiz()
        self.cambiar_pantalla("quiz")

    # ============================================================
    # QUIZ
    # ============================================================
        # ============================================================
    # QUIZ (una pregunta a la vez, bloqueo al finalizar)
    # ============================================================
    def cargar_quiz(self):
        """Inicializa el cuestionario"""
        self.preguntas_lista = obtener_preguntas(self.curso_actual, self.modulo_actual)
        self.indice_pregunta = 0
        self.respuestas_usuario = [None] * len(self.preguntas_lista)
        self.quiz_finalizado = False   # bloquea cambios después de finalizar

        pantalla = self.root.get_screen("quiz")
        pantalla.ids.titulo_quiz.text = self.curso_actual
        pantalla.ids.subtitulo_quiz.text = self.modulo_actual

        self.cargar_pregunta_actual()
        self.actualizar_botones_navegacion()

    def cargar_pregunta_actual(self):
        """Muestra la pregunta actual en su tarjeta"""
        pantalla = self.root.get_screen("quiz")
        pregunta = self.preguntas_lista[self.indice_pregunta]

        # Texto de la pregunta
        pantalla.ids.pregunta_texto.text = pregunta["pregunta"]

        # Opciones
        opciones = pregunta["opciones"]
        pantalla.ids.opcion_a.text = f"A) {opciones[0]}"
        pantalla.ids.opcion_b.text = f"B) {opciones[1]}"
        pantalla.ids.opcion_c.text = f"C) {opciones[2]}"
        pantalla.ids.opcion_d.text = f"D) {opciones[3]}"

        # Resetear selección visual (sin llamar eventos)
        chk_a = pantalla.ids.chk_a
        chk_b = pantalla.ids.chk_b
        chk_c = pantalla.ids.chk_c
        chk_d = pantalla.ids.chk_d
        chk_a.active = False
        chk_b.active = False
        chk_c.active = False
        chk_d.active = False

        # Marcar respuesta guardada
        resp = self.respuestas_usuario[self.indice_pregunta]
        if resp == 0:
            chk_a.active = True
        elif resp == 1:
            chk_b.active = True
        elif resp == 2:
            chk_c.active = True
        elif resp == 3:
            chk_d.active = True

        # Habilitar/deshabilitar checkboxes según si finalizado
        estado = not self.quiz_finalizado
        chk_a.disabled = not estado
        chk_b.disabled = not estado
        chk_c.disabled = not estado
        chk_d.disabled = not estado

        # Contador
        pantalla.ids.contador_preguntas.text = f"Pregunta {self.indice_pregunta + 1} de {len(self.preguntas_lista)}"

    def respuesta_seleccionada(self, opcion_idx):
        """Guarda la respuesta seleccionada (solo si no finalizado)"""
        if self.quiz_finalizado:
            return
        self.respuestas_usuario[self.indice_pregunta] = opcion_idx

    def actualizar_botones_navegacion(self):
        pantalla = self.root.get_screen("quiz")
        pantalla.ids.btn_anterior.disabled = (self.indice_pregunta == 0)
        if self.indice_pregunta == len(self.preguntas_lista) - 1:
            pantalla.ids.btn_siguiente.text = "Finalizar"
        else:
            pantalla.ids.btn_siguiente.text = "Siguiente"

    def siguiente_pregunta(self):
        if self.quiz_finalizado:
            return
        # Validar que haya respuesta en la actual
        if self.respuestas_usuario[self.indice_pregunta] is None:
            mostrar_mensaje("Selecciona una respuesta antes de continuar.")
            return

        if self.indice_pregunta == len(self.preguntas_lista) - 1:
            # finalizar
            self.finalizar_quiz()
        else:
            self.indice_pregunta += 1
            self.cargar_pregunta_actual()
            self.actualizar_botones_navegacion()

    def anterior_pregunta(self):
        if self.quiz_finalizado:
            return
        if self.indice_pregunta > 0:
            self.indice_pregunta -= 1
            self.cargar_pregunta_actual()
            self.actualizar_botones_navegacion()

    def finalizar_quiz(self):
        """Bloquea el quiz, calcula aciertos y muestra resultados detallados"""
        # Verificar que todas las preguntas tengan respuesta
        if any(r is None for r in self.respuestas_usuario):
            mostrar_mensaje("Debes responder todas las preguntas antes de finalizar.")
            return

        self.quiz_finalizado = True
        # Deshabilitar checkboxes
        self.cargar_pregunta_actual()  # esto actualiza el estado disabled

        # Calcular aciertos y preparar desglose
        aciertos = 0
        desglose = []
        for i, pregunta in enumerate(self.preguntas_lista):
            resp_user = self.respuestas_usuario[i]
            es_correcta = (resp_user == pregunta["respuesta"])
            if es_correcta:
                aciertos += 1
            desglose.append({
                "texto": pregunta["pregunta"],
                "opciones": pregunta["opciones"],
                "correcta_idx": pregunta["respuesta"],
                "user_idx": resp_user,
                "correcta": es_correcta
            })

        total = len(self.preguntas_lista)
        porcentaje = calcular_porcentaje(aciertos, total)

        # Guardar en base de datos
        db.guardar_intento(self.usuario["id"], self.curso_actual, self.modulo_actual, aciertos, porcentaje)
        db.guardar_progreso(self.usuario["id"], self.curso_actual, self.modulo_actual, aciertos)

        # Mostrar pantalla de resultados con desglose
        resultado_screen = self.root.get_screen("result")
        resultado_screen.ids.resultado_curso.text = self.curso_actual
        resultado_screen.ids.resultado_modulo.text = self.modulo_actual
        resultado_screen.ids.resultado_puntaje.text = f"{aciertos}/{total}"
        resultado_screen.ids.resultado_porcentaje.text = f"{porcentaje}%"

        if aprobo(aciertos, total):
            resultado_screen.ids.resultado_estado.text = "APROBADO"
            resultado_screen.ids.resultado_estado.color = (0, 0.6, 0, 1)
        else:
            resultado_screen.ids.resultado_estado.text = "REPROBADO"
            resultado_screen.ids.resultado_estado.color = (0.85, 0, 0, 1)

        # Construir lista de detalles en un ScrollView
        detalles_container = resultado_screen.ids.detalles_container
        detalles_container.clear_widgets()
        for idx, d in enumerate(desglose, 1):
            # Tarjeta por pregunta
            card = MDCard(
                orientation="vertical",
                size_hint_y=None,
                height=dp(160),
                radius=[12, 12, 12, 12],
                elevation=2,
                padding=dp(10),
                spacing=dp(5),
                md_bg_color=(1,1,1,1)
            )
            # Icono y encabezado
            icono = "checkbox-marked-circle" if d["correcta"] else "close-circle"
            color_icono = (0,0.8,0,1) if d["correcta"] else (0.9,0.2,0,1)
            encabezado = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(30), spacing=dp(5))
            encabezado.add_widget(MDIcon(icon=icono, theme_text_color="Custom", text_color=color_icono))
            encabezado.add_widget(MDLabel(text=f"Pregunta {idx}: {d['texto'][:80]}", bold=True))
            card.add_widget(encabezado)

            # Tu respuesta
            letra_user = ["A", "B", "C", "D"][d["user_idx"]] if d["user_idx"] is not None else "Ninguna"
            texto_user = f"Tu respuesta: {letra_user}) {d['opciones'][d['user_idx']]}" if d["user_idx"] is not None else "Sin respuesta"
            card.add_widget(MDLabel(text=texto_user, size_hint_y=None, height=dp(25), font_style="Caption"))

            # Respuesta correcta
            letra_correcta = ["A", "B", "C", "D"][d["correcta_idx"]]
            texto_correcta = f"Correcta: {letra_correcta}) {d['opciones'][d['correcta_idx']]}"
            card.add_widget(MDLabel(text=texto_correcta, size_hint_y=None, height=dp(25), font_style="Caption"))

            detalles_container.add_widget(card)

        self.cambiar_pantalla("result")
    # ============================================================
    # RESULTADOS Y CERTIFICADOS
    # ============================================================
    def generar_certificado_si_aplica(self):
        if not aprobo(self.puntaje_actual):
            mostrar_mensaje(f"No alcanzaste la mínima aprobatoria ({CALIFICACION_MINIMA})")
            return

        certificados = db.obtener_certificados_usuario(self.usuario["id"])
        ruta_anterior = None
        for cert in certificados:
            if cert["curso"] == self.curso_actual and cert["modulo"] == self.modulo_actual:
                ruta_anterior = cert["ruta_pdf"]
                break

        nuevo = generar_certificado_modulo(
            nombre_alumno=self.usuario["nombre"],
            curso=self.curso_actual,
            modulo=self.modulo_actual,
            calificacion=self.puntaje_actual,
            ruta_anterior=ruta_anterior
        )

        db.guardar_o_actualizar_certificado(
            usuario_id=self.usuario["id"],
            curso=self.curso_actual,
            modulo=self.modulo_actual,
            puntaje=self.puntaje_actual,
            porcentaje=calcular_porcentaje(self.puntaje_actual, 10),
            folio=nuevo["folio"],
            hash_certificado=nuevo["hash"],
            ruta_pdf=nuevo["ruta_pdf"]
        )
        mostrar_mensaje("Certificado generado correctamente")

    def abrir_ultimo_certificado(self):
        certificados = db.obtener_certificados_usuario(self.usuario["id"])
        for cert in certificados:
            if cert["curso"] == self.curso_actual and cert["modulo"] == self.modulo_actual:
                abrir_archivo(cert["ruta_pdf"])
                return
        mostrar_mensaje("No hay certificado disponible")

    def repetir_modulo(self):
        self.cargar_quiz()
        self.volver("quiz")

    def volver_a_modulos(self):
        self.cargar_modulos()
        self.volver("modules")

if __name__ == "__main__":
    RegularizacionApp().run()