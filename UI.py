import tkinter as tk
from tkinter import messagebox, ttk
from data import TREE_DATA, RECOMMENDATIONS, CATEGORY_ADVICE
from models import build_node, count_leaves
from logic import get_all_leaves, calculate_percentage, classify_level, find_highest_category
from db import save_record, get_all_records, check_student_exists

class StressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Alerta Temprana - Universidad de Cundinamarca")
        self.root.geometry("850x700")
        self.root.config(bg="#0B4619")  
        self.root.minsize(750, 620)

        self.student_name = ""
        self.semester = 1
        self.root_node = build_node(TREE_DATA)
        self.leaves = get_all_leaves(self.root_node)
        self.current_question_index = 0

       
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
       
        self.main_frame = tk.Frame(self.root, bg="#0B4619")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)

        self.show_welcome_screen()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_frame()


        header_lbl = tk.Label(
            self.main_frame, 
            text="UNIVERSIDAD DE CUNDINAMARCA", 
            font=("Arial", 16, "bold"), 
            bg="#0B4619", 
            fg="#FFFFFF"
        )
        header_lbl.pack(pady=(5, 5))

        sub_lbl = tk.Label(
            self.main_frame, 
            text="Sistema de Alerta Temprana - Permanencia Estudiantil", 
            font=("Arial", 12, "italic"), 
            bg="#0B4619", 
            fg="#E2E8F0"
        )
        sub_lbl.pack(pady=(0, 25))

     
        card = tk.Frame(self.main_frame, bg="#FFFFFF", padx=40, pady=35)
        card.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        title_card = tk.Label(card, text="Registro del Estudiante", font=("Arial", 18, "bold"), bg="#FFFFFF", fg="#0A3611")
        title_card.pack(pady=(0, 25))

        form_inner = tk.Frame(card, bg="#FFFFFF")
        form_inner.pack(anchor="center")

        tk.Label(form_inner, text="¿Cómo te llamas?", font=("Arial", 13, "bold"), bg="#FFFFFF", fg="#1E293B").pack(anchor="w", pady=(0, 5))
        self.name_entry = tk.Entry(form_inner, font=("Arial", 13), bd=2, relief="groove", width=32)
        self.name_entry.pack(pady=(0, 20), ipady=6)

        tk.Label(form_inner, text="¿En qué semestre vas? (1 - 12):", font=("Arial", 13, "bold"), bg="#FFFFFF", fg="#1E293B").pack(anchor="w", pady=(0, 5))
        self.semester_spin = ttk.Spinbox(form_inner, from_=1, to=12, font=("Arial", 13), width=15)
        self.semester_spin.set(1)
        self.semester_spin.pack(anchor="w", pady=(0, 30))

        btn_frame = tk.Frame(card, bg="#FFFFFF")
        btn_frame.pack(pady=(10, 0))

        start_btn = tk.Button(
            btn_frame, 
            text="Comenzar Test", 
            font=("Arial", 12, "bold"), 
            bg="#0A3611", 
            fg="#FFFFFF", 
            activebackground="#15803D",
            activeforeground="#FFFFFF",
            relief="flat", 
            padx=25, 
            pady=12,
            command=self.validate_and_start
        )
        start_btn.pack(side=tk.LEFT, padx=10)

        history_btn = tk.Button(
            btn_frame, 
            text="Ver Historial (BD)", 
            font=("Arial", 12, "bold"), 
            bg="#0A3611", 
            fg="#FFFFFF", 
            activebackground="#334155",
            activeforeground="#FFFFFF",
            relief="flat", 
            padx=20, 
            pady=12,
            command=self.show_history_screen
        )
        history_btn.pack(side=tk.LEFT, padx=10)

    def validate_and_start(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Por favor ingresa tu nombre completo.")
            return
        
        if check_student_exists(name):
            messagebox.showwarning(
                "Nombre Existente", 
                f"El nombre '{name}' ya se encuentra registrado en el sistema.\nPor favor, modifícalo o agrega un apellido/identificador para continuar."
            )
            return

        self.student_name = name
        try:
            self.semester = int(self.semester_spin.get())
        except ValueError:
            self.semester = 1

        self.root_node = build_node(TREE_DATA)
        self.leaves = get_all_leaves(self.root_node)
        self.current_question_index = 0
        self.show_question_screen()

    def show_question_screen(self):
        self.clear_frame()

        total = len(self.leaves)
        current = self.current_question_index + 1

        progress_frame = tk.Frame(self.main_frame, bg="#0B4619")
        progress_frame.pack(fill=tk.X, pady=(0, 10))

        prog_lbl = tk.Label(progress_frame, text=f"Pregunta {current} de {total}", font=("Arial", 12, "bold"), bg="#0B4619", fg="#FFFFFF")
        prog_lbl.pack(side=tk.LEFT)

        progress_bar = ttk.Progressbar(self.main_frame, orient="horizontal", length=100, mode="determinate")
        progress_bar.pack(fill=tk.X, pady=(0, 15))
        progress_bar["value"] = (current / total) * 100

        card = tk.Frame(self.main_frame, bg="#FFFFFF", padx=40, pady=30)
        card.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        node = self.leaves[self.current_question_index]
        
        q_lbl = tk.Label(
            card, 
            text=node.label, 
            font=("Arial", 15, "bold"), 
            bg="#FFFFFF", 
            fg="#0A3611", 
            wraplength=650, 
            justify="center"
        )
        q_lbl.pack(pady=(15, 20))

        scale_desc = (
            "Escala de frecuencia:\n"
            "1 = Nunca  |  2 = Casi nunca  |  3 = A veces  |  4 = Casi siempre  |  5 = Siempre"
        )
        tk.Label(
            card, 
            text=scale_desc, 
            font=("Arial", 11, "italic"), 
            bg="#FFFFFF", 
            fg="#334155",
            justify="center"
        ).pack(pady=(0, 25))

        options_container = tk.Frame(card, bg="#FFFFFF")
        options_container.pack(anchor="center")

        options = [
            (1, "1 - Nunca"),
            (2, "2 - Casi nunca"),
            (3, "3 - A veces"),
            (4, "4 - Casi siempre"),
            (5, "5 - Siempre")
        ]

        for val, text in options:
            btn = tk.Button(
                options_container, 
                text=text, 
                font=("Arial", 12, "bold"), 
                bg="#F1F5F9", 
                fg="#0F172A", 
                activebackground="#16A34A",
                activeforeground="#FFFFFF",
                anchor="center", 
                width=35,
                pady=10,
                relief="flat",
                command=lambda v=val: self.record_answer(v)
            )
            btn.pack(pady=6)

    def record_answer(self, value):
        node = self.leaves[self.current_question_index]
        node.answer = value
        node.score = (6 - value) if node.reverse else value

        self.current_question_index += 1
        if self.current_question_index < len(self.leaves):
            self.show_question_screen()
        else:
            self.show_results_screen()

    def show_results_screen(self):
        self.clear_frame()

        overall_percentage = calculate_percentage(self.root_node)
        overall_level = classify_level(overall_percentage)
        highest = find_highest_category(self.root_node.children)
        highest_percentage = calculate_percentage(highest)

        save_record(self.student_name, self.semester, overall_percentage, overall_level, highest.label)

        card = tk.Frame(self.main_frame, bg="#FFFFFF", padx=35, pady=25)
        card.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        tk.Label(card, text=f"RESULTADOS - {self.student_name.upper()}", font=("Arial", 16, "bold"), bg="#FFFFFF", fg="#0A3611").pack(pady=(0, 15))

        cat_frame = tk.Frame(card, bg="#F8FAFC", padx=15, pady=12)
        cat_frame.pack(fill=tk.X, pady=5)

        for child in self.root_node.children:
            pct = calculate_percentage(child)
            lvl = classify_level(pct)
            row_text = f"• {child.label}: {pct}% ({lvl})"
            tk.Label(cat_frame, text=row_text, font=("Arial", 11, "bold"), bg="#F8FAFC", fg="#1E293B").pack(anchor="w", pady=3)

        total_text = f"ESTRÉS TOTAL: {overall_percentage}% — {overall_level.upper()}"
        tk.Label(card, text=total_text, font=("Arial", 13, "bold"), bg="#FFFFFF", fg="#16A34A").pack(pady=(15, 5))

        rec_text = RECOMMENDATIONS[overall_level]
        tk.Label(card, text=rec_text, font=("Arial", 11), bg="#FFFFFF", fg="#334155", wraplength=650, justify="center").pack(pady=(0, 10))

        advice_text = f"Aspecto que más pesa: {highest.label} ({highest_percentage}%)\nConsejo: {CATEGORY_ADVICE[highest.name]}"
        tk.Label(card, text=advice_text, font=("Arial", 11, "italic"), bg="#FFFFFF", fg="#0A3611", wraplength=650, justify="center").pack(pady=(5, 20))

        nav_frame = tk.Frame(card, bg="#FFFFFF")
        nav_frame.pack(pady=10)

        tk.Button(
            nav_frame, text="Realizar de nuevo", font=("Arial", 11, "bold"), 
            bg="#16A34A", fg="#FFFFFF", relief="flat", padx=20, pady=10,
            command=self.show_welcome_screen
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(
            nav_frame, text="Ver Historial Global", font=("Arial", 11), 
            bg="#475569", fg="white", relief="flat", padx=20, pady=10,
            command=self.show_history_screen
        ).pack(side=tk.LEFT, padx=10)

    def show_history_screen(self):
        self.clear_frame()

        tk.Label(
            self.main_frame, text="REGISTROS DE LA BASE DE DATOS (SQLite)", 
            font=("Arial", 15, "bold"), bg="#0B4619", fg="#FFFFFF"
        ).pack(pady=(5, 15))

        card = tk.Frame(self.main_frame, bg="#FFFFFF", padx=20, pady=20)
        card.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        columns = ("Nombre", "Semestre", "Fecha", "Porcentaje", "Nivel", "Área Crítica")
        tree = ttk.Treeview(card, columns=columns, show="headings", height=12)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=110, anchor="center")

        tree.column("Nombre", width=140)
        tree.column("Fecha", width=140)

        records = get_all_records()
        for row in records:
            formatted_row = (row[0], row[1], row[2], f"{row[3]}%", row[4], row[5])
            tree.insert("", tk.END, values=formatted_row)

        tree.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

        tk.Button(
            card, text="Volver al Inicio", font=("Arial", 11, "bold"), 
            bg="#0B4619", fg="#FFFFFF", relief="flat", padx=25, pady=10,
            command=self.show_welcome_screen
        ).pack(anchor="center")


if __name__ == "__main__":
    root = tk.Tk()
    app = StressApp(root)
    root.mainloop()