import math
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox
from PyQt6 import uic


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculator.ui", self)

        # Connect buttons, including the square root and power buttons
        self.pushButtonpoint.clicked.connect(lambda: self.on_button_click('.'))
        self.pushButton0.clicked.connect(lambda: self.on_button_click('0'))
        self.pushButton1.clicked.connect(lambda: self.on_button_click('1'))
        self.pushButton2.clicked.connect(lambda: self.on_button_click('2'))
        self.pushButton3.clicked.connect(lambda: self.on_button_click('3'))
        self.pushButton4.clicked.connect(lambda: self.on_button_click('4'))
        self.pushButton5.clicked.connect(lambda: self.on_button_click('5'))
        self.pushButton6.clicked.connect(lambda: self.on_button_click('6'))
        self.pushButton7.clicked.connect(lambda: self.on_button_click('7'))
        self.pushButton8.clicked.connect(lambda: self.on_button_click('8'))
        self.pushButton9.clicked.connect(lambda: self.on_button_click('9'))

        self.add.clicked.connect(lambda: self.on_button_click('+'))
        self.subtract.clicked.connect(lambda: self.on_button_click('-'))
        self.multiply.clicked.connect(lambda: self.on_button_click('*'))
        self.backspace.clicked.connect(self.on_backspace_click)
        self.squareroot.clicked.connect(self.on_sqrt_click)
        self.exponential.clicked.connect(lambda: self.on_button_click('**'))
        self.percentage.clicked.connect(lambda: self.on_button_click('%'))
        self.equals.clicked.connect(self.evaluate_expression)
        self.clear.clicked.connect(self.clear_display)
        self.converter.clicked.connect(self.gotoconverter)
        self.back.clicked.connect(self.goback)
        # Currency conversion widgets
        self.convertbutton.clicked.connect(self.convert_currency)

        # Populate the currency dropdowns

    def on_sqrt_click(self):
        current_expression = self.display.text()
        try:
            # Calculate square root of the current number/expression
            result = math.sqrt(float(current_expression))
            self.display.setText(str(result))
        except ValueError:
            self.display.setText("Error")  # Handle invalid inputs

    def clear_display(self):
        self.display.setText('0')

    def on_backspace_click(self):
        current_text = self.display.text()

        # Check if there is any text to delete
        if current_text != '0':
            # Remove the last character from the display
            self.display.setText(current_text[:-1])

    def evaluate_expression(self):
        try:
            expression = self.display.text()
            # Evaluate the expression using eval, allowing for sqrt, pow, etc.
            result = eval(expression, {'sqrt': math.sqrt, 'pow': math.pow, 'abs': abs})
            self.display.setText(str(result))
        except Exception:
            self.display.setText('Error')

    def on_button_click(self, text):
        # Get the current text from the QLabel
        current_text = self.display.text()

        # Avoid starting the display with a zero
        if current_text == '0':
            self.display.setText(text)
        else:
            # Append the text of the button to the display
            self.display.setText(current_text + text)

    def gotoconverter(self):
        self.stackedWidget.setCurrentIndex(1)

    def goback(self):
        self.stackedWidget.setCurrentIndex(0)

    def convert_currency(self):
        from_currency = self.comboBoxfrom.currentText()
        to_currency = self.comboBoxto.currentText()
        amount = float(self.lineEdit.text())  # Assuming display has the amount to convert

        try:
            # Fetch exchange rate from an API (replace with your API key and proper URL)
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
            rates = response.json()['rates']

            # Convert the amount
            converted_amount = amount * rates[to_currency]
            self.result.setText(str(converted_amount))
        except Exception as e:
            self.result.setText(f"Error: {str(e)}")


# Run the application
app = QApplication([])
window = CalculatorApp()
window.show()
app.exec()
