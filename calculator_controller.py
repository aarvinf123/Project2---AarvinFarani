class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.parentheses_open = True
        self.connect_buttons()
        self.update_view()

    def connect_buttons(self):
        self.view.clear_button.clicked.connect(self.clear)
        self.view.mode_button.clicked.connect(self.toggle_mode)
        self.view.delete_button.clicked.connect(self.delete_last)
        self.view.divide_button.clicked.connect(lambda: self.add_text("/"))

        self.view.seven_button.clicked.connect(lambda: self.add_text("7"))
        self.view.eight_button.clicked.connect(lambda: self.add_text("8"))
        self.view.nine_button.clicked.connect(lambda: self.add_text("9"))
        self.view.multiply_button.clicked.connect(lambda: self.add_text("*"))

        self.view.four_button.clicked.connect(lambda: self.add_text("4"))
        self.view.five_button.clicked.connect(lambda: self.add_text("5"))
        self.view.six_button.clicked.connect(lambda: self.add_text("6"))
        self.view.minus_button.clicked.connect(lambda: self.add_text("-"))

        self.view.one_button.clicked.connect(lambda: self.add_text("1"))
        self.view.two_button.clicked.connect(lambda: self.add_text("2"))
        self.view.three_button.clicked.connect(lambda: self.add_text("3"))
        self.view.plus_button.clicked.connect(lambda: self.add_text("+"))

        self.view.parentheses_button.clicked.connect(self.add_parenthesis)
        self.view.zero_button.clicked.connect(lambda: self.add_text("0"))
        self.view.decimal_button.clicked.connect(lambda: self.add_text("."))
        self.view.equals_button.clicked.connect(self.calculate)

    def add_text(self, value):
        self.model.append(value)
        self.update_view()

    def add_parenthesis(self):
        if self.parentheses_open:
            self.model.append("(")
        else:
            self.model.append(")")
        self.parentheses_open = not self.parentheses_open
        self.update_view()

    def clear(self):
        self.model.clear()
        self.parentheses_open = True
        self.update_view()

    def delete_last(self):
        self.model.delete_last()
        self.update_view()

    def toggle_mode(self):
        self.model.toggle_mode()
        self.update_view()

    def calculate(self):
        self.model.calculate()
        self.update_view()

    def update_view(self):
        self.view.expression_label.setText(self.model.expression)
        self.view.answer_label.setText(f"Ans={self.model.answer}")
        if self.model.dark_mode:
            self.view.apply_dark_mode()
        else:
            self.view.apply_light_mode()
