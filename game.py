import tkinter as tk
import random
from scenarios import scenarios  # Asegúrate de que 'scenarios' esté bien definido
from tips import get_tip  # Asegúrate de que 'get_tip' esté bien definido

class CyberSecurityGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Ciberseguridad Avanzado")
        self.root.geometry("600x500")
        self.root.configure(bg="#1E1E2F")  # Fondo oscuro

        self.levels = list(scenarios.keys())
        self.current_level = None
        self.current_scenario = 0
        self.score = 0
        self.time_left = 50
        self.timer_id = None

        # Menú inicial
        self.show_level_selection()

    def show_level_selection(self):
        """Muestra el menú de selección de nivel."""
        self.clear_screen()

        title_label = tk.Label(
            self.root,
            text="Seleccione el nivel del juego",
            font=("Helvetica", 18, "bold"),
            fg="#FFD700", bg="#1E1E2F"
        )
        title_label.pack(pady=20)

        for level in self.levels:
            btn = tk.Button(
                self.root,
                text=level,
                font=("Arial", 14),
                bg="#4CAF50",
                fg="white",
                command=lambda level=level: self.start_game(level)
            )
            btn.pack(pady=10)

    def start_game(self, level):
        """Inicia el juego con el nivel seleccionado."""
        self.current_level = level
        self.current_scenario = 0
        self.score = 0
        self.time_left = 30
        self.show_scenario()
        self.start_timer()

    def show_scenario(self):
        """Muestra una pregunta con opciones aleatorias."""
        self.clear_screen()

        level = self.current_level
        scenario = scenarios[level][self.current_scenario]

        # Mostrar la pregunta
        self.question_label = tk.Label(
            self.root,
            text=scenario["question"],
            wraplength=500,
            font=("Arial", 14),
            fg="white", bg="#1E1E2F"
        )
        self.question_label.pack(pady=20)

        self.option_buttons = []
        options = scenario["options"]
        random.shuffle(options)  # Mezclar opciones aleatoriamente

        # Crear botones de opción
        for option in options:
            btn = tk.Button(
                self.root,
                text=option["text"],
                font=("Arial", 12),
                bg="#FF5722",  # Color de fondo más visible
                fg="black",  # Color del texto negro
                activebackground="#FF7043",  # Color cuando el botón está presionado
                command=lambda opt=option: self.check_answer(opt)
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Mostrar el temporizador
        self.timer_label = tk.Label(
            self.root,
            text=f"Tiempo restante: {self.time_left}s",
            font=("Arial", 12),
            fg="white", bg="#1E1E2F"
        )
        self.timer_label.pack(pady=10)

    def check_answer(self, option):
        """Verifica la respuesta y muestra feedback."""
        is_correct = option["is_correct"]
        feedback_text = "¡Correcto!" if is_correct else "Incorrecto."

        feedback_label = tk.Label(
            self.root,
            text=feedback_text,
            font=("Arial", 12),
            fg="#FFD700" if is_correct else "#FF4500",
            bg="#1E1E2F"
        )
        feedback_label.pack(pady=10)

        # Actualizar puntaje solo si la respuesta es correcta
        if is_correct:
            self.score += 10

        # Mostrar consejo
        self.show_tip()

        # Deshabilitar botones y esperar para avanzar
        for btn in self.option_buttons:
            btn.config(state="disabled")

        # Avanzar al siguiente escenario después de un tiempo
        self.root.after(2000, self.next_scenario)

    def show_tip(self):
        """Muestra un consejo basado en el escenario actual."""
        tip_label = tk.Label(
            self.root,
            text=f"💡 Consejo: {get_tip(self.current_scenario + 1)}",
            font=("Arial", 12),
            fg="#00BFFF",
            bg="#1E1E2F"
        )
        tip_label.pack(pady=10)

    def next_scenario(self):
        """Avanza al siguiente escenario o termina el juego."""
        self.current_scenario += 1
        level = self.current_level

        if self.current_scenario < len(scenarios[level]):
            self.show_scenario()
        else:
            self.end_game()

    def end_game(self):
        """Termina el juego y muestra el puntaje final."""
        self.stop_timer()

        # Limpiar la pantalla
        self.clear_screen()

        # Mensaje final
        result_text = f"Juego terminado. Obtuviste {self.score} puntos."
        if self.score >= 50:
            result_text += "\n¡Excelente trabajo! Estás muy preparado."
        elif self.score >= 30:
            result_text += "\nBien hecho, pero aún hay que mejorar."
        else:
            result_text += "\nSigue practicando para mejorar."

        end_label = tk.Label(
            self.root,
            text=result_text,
            font=("Arial", 14),
            fg="white", bg="#1E1E2F"
        )
        end_label.pack(pady=20)

        # Botón para reiniciar o volver al menú
        restart_btn = tk.Button(
            self.root,
            text="Volver al menú",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=self.show_level_selection
        )
        restart_btn.pack(pady=20)

    def clear_screen(self):
        """Limpia la pantalla de la interfaz gráfica."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_timer(self):
        """Inicia el temporizador."""
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Tiempo restante: {self.time_left}s")
            self.timer_id = self.root.after(1000, self.start_timer)
        else:
            self.end_game()

    def stop_timer(self):
        """Detiene el temporizador."""
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None


if __name__ == "__main__":
    root = tk.Tk()
    app = CyberSecurityGame(root)
    root.mainloop()
