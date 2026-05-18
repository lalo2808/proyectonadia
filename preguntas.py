# preguntas.py
# ------------------------------------------------------------
# Cursos de Regularización CECyTEM
# Banco de preguntas
# 5 cursos | 5 módulos por curso | 10 preguntas por módulo
# Total: 250 preguntas
# ------------------------------------------------------------

CURSOS = {
    "Primaria": {
        "descripcion": "Refuerzo de conocimientos básicos fundamentales",
        "modulos": {
            "Matemáticas básicas": [],
            "Lectura y comprensión": [],
            "Ciencias naturales": [],
            "Historia y geografía": [],
            "Valores y convivencia": []
        }
    },
    "Secundaria": {
        "descripcion": "Fortalecimiento académico intermedio",
        "modulos": {
            "Álgebra básica": [],
            "Español y redacción": [],
            "Biología y química": [],
            "Historia universal": [],
            "Tecnología e informática": []
        }
    },
    "Preparatoria": {
        "descripcion": "Preparación académica media superior",
        "modulos": {
            "Matemáticas avanzadas": [],
            "Física básica": [],
            "Química general": [],
            "Literatura y análisis": [],
            "Inglés básico/intermedio": []
        }
    },
    "Universidad": {
        "descripcion": "Competencias académicas superiores",
        "modulos": {
            "Pensamiento crítico": [],
            "Investigación académica": [],
            "Comunicación profesional": [],
            "Matemática aplicada": [],
            "Ética profesional": []
        }
    },
    "Cultura General": {
        "descripcion": "Conocimiento global y actualidad",
        "modulos": {
            "Mundo y geografía": [],
            "Historia universal": [],
            "Ciencia y tecnología": [],
            "Arte y cultura": [],
            "Actualidad y sociedad": []
        }
    }
}


def crear_pregunta(pregunta, opciones, respuesta, explicacion=""):
    """Crea una pregunta con formato estándar. respuesta = índice correcto (0,1,2,3)"""
    return {
        "pregunta": pregunta,
        "opciones": opciones,
        "respuesta": respuesta,
        "explicacion": explicacion
    }


# ============================================================
# PRIMARIA
# ============================================================

# --- Matemáticas básicas (10 preguntas) ---
CURSOS["Primaria"]["modulos"]["Matemáticas básicas"] = [
    crear_pregunta("¿Cuánto es 8 + 5?", ["11", "12", "13", "14"], 2, "8+5=13"),
    crear_pregunta("¿Cuánto es 20 - 7?", ["13", "12", "11", "10"], 0, "20-7=13"),
    crear_pregunta("¿Cuánto es 6 × 4?", ["22", "24", "26", "28"], 1, "6×4=24"),
    crear_pregunta("¿Cuánto es 18 ÷ 3?", ["5", "6", "7", "8"], 1, "18÷3=6"),
    crear_pregunta("¿Cuál número es mayor?", ["45", "54", "44", "35"], 1, "54 es el mayor"),
    crear_pregunta("¿Cuánto es la mitad de 100?", ["40", "45", "50", "55"], 2, "Mitad de 100 = 50"),
    crear_pregunta("¿Cuánto es 9 + 9?", ["18", "17", "16", "15"], 0),
    crear_pregunta("¿Cuánto es 5 × 5?", ["20", "25", "30", "35"], 1),
    crear_pregunta("¿Cuánto es 81 ÷ 9?", ["8", "9", "10", "7"], 1),
    crear_pregunta("¿Cuánto es 100 - 25?", ["65", "70", "75", "80"], 2),
]

# --- Lectura y comprensión (10 preguntas) ---
CURSOS["Primaria"]["modulos"]["Lectura y comprensión"] = [
    crear_pregunta("¿Cuál es un verbo?", ["Correr", "Mesa", "Rojo", "Casa"], 0),
    crear_pregunta("¿Qué palabra está bien escrita?", ["Habeces", "Avión", "Eskuela", "Jente"], 1),
    crear_pregunta("¿Qué signo lleva una pregunta?", ["()", "¿?", "[]", "{}"], 1),
    crear_pregunta("Sinónimo de feliz:", ["Triste", "Alegre", "Malo", "Lejos"], 1),
    crear_pregunta("Antónimo de alto:", ["Grande", "Bajo", "Ancho", "Leve"], 1),
    crear_pregunta("¿Qué es una oración?", ["Un dibujo", "Un conjunto de palabras con sentido", "Un número", "Un color"], 1),
    crear_pregunta("Plural de lápiz:", ["Lápizes", "Lápizs", "Lápices", "Lapiceros"], 2),
    crear_pregunta("¿Qué palabra es un sustantivo?", ["Correr", "Azul", "Perro", "Rápido"], 2),
    crear_pregunta("¿Qué lleva punto final?", ["Una oración completa", "Una letra", "Un número", "Un dibujo"], 0),
    crear_pregunta("¿Cuál palabra lleva acento?", ["Arbol", "Mesa", "Lápiz", "Casa"], 2),
]

# --- Ciencias naturales (10 preguntas) ---
CURSOS["Primaria"]["modulos"]["Ciencias naturales"] = [
    crear_pregunta("¿Qué necesitan las plantas para vivir?", ["Agua y sol", "Televisión", "Computadora", "Libros"], 0),
    crear_pregunta("¿Cuál es el planeta más cercano al Sol?", ["Tierra", "Marte", "Mercurio", "Venus"], 2),
    crear_pregunta("¿Qué animal es un mamífero?", ["Pez", "Perro", "Serpiente", "Loro"], 1),
    crear_pregunta("¿Cuál es el sentido que usa la nariz?", ["Vista", "Oído", "Olfato", "Tacto"], 2),
    crear_pregunta("¿Qué parte del día sale el Sol?", ["Noche", "Tarde", "Mañana", "Medianoche"], 2),
    crear_pregunta("¿Cuál de estos es un medio de transporte?", ["Silla", "Avión", "Cuaderno", "Lámpara"], 1),
    crear_pregunta("¿Qué estado del agua es el hielo?", ["Líquido", "Gaseoso", "Sólido", "Vapor"], 2),
    crear_pregunta("¿Cuál es el órgano que bombea sangre?", ["Cerebro", "Corazón", "Pulmón", "Estómago"], 1),
    crear_pregunta("¿Qué se obtiene de las vacas?", ["Huevos", "Lana", "Leche", "Miel"], 2),
    crear_pregunta("¿Qué material es reciclable?", ["Vidrio", "Plástico", "Papel", "Todas"], 3),
]

# --- Historia y geografía (10 preguntas) ---
CURSOS["Primaria"]["modulos"]["Historia y geografía"] = [
    crear_pregunta("¿Dónde está ubicada la Ciudad de México?", ["Norte", "Sur", "Centro", "Este"], 2),
    crear_pregunta("¿Quién descubrió América?", ["Hernán Cortés", "Cristóbal Colón", "Simón Bolívar", "Benito Juárez"], 1),
    crear_pregunta("¿Cuál es el océano más grande?", ["Atlántico", "Índico", "Pacífico", "Ártico"], 2),
    crear_pregunta("¿Qué monumento hay en la CDMX?", ["Torre Eiffel", "Coliseo", "Ángel de la Independencia", "Estatua de la Libertad"], 2),
    crear_pregunta("¿Cuál es el país más poblado del mundo?", ["India", "China", "EE.UU.", "Indonesia"], 1),
    crear_pregunta("¿En qué continente está Egipto?", ["Asia", "Europa", "África", "América"], 2),
    crear_pregunta("¿Quién pintó la Mona Lisa?", ["Van Gogh", "Picasso", "Da Vinci", "Miguel Ángel"], 2),
    crear_pregunta("¿Cuál es la capital de Francia?", ["Londres", "París", "Berlín", "Madrid"], 1),
    crear_pregunta("¿Qué civilización construyó Machu Picchu?", ["Azteca", "Inca", "Maya", "Olmeca"], 1),
    crear_pregunta("¿Qué río es el más largo del mundo?", ["Amazonas", "Nilo", "Yangtsé", "Misisipi"], 0),
]

# --- Valores y convivencia (10 preguntas) ---
CURSOS["Primaria"]["modulos"]["Valores y convivencia"] = [
    crear_pregunta("¿Qué valor representa ayudar a los demás?", ["Honestidad", "Solidaridad", "Pereza", "Egoísmo"], 1),
    crear_pregunta("¿Cómo se dice 'gracias' en inglés?", ["Sorry", "Please", "Thank you", "Hello"], 2),
    crear_pregunta("Si un compañero se cae, ¿qué debes hacer?", ["Reírte", "Ayudarlo", "Ignorarlo", "Gritarle"], 1),
    crear_pregunta("¿Qué significa ser responsable?", ["Cumplir con tus tareas", "No hacer nada", "Mentir", "Llegar tarde"], 0),
    crear_pregunta("¿Cuál es una forma de mostrar respeto?", ["Interrumpir", "Gritar", "Escuchar", "Burlarse"], 2),
    crear_pregunta("¿Qué debes hacer si encuentras una cartera?", ["Quedártela", "Tirarla", "Devolverla", "Esconderla"], 2),
    crear_pregunta("¿Cuál es un ejemplo de trabajo en equipo?", ["Jugar solo", "Ayudar en grupo", "Pelear", "Discutir"], 1),
    crear_pregunta("¿Qué valor es importante para decir la verdad?", ["Mentira", "Honestidad", "Envidia", "Tristeza"], 1),
    crear_pregunta("¿Cómo se saluda correctamente?", ["Sin mirar", "Gritando", "Con un 'Hola'", "De espaldas"], 2),
    crear_pregunta("¿Qué haces si alguien te pide perdón?", ["Lo ignoras", "Lo aceptas", "Te peleas", "Te ries"], 1),
]


# ============================================================
# SECUNDARIA
# ============================================================

# --- Álgebra básica (10 preguntas) ---
CURSOS["Secundaria"]["modulos"]["Álgebra básica"] = [
    crear_pregunta("Resuelve: 2x + 3 = 7", ["x=1", "x=2", "x=3", "x=4"], 1, "2x=4 => x=2"),
    crear_pregunta("¿Cuánto es (a + b)(a - b)?", ["a² - b²", "a² + b²", "2ab", "a² - 2ab"], 0),
    crear_pregunta("Simplifica: 3x + 2x", ["5x", "6x", "x", "5x²"], 0),
    crear_pregunta("Resuelve: 5 - x = 2", ["x=2", "x=3", "x=4", "x=1"], 1),
    crear_pregunta("¿Cuál es la pendiente de y = 3x + 2?", ["2", "3", "1", "0"], 1),
    crear_pregunta("Factoriza: x² - 4", ["(x-2)(x+2)", "(x-4)(x+1)", "(x-2)²", "(x+2)²"], 0),
    crear_pregunta("Resuelve: 2(x-3)=10", ["x=5", "x=6", "x=8", "x=10"], 2),
    crear_pregunta("¿Cuál es el valor de 3² + 4²?", ["25", "12", "7", "5"], 0),
    crear_pregunta("Simplifica: (3x²)(2x³)", ["6x⁵", "5x⁶", "6x⁶", "5x⁵"], 0),
    crear_pregunta("Resuelve sistema: x+y=5, x-y=1", ["x=3,y=2", "x=2,y=3", "x=4,y=1", "x=1,y=4"], 0),
]

# --- Español y redacción (10 preguntas) ---
CURSOS["Secundaria"]["modulos"]["Español y redacción"] = [
    crear_pregunta("¿Qué es un adjetivo?", ["Acción", "Cualidad", "Nombre", "Conector"], 1),
    crear_pregunta("¿Cuál es el sujeto en: 'Juan corre rápido'?", ["corre", "rápido", "Juan", "Juan corre"], 2),
    crear_pregunta("Sinónimo de 'rápido':", ["Lento", "Veloz", "Tranquilo", "Pesado"], 1),
    crear_pregunta("¿Qué oración está en futuro?", ["Voy al cine", "Fui al cine", "Iré al cine", "Iba al cine"], 2),
    crear_pregunta("¿Cuál es la palabra grave (llana)?", ["Árbol", "Canción", "Médico", "Café"], 0),
    crear_pregunta("¿Qué signo se usa para exclamar?", ["¿?", "¡!", ".;", "..."], 1),
    crear_pregunta("¿Qué es un párrafo?", ["Una palabra", "Una frase", "Conjunto de oraciones con idea", "Un título"], 2),
    crear_pregunta("¿Cuál es el verbo en 'Ellos comen pizza'?", ["Ellos", "comen", "pizza", "ellos comen"], 1),
    crear_pregunta("Antónimo de 'alegría':", ["Felicidad", "Gozo", "Tristeza", "Risa"], 2),
    crear_pregunta("¿Cómo se escribe correctamente?", ["Recojer", "Recoger", "Recogér", "Rrecoger"], 1),
]

# --- Biología y química (10 preguntas) ---
CURSOS["Secundaria"]["modulos"]["Biología y química"] = [
    crear_pregunta("¿Cuál es la unidad básica de la vida?", ["Átomo", "Molécula", "Célula", "Tejido"], 2),
    crear_pregunta("¿Qué orgánulo realiza la fotosíntesis?", ["Mitocondria", "Núcleo", "Cloroplasto", "Ribosoma"], 2),
    crear_pregunta("¿Qué gas respiramos principalmente?", ["Oxígeno", "Nitrógeno", "CO₂", "Hidrógeno"], 0),
    crear_pregunta("El pH neutro es:", ["0", "7", "14", "10"], 1),
    crear_pregunta("¿Qué tipo de ácido hay en las naranjas?", ["Ácido sulfúrico", "Ácido cítrico", "Ácido clorhídrico", "Ácido acético"], 1),
    crear_pregunta("¿Qué reacción une dos moléculas de agua? (fotosíntesis)", ["Respiración", "Hidrólisis", "Condensación", "Oxidación"], 2),
    crear_pregunta("¿Cuál es el hueso más largo del cuerpo?", ["Fémur", "Tibia", "Húmero", "Radio"], 0),
    crear_pregunta("¿Qué órgano filtra la sangre?", ["Corazón", "Pulmón", "Riñón", "Hígado"], 2),
    crear_pregunta("¿Qué tipo de célula no tiene núcleo?", ["Eucariota", "Procariota", "Animal", "Vegetal"], 1),
    crear_pregunta("¿Cuál es el elemento químico del oro?", ["Au", "Ag", "Fe", "Cu"], 0),
]

# --- Historia universal (10 preguntas) ---
CURSOS["Secundaria"]["modulos"]["Historia universal"] = [
    crear_pregunta("¿En qué año comenzó la Primera Guerra Mundial?", ["1914", "1918", "1939", "1945"], 0),
    crear_pregunta("¿Quién pintó el techo de la Capilla Sixtina?", ["Da Vinci", "Miguel Ángel", "Rafael", "Donatello"], 1),
    crear_pregunta("¿Cuál fue la primera civilización mesopotámica?", ["Egipto", "Sumeria", "Grecia", "Roma"], 1),
    crear_pregunta("¿Quién fue el primer emperador romano?", ["Julio César", "Augusto", "Nerón", "Marco Aurelio"], 1),
    crear_pregunta("¿Qué evento marcó el inicio de la Edad Media?", ["Caída de Roma", "Descubrimiento de América", "Revolución Francesa", "Primera Cruzada"], 0),
    crear_pregunta("¿Quién escribió 'El Quijote'?", ["Cervantes", "Lope de Vega", "Garcilaso", "Quevedo"], 0),
    crear_pregunta("¿Qué civilización usó el calendario solar de 365 días?", ["Azteca", "Maya", "Egipcia", "China"], 2),
    crear_pregunta("¿Qué líder independizó a México?", ["Hidalgo", "Morelos", "Iturbide", "Juárez"], 0),
    crear_pregunta("¿En qué año cayó el muro de Berlín?", ["1989", "1990", "1987", "1991"], 0),
    crear_pregunta("¿Quién fue el primer hombre en la Luna?", ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins"], 1),
]

# --- Tecnología e informática (10 preguntas) ---
CURSOS["Secundaria"]["modulos"]["Tecnología e informática"] = [
    crear_pregunta("¿Qué significa HTML?", ["High Text Markup", "Hyper Text Markup Language", "Hyperlink and Text", "Home Tool Markup"], 1),
    crear_pregunta("¿Qué unidad mide la frecuencia del procesador?", ["GHz", "GB", "MB", "KB"], 0),
    crear_pregunta("¿Cuál es el sistema operativo de Microsoft?", ["Linux", "macOS", "Windows", "Android"], 2),
    crear_pregunta("¿Qué componente muestra la imagen?", ["CPU", "RAM", "Monitor", "Disco duro"], 2),
    crear_pregunta("¿Qué significa 'URL'?", ["Uniform Resource Locator", "Universal Reference Link", "Unified Resource Link", "Ultra Rapid Link"], 0),
    crear_pregunta("¿Cuál es un lenguaje de programación?", ["Python", "HTML", "CSS", "SQL"], 0),
    crear_pregunta("¿Qué dispositivo se usa para imprimir?", ["Scanner", "Impresora", "Teclado", "Mouse"], 1),
    crear_pregunta("¿Qué es la nube (cloud computing)?", ["Almacenamiento online", "Un meteorito", "Un programa", "Un antivirus"], 0),
    crear_pregunta("¿Qué significa 'Wi-Fi'?", ["Wireless Fidelity", "Wide Frequency", "Web Finder", "Wired Fidelity"], 0),
    crear_pregunta("¿Cuál es un navegador web?", ["Google Chrome", "Windows", "Excel", "PowerPoint"], 0),
]


# ============================================================
# PREPARATORIA
# ============================================================

# --- Matemáticas avanzadas (10 preguntas) ---
CURSOS["Preparatoria"]["modulos"]["Matemáticas avanzadas"] = [
    crear_pregunta("Derivada de f(x) = x²", ["2x", "x", "2", "x²"], 0),
    crear_pregunta("∫ 2x dx", ["x² + C", "2x + C", "x²/2 + C", "x²"], 0),
    crear_pregunta("Límite cuando x→0 de sen(x)/x", ["0", "1", "∞", "No existe"], 1),
    crear_pregunta("log₂ 8 = ?", ["2", "3", "4", "8"], 1),
    crear_pregunta("¿Cuál es la matriz identidad 2x2?", ["[[1,0],[0,1]]", "[[0,1],[1,0]]", "[[1,1],[1,1]]", "[[0,0],[0,0]]"], 0),
    crear_pregunta("¿Cuál es la probabilidad de obtener un 6 al lanzar un dado?", ["1/2", "1/6", "1/3", "1/12"], 1),
    crear_pregunta("¿Cuál es el valor de e (número de Euler) aproximado?", ["2.718", "3.1416", "1.618", "2.302"], 0),
    crear_pregunta("La suma de ángulos internos de un triángulo es:", ["90°", "180°", "270°", "360°"], 1),
    crear_pregunta("Resuelve: |x-3| = 5", ["x=8 o x=-2", "x=2 o x=8", "x=-8 o x=2", "x=3"], 0),
    crear_pregunta("¿Qué es un número complejo?", ["a+bi", "a/b", "√x", "log x"], 0),
]

# --- Física básica (10 preguntas) ---
CURSOS["Preparatoria"]["modulos"]["Física básica"] = [
    crear_pregunta("Fórmula de la velocidad:", ["v = d/t", "v = m*a", "v = F/m", "v = p/v"], 0),
    crear_pregunta("¿Qué ley dice que a toda acción hay reacción?", ["Newton 1", "Newton 2", "Newton 3", "Ley de Gravitación"], 2),
    crear_pregunta("Unidad de fuerza en el SI:", ["Newton", "Joule", "Watt", "Pascal"], 0),
    crear_pregunta("¿Qué es la inercia?", ["Tendencia a cambiar", "Resistencia al cambio", "Aceleración", "Masa"], 1),
    crear_pregunta("¿Cuál es la energía cinética de 2 kg a 3 m/s?", ["6 J", "9 J", "18 J", "12 J"], 1, "Ec=½mv²=½*2*9=9 J"),
    crear_pregunta("¿Qué fenómeno explica la refracción de la luz?", ["Cambio de medio", "Reflejo", "Dispersión", "Difracción"], 0),
    crear_pregunta("Ley de Ohm:", ["V=IR", "P=VI", "I=V/R", "R=V/I"], 0),
    crear_pregunta("¿Qué tipo de onda es el sonido?", ["Electromagnética", "Mecánica longitudinal", "Transversal", "Gravitacional"], 1),
    crear_pregunta("¿Cuál es la aceleración de la gravedad en la Tierra (m/s²)?", ["9.8", "10", "8.9", "11.2"], 0),
    crear_pregunta("¿Qué partícula tiene carga negativa?", ["Protón", "Neutrón", "Electrón", "Positrón"], 2),
]

# --- Química general (10 preguntas) ---
CURSOS["Preparatoria"]["modulos"]["Química general"] = [
    crear_pregunta("¿Cuál es el símbolo del sodio?", ["S", "Na", "So", "K"], 1),
    crear_pregunta("¿Qué tipo de enlace comparten electrones?", ["Iónico", "Covalente", "Metálico", "Puente H"], 1),
    crear_pregunta("¿Cuántos electrones tiene el átomo de carbono (Z=6)?", ["6", "12", "4", "8"], 0),
    crear_pregunta("¿Qué es el pH?", ["Potencial de hidrógeno", "Partes por millón", "Peso atómico", "Presión hidráulica"], 0),
    crear_pregunta("¿Cuál es el gas más abundante en la atmósfera?", ["Oxígeno", "Nitrógeno", "CO₂", "Argón"], 1),
    crear_pregunta("La tabla periódica está ordenada por:", ["Masa atómica", "Número atómico", "Electronegatividad", "Año de descubrimiento"], 1),
    crear_pregunta("¿Qué elemento es un metal alcalino?", ["Li", "Mg", "Al", "Fe"], 0),
    crear_pregunta("Fórmula del agua oxigenada:", ["H₂O", "H₂O₂", "HO", "O₂H"], 1),
    crear_pregunta("¿Qué es una reacción endotérmica?", ["Absorbe calor", "Libera calor", "Explosiva", "Rápida"], 0),
    crear_pregunta("¿Cuál es el número de Avogadro?", ["6.022×10²³", "3.14×10²³", "6.022×10²⁴", "1.6×10⁻¹⁹"], 0),
]

# --- Literatura y análisis (10 preguntas) ---
CURSOS["Preparatoria"]["modulos"]["Literatura y análisis"] = [
    crear_pregunta("¿Quién escribió 'Cien años de soledad'?", ["Mario Vargas Llosa", "Gabriel García Márquez", "Julio Cortázar", "Carlos Fuentes"], 1),
    crear_pregunta("¿Qué movimiento literario es 'El Romanticismo'?", ["Razón", "Sentimiento y libertad", "Realidad objetiva", "Forma perfecta"], 1),
    crear_pregunta("Género de 'La Ilíada':", ["Épico", "Lírico", "Dramático", "Narrativo"], 0),
    crear_pregunta("¿Qué figura retórica es 'El silencio habla'?", ["Metáfora", "Oxímoron", "Paradoja", "Símil"], 1),
    crear_pregunta("Autor de 'Rayuela':", ["Cortázar", "Borges", "Paz", "Rulfo"], 0),
    crear_pregunta("¿Qué obra escribió Shakespeare?", ["Hamlet", "El Quijote", "La Divina Comedia", "Fausto"], 0),
    crear_pregunta("¿Qué es un soneto?", ["14 versos endecasílabos", "10 versos", "8 versos", "Poema sin rima"], 0),
    crear_pregunta("¿Qué corriente literaria exalta la naturaleza?", ["Realismo", "Modernismo", "Romanticismo", "Barroco"], 2),
    crear_pregunta("Personaje principal de 'El Principito':", ["Zorro", "Rosa", "Principito", "Aviador"], 2),
    crear_pregunta("¿Qué poeta mexicano ganó el Nobel?", ["Octavio Paz", "Jaime Sabines", "Sor Juana", "Pablo Neruda"], 0),
]

# --- Inglés básico/intermedio (10 preguntas) ---
CURSOS["Preparatoria"]["modulos"]["Inglés básico/intermedio"] = [
    crear_pregunta("Significado de 'Hello':", ["Adiós", "Hola", "Gracias", "Por favor"], 1),
    crear_pregunta("Pasado de 'go':", ["Went", "Gone", "Goed", "Going"], 0),
    crear_pregunta("¿Cómo se dice 'libro' en inglés?", ["Book", "Pen", "Table", "Chair"], 0),
    crear_pregunta("Traduce: 'Yo como manzanas'", ["I eat apples", "I eats apple", "Me eat apples", "I am eat apples"], 0),
    crear_pregunta("¿Qué significa 'Sorry'?", ["Lo siento", "Ayuda", "Gracias", "Bien"], 0),
    crear_pregunta("¿Cuál es el superlativo de 'good'?", ["Best", "Better", "Goodest", "More good"], 0),
    crear_pregunta("Oración en futuro: 'She ___ visit us tomorrow'", ["will", "is", "are", "going"], 0),
    crear_pregunta("Plural de 'child':", ["Childs", "Children", "Childes", "Childern"], 1),
    crear_pregunta("¿Qué significa 'Weather'?", ["Tiempo atmosférico", "Clima emocional", "Clima político", "Estado"], 0),
    crear_pregunta("¿Cuál es el pronombre objetivo de 'they'?", ["Them", "Their", "Theirs", "They"], 0),
]


# ============================================================
# UNIVERSIDAD
# ============================================================

# --- Pensamiento crítico (10 preguntas) ---
CURSOS["Universidad"]["modulos"]["Pensamiento crítico"] = [
    crear_pregunta("¿Qué es una falacia ad hominem?", ["Atacar a la persona", "Falsa analogía", "Generalización apresurada", "Causa falsa"], 0),
    crear_pregunta("Premisa: Todos los hombres son mortales. Sócrates es hombre. Conclusión:", ["Sócrates es mortal", "Sócrates es inmortal", "Los hombres son inmortales", "Nada"], 0),
    crear_pregunta("¿Qué habilidad evalúa el pensamiento crítico?", ["Memorizar", "Analizar argumentos", "Crear arte", "Deportes"], 1),
    crear_pregunta("Ejemplo de sesgo de confirmación:", ["Buscar datos que confirmen mi idea", "Rechazar toda evidencia", "Preferir lo nuevo", "Seguir a la mayoría"], 0),
    crear_pregunta("¿Qué es un argumento deductivo válido?", ["Si premisas verdaderas, conclusión verdadera", "Conclusión probable", "Basado en opiniones", "Estadístico"], 0),
    crear_pregunta("¿Qué principio dice que 'lo que es, es'?", ["Identidad", "No contradicción", "Tercero excluido", "Razón suficiente"], 0),
    crear_pregunta("¿Cómo se llama la falacia de 'si no estás conmigo, estás contra mí'?", ["Falsa dicotomía", "Pendiente resbaladiza", "Petición de principio", "Hombre de paja"], 0),
    crear_pregunta("¿Qué es el escepticismo?", ["Duda metódica", "Creencia absoluta", "Fe ciega", "Racionalismo"], 0),
    crear_pregunta("Un argumento inductivo fuerte:", ["Conclusión probable", "Verdad absoluta", "Falaz", "Deductivo"], 0),
    crear_pregunta("¿Qué filósofo planteó el 'Método cartesiano'?", ["Descartes", "Kant", "Platón", "Aristóteles"], 0),
]

# --- Investigación académica (10 preguntas) ---
CURSOS["Universidad"]["modulos"]["Investigación académica"] = [
    crear_pregunta("¿Qué es una hipótesis?", ["Suposición a probar", "Resultado final", "Pregunta de investigación", "Conclusión"], 0),
    crear_pregunta("¿Qué tipo de investigación busca causas?", ["Correlacional", "Descriptiva", "Exploratoria", "Experimental"], 3),
    crear_pregunta("¿Qué es una variable dependiente?", ["La que se mide", "La que manipula", "Constante", "Aleatoria"], 0),
    crear_pregunta("¿Qué significa 'muestra'?", ["Subconjunto de población", "Toda la población", "Error estadístico", "Instrumento"], 0),
    crear_pregunta("Formato de citación APA: (Autor, año) se usa en:", ["Citas en texto", "Referencias", "Notas al pie", "Índice"], 0),
    crear_pregunta("¿Qué es un artículo científico revisado por pares?", ["Publ. en revista indexada", "Blog", "Tesis", "Libro"], 0),
    crear_pregunta("Pasos del método científico:", ["Observación, hipótesis, experimento, conclusión", "Teoría, ley, hipótesis", "Análisis, síntesis, conclusión", "Pregunta, respuesta"], 0),
    crear_pregunta("¿Qué mide la validez en investigación?", ["Instrumento mide lo que debe", "Consistencia de resultados", "Aplicabilidad", "Muestreo"], 0),
    crear_pregunta("¿Qué tipo de muestreo es el aleatorio simple?", ["Probabilístico", "No probabilístico", "Conveniencia", "Bola de nieve"], 0),
    crear_pregunta("¿Qué es un DOI?", ["Identificador digital", "Índice de impacto", "Número de ISSN", "Código de barras"], 0),
]

# --- Comunicación profesional (10 preguntas) ---
CURSOS["Universidad"]["modulos"]["Comunicación profesional"] = [
    crear_pregunta("¿Qué debe evitarse en un correo profesional?", ["Lenguaje informal", "Saludo", "Despedida", "Asunto claro"], 0),
    crear_pregunta("¿Qué es la comunicación asertiva?", ["Expresar ideas sin agresión", "Callar siempre", "Gritar", "Imponer"], 0),
    crear_pregunta("¿Qué es un resumen ejecutivo?", ["Síntesis de un documento", "Carta de presentación", "Índice", "Conclusión"], 0),
    crear_pregunta("Elemento clave en una presentación oral:", ["Contacto visual", "Leer diapositivas", "Monótono", "Rapidez"], 0),
    crear_pregunta("¿Qué es el feedback?", ["Retroalimentación", "Crítica destructiva", "Elogio", "Silencio"], 0),
    crear_pregunta("¿Cómo se llama la comunicación no verbal con las manos?", ["Gestos", "Postura", "Proxémica", "Paralingüística"], 0),
    crear_pregunta("¿Qué CV es más recomendado en la actualidad?", ["CV funcional", "CV cronológico inverso", "CV extenso", "CV con foto"], 1),
    crear_pregunta("¿Qué significa 'CCO' en un correo?", ["Copia oculta", "Copia de cortesía", "Con copia a", "Carta con oficio"], 0),
    crear_pregunta("¿Qué es la escucha activa?", ["Prestar atención y responder", "Oír sin responder", "Interrumpir", "No mirar"], 0),
    crear_pregunta("¿Qué herramienta colaborativa es común?", ["Teams", "Word", "Excel", "Paint"], 0),
]

# --- Matemática aplicada (10 preguntas) ---
CURSOS["Universidad"]["modulos"]["Matemática aplicada"] = [
    crear_pregunta("¿Qué es una matriz inversa?", ["A*A⁻¹=I", "A²=I", "A+A⁻¹=0", "det(A)=0"], 0),
    crear_pregunta("Derivada de ln(x):", ["1/x", "x", "eˣ", "1/x²"], 0),
    crear_pregunta("∫ eˣ dx", ["eˣ+C", "xeˣ+C", "eˣ", "ln(eˣ)"], 0),
    crear_pregunta("¿Qué es un valor propio?", ["λ que satisface Av=λv", "Máximo de matriz", "Determinante", "Traza"], 0),
    crear_pregunta("Fórmula de interés compuesto:", ["A=P(1+r/n)^(nt)", "A=Pr", "A=P(1+rt)", "A=P/(1+rt)"], 0),
    crear_pregunta("¿Qué es una función convexa?", ["Curva hacia arriba", "Curva hacia abajo", "Lineal", "Discontinua"], 0),
    crear_pregunta("Método de Newton-Raphson sirve para:", ["Encontrar raíces", "Derivar", "Integrar", "Optimizar"], 0),
    crear_pregunta("¿Qué mide la desviación estándar?", ["Dispersión", "Media", "Moda", "Mediana"], 0),
    crear_pregunta("¿Qué es un número primo?", ["Divisible solo por 1 y sí mismo", "Par", "Múltiplo de 2", "Decimal"], 0),
    crear_pregunta("¿Cuánto es 5! (factorial)?", ["120", "24", "60", "25"], 0),
]

# --- Ética profesional (10 preguntas) ---
CURSOS["Universidad"]["modulos"]["Ética profesional"] = [
    crear_pregunta("¿Qué es un dilema ético?", ["Conflicto de valores", "Fácil decisión", "Ley", "Norma"], 0),
    crear_pregunta("¿Qué principio ético implica 'hacer el bien'?", ["Beneficencia", "No maleficencia", "Justicia", "Autonomía"], 0),
    crear_pregunta("¿Qué es el código deontológico?", ["Normas de la profesión", "Ley penal", "Reglamento interno", "Contrato"], 0),
    crear_pregunta("Ejemplo de conflicto de intereses:", ["Trabajador que contrata a familiar", "Seguir la ley", "Denunciar corrupción", "Ayudar a colega"], 0),
    crear_pregunta("¿Qué implica la responsabilidad profesional?", ["Responder por actos", "Hacer solo lo mínimo", "Cobrar más", "Evitar riesgos"], 0),
    crear_pregunta("¿Qué es la transparencia?", ["Acceso a la información", "Secreto", "Lealtad", "Eficiencia"], 0),
    crear_pregunta("¿Cuál es un valor ético universal?", ["Honestidad", "Éxito", "Fama", "Poder"], 0),
    crear_pregunta("¿Qué se entiende por 'corrupción'?", ["Abuso de poder para beneficio", "Error honesto", "Incumplimiento leve", "Discusión"], 0),
    crear_pregunta("¿Qué es la sostenibilidad en ética?", ["Satisfacer necesidades sin comprometer futuro", "Rentabilidad", "Ahorro", "Tecnología"], 0),
    crear_pregunta("¿Cuál es el principal deber de un ingeniero con la sociedad?", ["Seguridad y bienestar", "Maximizar ganancias", "Acatar jefes", "Competir"], 0),
]


# ============================================================
# CULTURA GENERAL
# ============================================================

# --- Mundo y geografía (10 preguntas) ---
CURSOS["Cultura General"]["modulos"]["Mundo y geografía"] = [
    crear_pregunta("¿Cuál es la capital de Japón?", ["Tokio", "Pekín", "Seúl", "Bangkok"], 0),
    crear_pregunta("¿Cuál es el país más extenso del mundo?", ["Rusia", "Canadá", "China", "EE.UU."], 0),
    crear_pregunta("¿Qué océano baña la costa oeste de México?", ["Pacífico", "Atlántico", "Índico", "Ártico"], 0),
    crear_pregunta("¿Cuál es el río más caudaloso del mundo?", ["Amazonas", "Nilo", "Yangtsé", "Misisipi"], 0),
    crear_pregunta("¿En qué continente está Australia?", ["Oceanía", "Asia", "América", "África"], 0),
    crear_pregunta("¿Cuál es la montaña más alta de la Tierra?", ["Everest", "K2", "Kanchenjunga", "Makalu"], 0),
    crear_pregunta("¿Qué país tiene forma de bota?", ["Italia", "España", "Francia", "Grecia"], 0),
    crear_pregunta("¿Cuál es la ciudad más poblada del mundo?", ["Tokio", "Delhi", "Shanghái", "CDMX"], 0),
    crear_pregunta("¿Qué desierto es el más grande fuera de los polos?", ["Sáhara", "Gobi", "Kalahari", "Atacama"], 0),
    crear_pregunta("¿Qué país es conocido como 'la tierra del sol naciente'?", ["Japón", "China", "Corea", "Tailandia"], 0),
]

# --- Historia universal (10 preguntas) ---
CURSOS["Cultura General"]["modulos"]["Historia universal"] = [
    crear_pregunta("¿Quién fue el primer presidente de Estados Unidos?", ["George Washington", "Thomas Jefferson", "John Adams", "Abraham Lincoln"], 0),
    crear_pregunta("¿En qué año terminó la Segunda Guerra Mundial?", ["1945", "1939", "1944", "1946"], 0),
    crear_pregunta("¿Quién pintó 'La noche estrellada'?", ["Van Gogh", "Picasso", "Monet", "Rembrandt"], 0),
    crear_pregunta("¿Qué civilización construyó las pirámides de Giza?", ["Egipcia", "Sumeria", "India", "China"], 0),
    crear_pregunta("¿Quién fue Cleopatra?", ["Reina de Egipto", "Diosa griega", "Filósofa romana", "Escritora"], 0),
    crear_pregunta("¿Qué emperador romano supuestamente 'tocó la lira mientras Roma ardía'?", ["Nerón", "César", "Augusto", "Tiberio"], 0),
    crear_pregunta("¿Qué movimiento cultural fue el Renacimiento?", ["Florecimiento artístico", "Revolución industrial", "Ilustración", "Barroco"], 0),
    crear_pregunta("¿Quién escribió 'La República'?", ["Platón", "Aristóteles", "Sócrates", "Cicerón"], 0),
    crear_pregunta("¿Cuál fue la primera civilización de América?", ["Olmeca", "Maya", "Azteca", "Inca"], 0),
    crear_pregunta("¿Qué tratado puso fin a la Primera Guerra Mundial?", ["Versalles", "París", "Londres", "Berlín"], 0),
]

# --- Ciencia y tecnología (10 preguntas) ---
CURSOS["Cultura General"]["modulos"]["Ciencia y tecnología"] = [
    crear_pregunta("¿Quién descubrió la penicilina?", ["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Einstein"], 0),
    crear_pregunta("¿Qué teoría propuso Charles Darwin?", ["Evolución por selección natural", "Relatividad", "Gravitación", "Big Bang"], 0),
    crear_pregunta("¿Qué es la inteligencia artificial?", ["Máquinas que aprenden", "Robots físicos", "Código binario", "Internet"], 0),
    crear_pregunta("¿Qué empresa creó el iPhone?", ["Apple", "Samsung", "Google", "Microsoft"], 0),
    crear_pregunta("¿Qué es un algoritmo?", ["Secuencia de pasos", "Virus", "Lenguaje", "Hardware"], 0),
    crear_pregunta("¿Quién es el creador de la teoría de la relatividad?", ["Albert Einstein", "Newton", "Galileo", "Max Planck"], 0),
    crear_pregunta("¿Qué significa ADN?", ["Ácido desoxirribonucleico", "Ácido ribonucleico", "Asociación de datos", "Almacenamiento digital"], 0),
    crear_pregunta("¿Qué es la vacuna contra el COVID-19?", ["Inmunización", "Antibiótico", "Analgésico", "Antiviral"], 0),
    crear_pregunta("¿Qué es un agujero negro?", ["Región con gravedad extrema", "Estrella muerta", "Planeta gaseoso", "Nube interestelar"], 0),
    crear_pregunta("¿Cuál es el planeta más grande del sistema solar?", ["Júpiter", "Saturno", "Neptuno", "Urano"], 0),
]

# --- Arte y cultura (10 preguntas) ---
CURSOS["Cultura General"]["modulos"]["Arte y cultura"] = [
    crear_pregunta("¿Quién pintó 'La última cena'?", ["Da Vinci", "Miguel Ángel", "Rafael", "Caravaggio"], 0),
    crear_pregunta("¿Qué ballet clásico cuenta la historia de un cisne?", ["El lago de los cisnes", "El cascanueces", "La bella durmiente", "Giselle"], 0),
    crear_pregunta("¿Cuál es la obra más famosa de Shakespeare?", ["Hamlet", "Romeo y Julieta", "Macbeth", "El rey Lear"], 0),
    crear_pregunta("¿Qué instrumento toca Beethoven?", ["Piano", "Violín", "Flauta", "Guitarra"], 0),
    crear_pregunta("¿Dónde está el Museo del Prado?", ["Madrid", "París", "Londres", "Roma"], 0),
    crear_pregunta("¿Qué estilo arquitectónico tiene la Sagrada Familia?", ["Modernismo", "Gótico", "Románico", "Barroco"], 0),
    crear_pregunta("¿Quién es Frida Kahlo?", ["Pintora mexicana", "Cantante", "Poetisa", "Actriz"], 0),
    crear_pregunta("¿Qué es la Ópera?", ["Teatro musical", "Ballet", "Orquesta", "Coro"], 0),
    crear_pregunta("¿Qué famoso mural pintó Diego Rivera en el Palacio Nacional?", ["Historia de México", "Sueño de una tarde", "El hombre controlador", "Mercado"], 0),
    crear_pregunta("¿Cuál es la danza nacional de Argentina?", ["Tango", "Salsa", "Flamenco", "Cumbia"], 0),
]

# --- Actualidad y sociedad (10 preguntas) ---
CURSOS["Cultura General"]["modulos"]["Actualidad y sociedad"] = [
    crear_pregunta("¿Qué es el cambio climático?", ["Aumento temperatura global", "Contaminación local", "Hole de ozono", "Inundaciones"], 0),
    crear_pregunta("¿Qué es la ONU?", ["Organización de Naciones Unidas", "Organización del Tratado Atlántico", "Unión Europea", "Gobierno mundial"], 0),
    crear_pregunta("¿Qué premio se otorga a la paz?", ["Nobel de la Paz", "Oscar", "Grammy", "Príncipe de Asturias"], 0),
    crear_pregunta("¿Qué es la OMS?", ["Organización Mundial de la Salud", "Oficina Meteorológica", "Organización Militar", "Oscar de la Medicina"], 0),
    crear_pregunta("¿Qué hizo Greta Thunberg?", ["Activismo climático", "Cantar", "Actuar", "Escribir"], 0),
    crear_pregunta("¿Qué es la inflación?", ["Aumento de precios", "Bajada de precios", "Crecimiento económico", "Devaluación"], 0),
    crear_pregunta("¿Qué red social es propiedad de Meta?", ["Facebook", "Twitter", "TikTok", "Snapchat"], 0),
    crear_pregunta("¿Qué significa 'brecha digital'?", ["Desigualdad acceso a tecnología", "Hackeo", "Vacío de datos", "Ciberataque"], 0),
    crear_pregunta("¿Qué es la sostenibilidad?", ["Desarrollo que no agota recursos", "Crecimiento ilimitado", "Reciclaje", "Energía eólica"], 0),
    crear_pregunta("¿Qué es la 'huella de carbono'?", ["Medida de emisiones CO₂", "Marca en el suelo", "Combustible fósil", "Efecto invernadero"], 0),
]


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def validar_banco():
    total_cursos = len(CURSOS)
    total_modulos = 0
    total_preguntas = 0
    for curso in CURSOS.values():
        modulos = curso["modulos"]
        total_modulos += len(modulos)
        for preguntas in modulos.values():
            total_preguntas += len(preguntas)
    return {"cursos": total_cursos, "modulos": total_modulos, "preguntas": total_preguntas}

def obtener_cursos():
    return list(CURSOS.keys())

def obtener_modulos(curso):
    if curso in CURSOS:
        return list(CURSOS[curso]["modulos"].keys())
    return []

def obtener_preguntas(curso, modulo):
    try:
        return CURSOS[curso]["modulos"][modulo]
    except KeyError:
        return []

if __name__ == "__main__":
    resumen = validar_banco()
    print("Cursos:", resumen["cursos"])
    print("Módulos:", resumen["modulos"])
    print("Preguntas cargadas:", resumen["preguntas"])