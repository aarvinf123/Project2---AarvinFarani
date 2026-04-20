import sys
from PyQt6.QtWidgets import QApplication
from models.calculator_model import CalculatorModel
from views.calculator_view import CalculatorView
from controllers.calculator_controller import CalculatorController

def main():
    app = QApplication(sys.argv)
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
