import random
from fuzzywuzzy import process
from unidecode import unidecode  # Para manejar los acentos

# Grupos de preguntas relacionadas
question_groups = {
    "horarios": [
        "¿Cual es el horario de atencion?",
        "¿Cuales son los contactos de atencion?",
        "¿Que turnos ofrece la UPTex?"
    ],
    "admision": [
        "¿Como puedo ingresar a una carrera en la UPTex?",
        "¿Cual es el promedio minimo para ingresar a la UPTex?",
        "¿Cuales son las fechas de inscripcion y admision?"
    ],
    "carreras": [
        "¿Que carreras ofrece la UPTex?",
        "¿Que duracion tienen las carreras?",
        "¿Cual es el plan de estudios de cada carrera?"
    ],
    "tramites": [
        "¿La UPTex cuenta con programas de posgrado o maestria?",
        "¿Como realizo el tramite de titulacion?",
        "¿Que becas o apoyos financieros ofrece para los estudiantes?"
    ],
    "instalaciones": [
        "¿Donde se encuentra ubicada la UPTex?",
        "¿Que servicios ofrece la UPTex en sus instalaciones?",
        "¿Hay areas deportivas en la UPTex?"
    ],
    "becas": [
        "¿Que tipos de becas ofrece la UPTex?",
        "¿Cuales son los requisitos para obtener una beca?",
        "¿Como puedo solicitar una beca en la UPTex?"
    ]
}

# Base de datos de respuestas
educational_offers = {
    "¿Cual es el horario de atencion?": "El horario de atencion en la UPTex es de lunes a viernes, de 8:00 am a 6:00 pm.",
    "¿Cuales son los contactos de atencion?": "Direccion Academica: (01) 595 95 4 23 61, Servicios Escolares: (01) 595 92 1 30 27, rectoria.uptex@uptex.edu.mx.",
    "¿Que turnos ofrece la UPTex?": "Turno matutino: 7:00 am a 3:00 pm, Turno vespertino: 12:00 pm a 8:00 pm.",
    "¿Como puedo ingresar a una carrera en la UPTex?": "Debes realizar un examen de admision y alcanzar el puntaje requerido para cada carrera o, si obtuviste un promedio general de 8.0 en tu bachillerato, puedes presentar tu solicitud de pase directo.",
    "¿Cual es el promedio minimo para ingresar a la UPTex?": "El promedio minimo para ingresar es de 7.0 general.",
    "¿Cuales son las fechas de inscripcion y admision?": "La convocatoria para nuevo ingreso se lleva a cabo cada año en el mes de mayo. Si fuiste seleccionado, puedes iniciar tu proceso de inscripcion en septiembre.",
    "¿Que carreras ofrece la UPTex?": "Ingenieria en Sistemas Electronicos, Ingenieria en Mecatronica, Ingenieria en Tecnologias de la Informacion e Innovacion Digital, Ingenieria en Logistica y Transporte, Licenciatura en Administracion y Gestion de Empresas, Licenciatura en Comercio Internacional y Aduanas.",
    "¿Que duracion tienen las carreras?": "Todas las carreras son de 3 años y 4 meses, organizados en cuatrimestres.",
    "¿Cual es el plan de estudios de cada carrera?": "El plan de estudios varía según la carrera y puede consultarse en el sitio oficial de la UPTex.",
    "¿La UPTex cuenta con programas de posgrado o maestria?": "Por ahora, en la UPTex puedes obtener tu maestria en Comercio Logistica Internacional.",
    "¿Como realizo el tramite de titulacion?": "El tramite de titulacion se realiza a traves del portal en linea.",
    "¿Que becas o apoyos financieros ofrece para los estudiantes?": "Madres que se encuentran estudiando, discapacidad, estudiantes indigenas, descuentos de pago.",
    "¿Donde se encuentra ubicada la UPTex?": "La UPTex esta ubicada en Texcoco, Estado de Mexico.",
    "¿Que servicios ofrece la UPTex en sus instalaciones?": "La UPTex cuenta con bibliotecas, cafeterias, laboratorios, y areas de estudio grupales.",
    "¿Hay areas deportivas en la UPTex?": "Si, la UPTex dispone de areas deportivas para los estudiantes.",
    "¿Que tipos de becas ofrece la UPTex?": "La UPTex ofrece becas para madres estudiantes, estudiantes con discapacidad, y estudiantes indigenas.",
    "¿Cuales son los requisitos para obtener una beca?": "Los requisitos incluyen estar inscrito en la UPTex, mantener un promedio minimo de 8.0 y cumplir con la documentacion solicitada.",
    "¿Como puedo solicitar una beca en la UPTex?": "Puedes solicitar una beca directamente en el area de servicios escolares, presentando tu documentacion completa."
}

def chatbot_response(user_input):
    # Transformar el texto del usuario a minúsculas y eliminar acentos
    normalized_input = unidecode(user_input.lower())

    # Verificar si el usuario seleccionó una categoría
    if normalized_input in question_groups:
        # Seleccionar preguntas al azar de la categoría
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
