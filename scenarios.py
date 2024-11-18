scenarios = {
    "Fácil": [
        {
            "question": "¿Qué es el phishing?",
            "options": [
                {"text": "Un intento de obtener información personal de forma fraudulenta.", "is_correct": True},
                {"text": "Un software que protege tus contraseñas.", "is_correct": False},
                {"text": "Un tipo de virus que infecta tu computadora.", "is_correct": False},
                {"text": "Un tipo de malware que roba tu identidad.", "is_correct": False}
            ]
        },
        {
            "question": "¿Cuál es la mejor manera de crear una contraseña segura?",
            "options": [
                {"text": "Usar solo letras y números fáciles de recordar.", "is_correct": False},
                {"text": "Usar una combinación de letras mayúsculas, minúsculas, números y símbolos.", "is_correct": True},
                {"text": "Usar tu nombre y fecha de nacimiento.", "is_correct": False},
                {"text": "Usar solo letras minúsculas.", "is_correct": False}
            ]
        },
        {
            "question": "¿Qué debes hacer si un amigo te envía un enlace sospechoso?",
            "options": [
                {"text": "Hacer clic en el enlace para ver qué es.", "is_correct": False},
                {"text": "Ignorar el enlace y pedirle a tu amigo más detalles.", "is_correct": True},
                {"text": "Reenviar el enlace a tus otros amigos.", "is_correct": False},
                {"text": "Descargar el archivo adjunto inmediatamente.", "is_correct": False}
            ]
        },
        {
            "question": "Si ves un correo de tu banco pidiéndote que actualices tus datos personales, ¿qué debes hacer?",
            "options": [
                {"text": "Ignorar el correo.", "is_correct": True},
                {"text": "Hacer clic en el enlace y proporcionar tus datos.", "is_correct": False},
                {"text": "Llamar a tu banco para confirmar si es legítimo.", "is_correct": False},
                {"text": "Reenviar el correo a un amigo para que lo vea.", "is_correct": False}
            ]
        },
        {
            "question": "¿Qué es un antivirus?",
            "options": [
                {"text": "Un programa que protege tu computadora de virus y otros software maliciosos.", "is_correct": True},
                {"text": "Un tipo de firewall.", "is_correct": False},
                {"text": "Un servicio que limpia tus archivos temporales.", "is_correct": False},
                {"text": "Un software para mejorar la velocidad de tu computadora.", "is_correct": False}
            ]
        }
    ],
    "Intermedio": [
        {
            "question": "¿Cuál es la mejor práctica para proteger tus cuentas en línea?",
            "options": [
                {"text": "Usar la misma contraseña para todas las cuentas.", "is_correct": False},
                {"text": "Activar la autenticación en dos pasos siempre que sea posible.", "is_correct": True},
                {"text": "Compartir tus contraseñas con amigos para que puedan ayudarte.", "is_correct": False},
                {"text": "Usar contraseñas fáciles de recordar.", "is_correct": False}
            ]
        },
        {
            "question": "¿Qué debes hacer si encuentras un archivo sospechoso en tu computadora?",
            "options": [
                {"text": "Abrirlo para ver qué contiene.", "is_correct": False},
                {"text": "Desinfectar el archivo con un software antivirus.", "is_correct": True},
                {"text": "Eliminarlo inmediatamente sin abrirlo.", "is_correct": False},
                {"text": "Ignorarlo si no está causando problemas.", "is_correct": False}
            ]
        },
        {
            "question": "Si recibes un mensaje en redes sociales de alguien que no conoces, ¿cómo debes proceder?",
            "options": [
                {"text": "Aceptar la solicitud de amistad para ver qué quiere.", "is_correct": False},
                {"text": "Ignorar el mensaje si parece sospechoso.", "is_correct": True},
                {"text": "Responder inmediatamente solicitando más detalles.", "is_correct": False},
                {"text": "Hacer clic en cualquier enlace que te envíen.", "is_correct": False}
            ]
        },
        {
            "question": "¿Qué es un firewall?",
            "options": [
                {"text": "Un software que ayuda a proteger tu computadora de accesos no autorizados.", "is_correct": True},
                {"text": "Un programa que limpia tus archivos temporales.", "is_correct": False},
                {"text": "Un antivirus que elimina virus.", "is_correct": False},
                {"text": "Un servicio que acelera tu conexión a Internet.", "is_correct": False}
            ]
        },
        {
            "question": "Si te piden tu información personal en un sitio web, ¿cómo puedes saber si es seguro?",
            "options": [
                {"text": "Verificar que la dirección web comience con 'https://' y tenga un candado en la barra de direcciones.", "is_correct": True},
                {"text": "Simplemente ingresar tus datos sin revisar la URL.", "is_correct": False},
                {"text": "Verificar la URL en Google.", "is_correct": False},
                {"text": "Ignorar los detalles y proceder.", "is_correct": False}
            ]
        }
    ],
    "Difícil": [
        {
            "question": "¿Qué es un ataque de 'Man in the middle' (MITM)?",
            "options": [
                {"text": "Un tipo de ataque que intercepta la comunicación entre dos partes para robar información.", "is_correct": True},
                {"text": "Un virus que se propaga a través de redes inalámbricas.", "is_correct": False},
                {"text": "Un tipo de malware que bloquea el acceso a tu sistema.", "is_correct": False},
                {"text": "Un tipo de troyano que se oculta en tus archivos personales.", "is_correct": False}
            ]
        },
        {
            "question": "¿Cuál es el principal objetivo de un ataque DDoS (Distributed Denial of Service)?",
            "options": [
                {"text": "Robar información personal de los usuarios.", "is_correct": False},
                {"text": "Destruir la infraestructura de la red.", "is_correct": False},
                {"text": "Sobrecargar un servidor para hacerlo inaccesible.", "is_correct": True},
                {"text": "Instalar malware en el servidor de destino.", "is_correct": False}
            ]
        },
        {
            "question": "¿Cómo puedes protegerte de un ataque de ransomware?",
            "options": [
                {"text": "Realizando copias de seguridad regulares de tus archivos.", "is_correct": True},
                {"text": "Usando contraseñas fuertes.", "is_correct": False},
                {"text": "Manteniendo actualizado el antivirus.", "is_correct": False},
                {"text": "Evitando hacer clic en enlaces de correos electrónicos sospechosos.", "is_correct": False}
            ]
        },
        {
            "question": "¿Qué es un 'zero-day exploit'?",
            "options": [
                {"text": "Un tipo de virus que solo puede infectar tu sistema durante el primer día de su lanzamiento.", "is_correct": False},
                {"text": "Un ataque que explota una vulnerabilidad de seguridad desconocida hasta ese momento.", "is_correct": True},
                {"text": "Un tipo de malware que se activa al abrir un archivo adjunto.", "is_correct": False},
                {"text": "Un software que protege tu sistema de ataques conocidos.", "is_correct": False}
            ]
        },
        {
            "question": "¿Qué es un 'pharming' en el contexto de ciberseguridad?",
            "options": [
                {"text": "Un tipo de ataque donde se redirige a los usuarios a un sitio web falso para robar su información.", "is_correct": True},
                {"text": "Un software para mejorar la privacidad en línea.", "is_correct": False},
                {"text": "Un virus que infecta tus archivos y los hace inaccesibles.", "is_correct": False},
                {"text": "Un programa para acelerar tu conexión a Internet.", "is_correct": False}
            ]
        },
        {
            "question": "¿?",
            "options": [
                {"text": ".", "is_correct": True},
                {"text": ".", "is_correct": False},
                {"text": ".", "is_correct": False},
                {"text": ".", "is_correct": False}
            ]
        }
    ]
}


