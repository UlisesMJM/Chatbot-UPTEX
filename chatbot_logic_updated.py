from fuzzywuzzy import process

# Datos simulados para las ofertas educativas y otras preguntas frecuentes
educational_offers = {
    "Ingeniería en Sistemas Computacionales": "La Ingeniería en Sistemas Computacionales se enfoca en la tecnología de la información y la computación.",
    "Licenciatura en Administración": "La Licenciatura en Administración prepara a los estudiantes para liderar y gestionar organizaciones de diversos tipos.",
    "Ingeniería Industrial": "La Ingeniería Industrial optimiza procesos y sistemas en diferentes industrias.",
    "Perfil de egreso de Ingeniería en Sistemas Computacionales": "El perfil de egreso de la Ingeniería en Sistemas Computacionales incluye habilidades en desarrollo de software, administración de redes y bases de datos, y gestión de proyectos tecnológicos.",
    "Áreas de especialización de Licenciatura en Administración": "La Licenciatura en Administración ofrece especialización en áreas como finanzas, recursos humanos, y marketing.",
    "Habilidades desarrolladas en Ingeniería Industrial": "La Ingeniería Industrial desarrolla habilidades en optimización de procesos, análisis de sistemas, y gestión de calidad.",
    "Requisitos de ingreso a la UPTEX": "Los requisitos para ingresar a la UPTEX incluyen completar el nivel medio superior, presentar un examen de admisión, y cumplir con la documentación requerida.",
    "Proceso de admisión en la UPTEX": "El proceso de admisión en la Universidad Politécnica de Texcoco incluye registro en línea, presentación de un examen, y entrega de documentos.",
    "Oportunidades de empleo para egresados de Ingeniería en Sistemas Computacionales": "Los egresados de Ingeniería en Sistemas Computacionales tienen oportunidades de empleo en desarrollo de software, administración de sistemas, y consultoría tecnológica.",
    "Duración de la Licenciatura en Administración": "La Licenciatura en Administración tiene una duración de 8 semestres, equivalente a 4 años.",
    "Prácticas profesionales en Ingeniería Industrial": "Sí, la Ingeniería Industrial incluye prácticas profesionales como parte del plan de estudios para aplicar los conocimientos adquiridos en el campo laboral.",
    "Instalaciones de la UPTEX": "La UPTEX cuenta con laboratorios de cómputo, talleres, biblioteca, y áreas deportivas, entre otras instalaciones.",
    "Programas de intercambio en la UPTEX": "Sí, la Universidad Politécnica de Texcoco ofrece programas de intercambio con universidades nacionales e internacionales.",
    "Actividades extracurriculares en la UPTEX": "La UPTEX ofrece actividades extracurriculares como deportes, grupos culturales, y talleres de desarrollo personal.",
    "Costo de la matrícula en la UPTEX": "El costo de la matrícula en la UPTEX varía según el programa de estudios y el semestre, pero es accesible para los estudiantes.",
    "Becas en la UPTEX": "Sí, existen diversas becas disponibles para los estudiantes de la UPTEX, incluyendo becas académicas, deportivas, y de apoyo económico.",
    "Servicios de apoyo académico en la UPTEX": "La universidad ofrece servicios de apoyo académico como tutorías, asesorías, y acceso a recursos educativos en línea.",
    "Vida estudiantil en la UPTEX": "La vida estudiantil en la Universidad Politécnica de Texcoco es activa y diversa, con oportunidades para participar en eventos, organizaciones estudiantiles, y actividades recreativas.",
    "Documentos necesarios para inscribirse en la UPTEX": "Los documentos necesarios para inscribirse en una carrera en la UPTEX incluyen certificado de preparatoria, acta de nacimiento, CURP, y comprobante de domicilio.",
    "Horario de clases en la UPTEX": "El horario de clases en la UPTEX puede variar según la carrera y el semestre, pero generalmente se ofrece en horarios matutinos y vespertinos.",
    # Agrega más respuestas según sea necesario
}

def get_offer_details(query):
    # Usa fuzzy matching para encontrar la mejor coincidencia
    best_match = process.extractOne(query, educational_offers.keys())
    if best_match[1] > 70:  # Si la coincidencia es mayor al 70%
        return educational_offers[best_match[0]]
    else:
        return "Lo siento, no pude encontrar información sobre esa oferta educativa."

# Función principal del chatbot
def chatbot_response(user_input):
    response = get_offer_details(user_input)
    return response



import logging

# Configurar el registro de preguntas
logging.basicConfig(filename='chatbot_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_question(user_input, response):
    logging.info(f'Pregunta: {user_input} | Respuesta: {response}')

def chatbot_response(user_input):
    # Simulación de la respuesta del chatbot
    best_match = process.extractOne(user_input, educational_offers.keys())
    if best_match:
        response = educational_offers[best_match[0]]
    else:
        response = "Lo siento, no entiendo tu pregunta. Por favor, intenta de nuevo."
    # Registrar la pregunta y respuesta
    log_question(user_input, response)
    return response
