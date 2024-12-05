import random
from fuzzywuzzy import process
from unidecode import unidecode  # Para manejar los acentos

# Grupos de preguntas relacionadas
question_groups = {
    "horarios": [
        "¿Cuál es el horario de atención?",
        "¿Cuáles son los contactos de atención?",
        "¿Qué turnos ofrece la UPTex?",
        "¿Cuál es el horario de atención para los alumnos?"
    ],
    "admision": [  # Cambiado "admisión" por "admision"
        "¿Cómo puedo ingresar a una carrera en la UPTex?",
        "¿Cuál es el promedio mínimo para ingresar a la UPTex?",
        "¿Por qué su modelo educativo incluye inglés?",
        "¿Cuándo se abre la convocatoria para nuevo ingreso?",
        "¿Cuál es el promedio mínimo requerido para ingresar a la Universidad Politécnica de Texcoco?"
    ],
    "carreras": [
        "¿Qué carreras ofrece la UPTex?",
        "¿Qué duración tienen las carreras?",
        "¿Cuál es el plan de estudios de cada carrera?",
        "¿Qué carreras ofrece la Universidad Politécnica de Texcoco?",
        "¿Cuál es la duración de las carreras?"
    ],
    "tramites": [  # Cambiado "trámites" por "tramites"
        "¿La UPTex cuenta con programas de posgrado o maestría?",
        "¿Cómo realizo el trámite de titulación?",
        "¿Qué becas o apoyos financieros ofrece para los estudiantes?",
        "¿Cuál es el proceso para titularse en la Universidad Politécnica de Texcoco?",
        "¿UPTex proporciona seguro social a los estudiantes?"
    ],
    "instalaciones": [
        "¿Dónde se encuentra ubicada la UPTex?",
        "¿Qué servicios ofrece la UPTex en sus instalaciones?",
        "¿Hay áreas deportivas en la UPTex?",
        "¿UPTex ofrece actividades deportivas y/o culturales?"
    ],
    "becas": [
        "¿Qué tipos de becas ofrece la UPTex?",
        "¿Cuáles son los requisitos para obtener una beca?",
        "¿Cómo puedo solicitar una beca en la UPTex?",
        "¿La UPTex ofrece becas o apoyos a los estudiantes?",
        "¿UPTex ofrece becas tanto federales como estatales?"
    ]
}

# Base de datos de respuestas
educational_offers = {
    "¿Cuál es el horario de atención?": "El horario de atención en la UPTex es de lunes a viernes, de 8:00 am a 6:00 pm.",
    "¿Cuáles son los contactos de atención?": "Dirección Académica: (01) 595 95 4 23 61, Servicios Escolares: (01) 595 92 1 30 27, rectoria.uptex@uptex.edu.mx.",
    "¿Qué turnos ofrece la UPTex?": "Turno matutino: 7:00 am a 3:00 pm, Turno vespertino: 12:00 pm a 8:00 pm.",
    "¿Cuál es el horario de atención para los alumnos?": "El horario de atención es de 9:00 am a 6:00 pm, de lunes a viernes.",
    "¿Cómo puedo ingresar a una carrera en la UPTex?": "Debes realizar un examen de admisión y alcanzar el puntaje requerido para cada carrera o, si obtuviste un promedio general de 8.0 en tu bachillerato, puedes presentar tu solicitud de pase directo.",
    "¿Cuál es el promedio mínimo para ingresar a la UPTex?": "El promedio mínimo para ingresar es de 7.0 general.",
    "¿Cuándo se abre la convocatoria para nuevo ingreso?": "La convocatoria para nuevo ingreso se lleva a cabo cada año en el mes de mayo.",
    "¿Cuál es el promedio mínimo requerido para ingresar a la Universidad Politécnica de Texcoco?": "El promedio mínimo requerido para ingresar es de 7.0.",
    "¿Qué carreras ofrece la UPTex?": "Ingeniería en Sistemas Electrónicos, Ingeniería en Mecatrónica, Ingeniería en Tecnologías de la Información e Innovación Digital, Ingeniería en Logística y Transporte, Licenciatura en Administración y Gestión de Empresas, Licenciatura en Comercio Internacional y Aduanas.",
    "¿Qué duración tienen las carreras?": "Todas las carreras son de 3 años y 4 meses, organizados en cuatrimestres.",
    "¿Cuál es el plan de estudios de cada carrera?": "El plan de estudios varía según la carrera y puede consultarse en el sitio oficial de la UPTex.",
    "¿Qué carreras ofrece la Universidad Politécnica de Texcoco?": "Ingeniería en Electrónica y Telecomunicaciones, Ingeniería en Robótica, Ingeniería en Sistemas Computacionales, Ingeniería en Logística y Transporte, Licenciatura en Administración y Gestión de Pequeñas y Medianas Empresas, Licenciatura en Comercio Internacional y Aduanas.",
    "¿Cuál es la duración de las carreras?": "Todas las carreras tienen una duración de 10 cuatrimestres.",
    "¿La UPTex cuenta con programas de posgrado o maestría?": "Por ahora, en la UPTex puedes obtener tu maestría en Comercio Logística Internacional.",
    "¿Cómo realizo el trámite de titulación?": "El trámite de titulación se realiza a través del portal en línea.",
    "¿Qué becas o apoyos financieros ofrece para los estudiantes?": "Madres que se encuentran estudiando, discapacidad, estudiantes indígenas, descuentos de pago.",
    "¿Cuál es el proceso para titularse en la Universidad Politécnica de Texcoco?": "Para titularse, es necesario tener el 100% de los créditos aprobados y haber concluido el Servicio Social.",
    "¿UPTex proporciona seguro social a los estudiantes?": "Sí, todos los alumnos cuentan con el seguro médico del IMSS.",
    "¿Dónde se encuentra ubicada la UPTex?": "La UPTex está ubicada en Texcoco, Estado de México.",
    "¿Qué servicios ofrece la UPTex en sus instalaciones?": "La UPTex cuenta con bibliotecas, cafeterías, laboratorios, y áreas de estudio grupales.",
    "¿Hay áreas deportivas en la UPTex?": "Sí, la UPTex dispone de áreas deportivas para los estudiantes.",
    "¿UPTex ofrece actividades deportivas y/o culturales?": "Sí, se ofrecen talleres de fútbol, baloncesto, voleibol, atletismo, entre otros.",
    "¿Qué tipos de becas ofrece la UPTex?": "La UPTex ofrece becas para madres estudiantes, estudiantes con discapacidad, y estudiantes indígenas.",
    "¿Cuáles son los requisitos para obtener una beca?": "Los requisitos incluyen estar inscrito en la UPTex, mantener un promedio mínimo de 8.0 y cumplir con la documentación solicitada.",
    "¿Cómo puedo solicitar una beca en la UPTex?": "Puedes solicitar una beca directamente en el área de servicios escolares, presentando tu documentación completa.",
    "¿La UPTex ofrece becas o apoyos a los estudiantes?": "Sí, se ofrecen becas tanto federales como estatales.",
    "¿UPTex ofrece becas tanto federales como estatales?": "Sí, ambas opciones están disponibles para apoyar a los estudiantes.",
    "¿Por qué su modelo educativo incluye inglés?": "En UPTex consideramos primordial el aprendizaje de un segundo idioma, ya que esto garantiza una mejor preparación en las carreras. Además, estamos en transición para convertirnos en una universidad con modelo BIS (Bilingüe, Internacional y de Sustentabilidad)."
}


def chatbot_response(user_input):
    # Transformar el texto del usuario a minúsculas y eliminar acentos
    normalized_input = unidecode(user_input.lower())

    # Verificar si el usuario seleccionó una categoría
    if normalized_input in question_groups:
        questions = question_groups[normalized_input]
        selected_questions = random.sample(questions, min(8, len(questions)))
        return {
            "response": f"Aqui tienes algunas preguntas relacionadas con {user_input}:",
            "suggestions": selected_questions
        }

    # Buscar la mejor coincidencia entre las preguntas
    normalized_questions = {unidecode(k): k for k in educational_offers.keys()}
    best_match = process.extractOne(normalized_input, normalized_questions.keys())
    if best_match and best_match[1] > 80:
        matched_question = normalized_questions[best_match[0]]
        return {"response": educational_offers[matched_question], "suggestions": []}
    else:
        # Si no se encuentra una coincidencia clara
        return {
            "response": (
                "Lo siento, no entiendo tu pregunta. Por favor intenta ser mas especifico o selecciona una categoria:"
            ),
            "suggestions": list(question_groups.keys())
        }
