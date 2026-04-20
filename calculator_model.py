class CalculatorModel:
    def __init__(self):
        self.expression = ""
        self.answer = "0"
        self.dark_mode = False

    def append(self, value):
        self.expression += value

    def clear(self):
        self.expression = ""

    def delete_last(self):
        self.expression = self.expression[:-1]

    def toggle_mode(self):
        self.dark_mode = not self.dark_mode

    def calculate(self):
        if not self.expression.strip():
            self.answer = "0"
            return
        allowed = set("0123456789+-*/.() ")
        if any(ch not in allowed for ch in self.expression):
            self.answer = "Error"
            return
        try:
            result = eval(self.expression, {"__builtins__": {}}, {})
            self.answer = str(float(result))
            self.expression = self.answer
        except Exception:
            self.answer = "Error"
