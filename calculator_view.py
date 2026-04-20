from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QFrame

class CalculatorView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CalculatorProject")
        self.setFixedSize(420, 620)

        self.expression_label = QLabel("")
        self.expression_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.expression_label.setFixedHeight(70)

        self.answer_label = QLabel("Ans=0")
        self.answer_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.answer_label.setFixedHeight(70)

        top_line = QFrame()
        top_line.setFrameShape(QFrame.Shape.HLine)

        self.clear_button = QPushButton("Clear")
        self.mode_button = QPushButton("Mode")
        self.delete_button = QPushButton("Del")
        self.divide_button = QPushButton("/")

        self.seven_button = QPushButton("7")
        self.eight_button = QPushButton("8")
        self.nine_button = QPushButton("9")
        self.multiply_button = QPushButton("*")

        self.four_button = QPushButton("4")
        self.five_button = QPushButton("5")
        self.six_button = QPushButton("6")
        self.minus_button = QPushButton("-")

        self.one_button = QPushButton("1")
        self.two_button = QPushButton("2")
        self.three_button = QPushButton("3")
        self.plus_button = QPushButton("+")

        self.parentheses_button = QPushButton("( )")
        self.zero_button = QPushButton("0")
        self.decimal_button = QPushButton(".")
        self.equals_button = QPushButton("=")

        grid = QGridLayout()
        grid.setSpacing(8)

        buttons = [
            (self.clear_button, 0, 0), (self.mode_button, 0, 1), (self.delete_button, 0, 2), (self.divide_button, 0, 3),
            (self.seven_button, 1, 0), (self.eight_button, 1, 1), (self.nine_button, 1, 2), (self.multiply_button, 1, 3),
            (self.four_button, 2, 0), (self.five_button, 2, 1), (self.six_button, 2, 2), (self.minus_button, 2, 3),
            (self.one_button, 3, 0), (self.two_button, 3, 1), (self.three_button, 3, 2), (self.plus_button, 3, 3),
            (self.parentheses_button, 4, 0), (self.zero_button, 4, 1), (self.decimal_button, 4, 2), (self.equals_button, 4, 3),
        ]

        for button, row, col in buttons:
            button.setMinimumHeight(75)
            grid.addWidget(button, row, col)

        layout = QVBoxLayout()
        layout.addWidget(self.expression_label)
        layout.addWidget(self.answer_label)
        layout.addWidget(top_line)
        layout.addLayout(grid)
        self.setLayout(layout)

        self.apply_light_mode()

    def apply_dark_mode(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1f1f1f;
                color: white;
                font-size: 18px;
            }
            QLabel {
                background-color: #2a2a2a;
                border: 1px solid #444444;
                padding: 10px;
                font-size: 28px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #333333;
                color: white;
                border: 1px solid #555555;
                border-radius: 8px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #444444;
            }
        """)

    def apply_light_mode(self):
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                color: black;
                font-size: 18px;
            }
            QLabel {
                background-color: white;
                border: 1px solid #cfcfcf;
                padding: 10px;
                font-size: 28px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #f6f6f6;
                color: black;
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #e6e6e6;
            }
        """)
