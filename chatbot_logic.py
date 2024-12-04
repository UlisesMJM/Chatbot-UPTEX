from fuzzywuzzy import process

# Grupos de preguntas relacionadas
question_groups = {
    "horarios": [
        "¿Cuál es el horario de atención?",
        "¿Cuál es el horario de clases?",
        "¿Qué horario tiene la biblioteca?"
    ],
    "admisión": [
        "¿Cuáles son los requisitos de admisión?",
        "¿Cuándo abren las convocatorias?",
        "¿Cómo puedo registrarme para el examen de admisión?"
    ],
    "carreras": [
        "¿Qué carreras ofrece la UPTex?",
        "¿Qué duración tienen las carreras?",
        "¿Qué programas tienen enfoque en tecnología?"
    ]
}

# Base de datos de respuestas
educational_offers = { 
    # Horarios
    "¿Cuál es el horario de atención?": "El horario de atención en la UPTex es de lunes a viernes, de 8:00 am a 6:00 pm.",
    "horario de atención": "El horario de atención en la UPTex es de lunes a viernes, de 8:00 am a 6:00 pm.",
    "¿Cuál es el horario de clases?": "El horario de clases varía según la carrera, pero generalmente es de 7:00 am a 3:00 pm.",
    "horario de clases": "El horario de clases varía según la carrera, pero generalmente es de 7:00 am a 3:00 pm.",
    "¿Qué horario tiene la biblioteca?": "La biblioteca está abierta de lunes a viernes, de 8:00 am a 8:00 pm, y los sábados de 9:00 am a 2:00 pm.",
    "horario de la biblioteca": "La biblioteca está abierta de lunes a viernes, de 8:00 am a 8:00 pm, y los sábados de 9:00 am a 2:00 pm.",

    # Contacto
    "¿Cuál es el correo electrónico de contacto?": "Puedes contactar a la UPTex al correo: rectoria.uptex@uptex.edu.mx.",
    "correo": "Puedes contactar a la UPTex al correo: rectoria.uptex@uptex.edu.mx.",
    "contacto para mandar un correo": "Puedes contactar a la UPTex al correo: rectoria.uptex@uptex.edu.mx.",
    "¿Cómo puedo contactar a la UPTex?": "Puedes contactar a la UPTex al teléfono 5588440102 o al correo: rectoria.uptex@uptex.edu.mx.",
    "teléfono de contacto": "El teléfono de contacto de la UPTex es 5588440102.",

    # Carreras
    "¿Qué carreras ofrece la UPTex?": "La UPTex ofrece las siguientes carreras: Ingeniería en Mecatrónica, Ingeniería en Sistemas Electrónicos, Ingeniería en Tecnologías de la Información y Comunicación, Ingeniería en Logística, Licenciatura en Comercio Internacional y Aduanas, y Licenciatura en Administración.",
    "carreras disponibles": "La UPTex ofrece las siguientes carreras: Ingeniería en Mecatrónica, Ingeniería en Sistemas Electrónicos, Ingeniería en Tecnologías de la Información y Comunicación, Ingeniería en Logística, Licenciatura en Comercio Internacional y Aduanas, y Licenciatura en Administración.",
    "dime las carreras": "La UPTex ofrece las siguientes carreras: Ingeniería en Mecatrónica, Ingeniería en Sistemas Electrónicos, Ingeniería en Tecnologías de la Información y Comunicación, Ingeniería en Logística, Licenciatura en Comercio Internacional y Aduanas, y Licenciatura en Administración.",
    "¿Qué es Ingeniería en Mecatrónica?": "La Ingeniería en Mecatrónica combina la mecánica, electrónica y sistemas de control para diseñar y mejorar procesos automatizados.",
    "¿Qué es Ingeniería en Sistemas Electrónicos?": "La Ingeniería en Sistemas Electrónicos se enfoca en la creación y mantenimiento de circuitos y dispositivos electrónicos.",
    "¿Qué es Ingeniería en Tecnologías de la Información?": "Esta carrera prepara a los estudiantes en desarrollo de software, redes de comunicación y ciberseguridad.",
    "¿Qué es Ingeniería en Logística?": "La Ingeniería en Logística enseña a gestionar cadenas de suministro, transporte y almacenamiento de manera eficiente.",
    "¿Qué es la Licenciatura en Comercio Internacional?": "Esta carrera forma especialistas en comercio exterior, aduanas y logística internacional.",
    "¿Qué es la Licenciatura en Administración?": "Prepara a los estudiantes para liderar organizaciones y manejar recursos de manera eficiente.",

    # Admisión
    "¿Cuáles son los requisitos de admisión?": "Los requisitos de admisión incluyen certificado de preparatoria, acta de nacimiento, CURP y comprobante de domicilio.",
    "requisitos de admisión": "Los requisitos de admisión incluyen certificado de preparatoria, acta de nacimiento, CURP y comprobante de domicilio.",
    "¿Cuál es el promedio mínimo para ingresar?": "El promedio mínimo para ingresar a la UPTex es de 7.0.",
    "promedio mínimo": "El promedio mínimo para ingresar a la UPTex es de 7.0.",
    "¿Cuándo abren las convocatorias?": "Las convocatorias de admisión se publican cada año en mayo.",
    "convocatorias de admisión": "Las convocatorias de admisión se publican cada año en mayo.",
    "¿Cómo me registro para el examen de admisión?": "Puedes registrarte para el examen de admisión a través del sitio oficial de la UPTex siguiendo los pasos de la convocatoria.",
    "registro para examen de admisión": "Debes registrarte en línea y completar los pasos indicados en la convocatoria.",

    # Becas
    "¿La UPTex ofrece becas?": "Sí, la UPTex ofrece becas académicas, deportivas y de apoyo económico.",
    "becas disponibles": "La UPTex ofrece becas académicas, deportivas y de apoyo económico.",
    "¿Cómo puedo solicitar una beca?": "Puedes solicitar una beca a través de las convocatorias publicadas en el sitio oficial de la UPTex.",
    "solicitar beca": "Consulta las bases en la sección de convocatorias de la UPTex.",

    # Instalaciones
    "¿Qué instalaciones tiene la UPTex?": "La UPTex cuenta con laboratorios de cómputo, talleres, biblioteca, áreas deportivas y cafeterías.",
    "instalaciones de la UPTex": "La UPTex cuenta con laboratorios de cómputo, talleres, biblioteca, áreas deportivas y cafeterías.",
    "¿Tiene la UPTex biblioteca?": "Sí, la UPTex tiene una biblioteca bien equipada con recursos físicos y digitales.",
    "biblioteca de la UPTex": "La biblioteca está disponible de lunes a viernes, de 8:00 am a 8:00 pm.",

    # Actividades extracurriculares
    "¿Qué actividades extracurriculares tiene la UPTex?": "La UPTex ofrece deportes, grupos culturales y talleres de desarrollo personal.",
    "actividades extracurriculares": "Puedes participar en deportes, grupos culturales y talleres en la UPTex.",
    "¿Qué deportes ofrece la UPTex?": "La UPTex tiene equipos de fútbol, voleibol, baloncesto y más.",
    "deportes en la UPTex": "Puedes practicar fútbol, voleibol, baloncesto y atletismo en la UPTex."
}

related_questions = {
    "horarios": ["¿Cuál es el horario de clases?", "¿Qué horario tiene la biblioteca?", "¿Cuál es el horario de atención?"],
    "carreras": ["¿Qué carreras ofrece la UPTex?", "¿Qué es Ingeniería en Mecatrónica?", "¿Qué es Ingeniería en Sistemas Electrónicos?"],
    "contacto": ["¿Cuál es el correo electrónico de contacto?", "¿Cómo puedo contactar a la UPTex?", "¿Cuál es el número telefónico de la UPTex?"]
}

def chatbot_response(user_input):
    # Encuentra respuesta y sugerencias relacionadas
    response, category = get_response_and_category(user_input)  # Función que devuelve la respuesta y categoría
    suggestions = related_questions.get(category, [])
    return {"response": response, "suggestions": suggestions}

# Función para buscar preguntas relacionadas
def suggest_questions(query):
    suggestions = []
    for group, questions in question_groups.items():
        for q in questions:
            if process.extractOne(query, questions)[1] > 60:
                suggestions.extend(questions)
    return list(set(suggestions))  # Elimina duplicados

# Función principal del chatbot
def chatbot_response(user_input):
    # Buscar la mejor coincidencia
    best_match = process.extractOne(user_input, educational_offers.keys())
    if best_match and best_match[1] > 80:
        return educational_offers[best_match[0]]
    else:
        # Ofrecer sugerencias si la pregunta no es clara
        suggestions = suggest_questions(user_input)
        if suggestions:
            return f"No estoy seguro de lo que preguntas. Quizás te refieres a: {', '.join(suggestions)}"
        else:
            return "Lo siento, no entiendo tu pregunta. Por favor, intenta ser más específico."
