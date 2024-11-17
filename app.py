from flask import Flask, render_template
import random  # Para generar preguntas aleatorias

app = Flask(__name__)

@app.route("/")
def home():
    # Aquí iría la lógica de tu juego
    # Por ejemplo, una pregunta aleatoria
    question = "¿Qué harías si recibes un email desconocido pidiendo información personal?"
    options = ["Responder", "Ignorar", "Hacer clic en el enlace"]
    random.shuffle(options)
    return render_template("index.html", question=question, options=options)

if __name__ == "__main__":
    app.run(debug=True)
