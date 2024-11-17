def get_tip(scenario_index):
    tips = {
        1: "Consejo: Siempre verifica la autenticidad de los correos antes de hacer clic en los enlaces.",
        2: "Consejo: Los ataques de phishing pueden parecer urgentes, pero siempre debes confirmar antes de transferir dinero.",
        3: "Consejo: Revisa los permisos y opiniones de las aplicaciones antes de instalar, especialmente si vienen de fuentes no confiables.",
        # Agregar más consejos para más escenarios...
    }
    return tips.get(scenario_index, "Consejo general: No confíes en todo lo que ves en línea.")
