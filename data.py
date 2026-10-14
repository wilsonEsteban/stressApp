TREE_DATA = {
    "name": "stress",
    "label": "Estres total",
    "children": [
        {
            "name": "emotional",
            "label": "Emocional",
            "children": [
                {"name": "q1", "text": "Me siento triste, desanimado o sin ganas de hacer las cosas", "reverse": False},
                {"name": "q2", "text": "Me siento ansioso o preocupado la mayor parte del tiempo", "reverse": False},
                {"name": "q3", "text": "Me cuesta dormir o descansar bien por pensar en la universidad", "reverse": False},
                {"name": "q4", "text": "Me siento tranquilo y con buen estado de animo", "reverse": True},
                {"name": "q5", "text": "He pensado en abandonar mis estudios", "reverse": False},
            ],
        },
        {
            "name": "economic",
            "label": "Economico",
            "children": [
                {"name": "q6", "text": "Me preocupa no poder pagar la matricula, el transporte o la alimentacion", "reverse": False},
                {"name": "q7", "text": "Tengo que trabajar y eso me quita tiempo para estudiar", "reverse": False},
                {"name": "q8", "text": "Mis ingresos o los de mi familia alcanzan para cubrir mis gastos basicos", "reverse": True},
                {"name": "q9", "text": "Conozco y he usado apoyos economicos como exoneraciones de matricula", "reverse": True},
            ],
        },
        {
            "name": "academic",
            "label": "Academico",
            "children": [
                {"name": "q10", "text": "Siento que tengo demasiada carga academica (trabajos, parciales, proyectos)", "reverse": False},
                {"name": "q11", "text": "Me preocupa reprobar materias o perder mi promedio", "reverse": False},
                {"name": "q12", "text": "Dudo de haber elegido la carrera correcta", "reverse": False},
                {"name": "q13", "text": "Entiendo los temas y puedo seguir el ritmo de mis clases", "reverse": True},
            ],
        },
        {
            "name": "social",
            "label": "Social e institucional",
            "children": [
                {"name": "q14", "text": "Siento que tengo apoyo de mi familia o mis amigos", "reverse": True},
                {"name": "q15", "text": "Me siento solo o aislado en la universidad", "reverse": False},
                {"name": "q16", "text": "No se a donde acudir cuando tengo un problema en la universidad", "reverse": False},
            ],
        },
    ],
}

RECOMMENDATIONS = {
    "Bajo": "Tu nivel de estres es bajo. Mantén tus habitos y no dudes en buscar apoyo si algo cambia.",
    "Moderado": "Hay senales de estres acumulado. Conviene organizar tu tiempo y hablar con alguien de confianza.",
    "Alto": "Tu estres es alto. Te recomendamos acercarte a Bienestar Universitario para recibir acompanamiento.",
    "Muy alto": "Tu estres es muy alto. Busca apoyo de Bienestar Universitario lo antes posible y habla con alguien cercano.",
}

CATEGORY_ADVICE = {
    "emotional": "Prioriza descanso, pausas activas y hablar con Bienestar Universitario.",
    "economic": "Consulta exoneraciones de matricula y apoyos economicos de la universidad.",
    "academic": "Organiza un horario de estudio y busca tutorias o a tus docentes.",
    "social": "Acercate a grupos estudiantiles y a los servicios de acompanamiento.",
}