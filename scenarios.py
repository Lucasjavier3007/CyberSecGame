scenarios = {
    "Fácil": [
        {
            "question": "Recibes un correo que dice que has ganado un premio y te piden hacer clic en un enlace. ¿Qué haces?",
            "options": [
                {"text": "Hacer clic y seguir las instrucciones.", "is_correct": False},
                {"text": "No hacer clic y verificar la fuente primero.", "is_correct": True},
                {"text": "Responder al correo para obtener más información.", "is_correct": False}
            ],
            "feedback": [
                "¡Correcto! Siempre verifica la fuente antes de actuar.",
                "Error. Nunca hagas clic sin verificar la autenticidad del correo."
            ]
        },
        # Añadir más preguntas...
    ],
    "Intermedio": [
        {
            "question": "Recibes un mensaje de un amigo pidiéndote dinero urgente. ¿Qué haces?",
            "options": [
                {"text": "Transferir el dinero de inmediato.", "is_correct": False},
                {"text": "Llamar a tu amigo para confirmar la situación.", "is_correct": True},
                {"text": "Ignorar el mensaje completamente.", "is_correct": False}
            ],
            "feedback": [
                "¡Correcto! Siempre confirma con la persona antes de actuar.",
                "Error. Podría tratarse de una suplantación de identidad."
            ]
        },
        # Añadir más preguntas...
    ],
    "Avanzado": [
        {
            "question": "Descargas una aplicación gratuita desde un sitio desconocido. ¿Qué haces antes de instalarla?",
            "options": [
                {"text": "La instalas sin pensarlo, es gratuita.", "is_correct": False},
                {"text": "Verificas las opiniones y permisos requeridos.", "is_correct": True},
                {"text": "Desactivas el antivirus para evitar problemas.", "is_correct": False}
            ],
            "feedback": [
                "¡Correcto! Siempre revisa la fuente y los permisos antes de instalar algo.",
                "Error. Instalar software de fuentes desconocidas es riesgoso."
            ]
        },
        # Añadir más preguntas...
    ]
}

