import sys
from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка интерфейса из файла .ui
        uic.loadUi('ui/Calc.ui', self)

        # Получение доступа к элементам интерфейса
        self.inputField = self.findChild(QtWidgets.QTextEdit, 'InputField')

        # Настройка обработчиков событий для кнопок
        self.setupConnections()

    def create_number_handler(self, number):
        def handler():
            self.append_number(str(number))

        return handler

    def setupConnections(self):
        self.findChild(QtWidgets.QPushButton, 'Button_Clear').clicked.connect(self.clear)
        self.findChild(QtWidgets.QPushButton, 'Button_PlusMinus').clicked.connect(self.plusMinus)
        self.findChild(QtWidgets.QPushButton, 'Button_Dot').clicked.connect(self.dot)
        self.findChild(QtWidgets.QPushButton, 'Button_Rem').clicked.connect(self.rem)

        for i in range(10):
            button_name = f'Button_{i}'
            handler = self.create_number_handler(i)
            self.findChild(QtWidgets.QPushButton, button_name).clicked.connect(handler)

        self.findChild(QtWidgets.QPushButton, 'Button_Plus').clicked.connect(lambda: self.append_operator('+'))
        self.findChild(QtWidgets.QPushButton, 'Button_Minus').clicked.connect(lambda: self.append_operator('-'))
        self.findChild(QtWidgets.QPushButton, 'Button_Multy').clicked.connect(lambda: self.append_operator('*'))
        self.findChild(QtWidgets.QPushButton, 'Button_Div').clicked.connect(lambda: self.append_operator('/'))
        self.findChild(QtWidgets.QPushButton, 'Button_Result').clicked.connect(self.calculate_result)

    def append_number(self, number):
        self.inputField.insertPlainText(number)

    def append_operator(self, operator):
        self.inputField.insertPlainText(operator)

    def clear(self):
        self.inputField.clear()

    def plusMinus(self):
        current_text = self.inputField.toPlainText()
        if current_text.startswith('-'):
            self.inputField.setPlainText(current_text[1:])
        else:
            self.inputField.setPlainText('-' + current_text)

    def rem(self):
        current_text = self.inputField.toPlainText()
        # Удаление последнего символа
        new_text = current_text[:-1]
        self.inputField.setPlainText(new_text)

    def dot(self):
        self.inputField.insertPlainText('.')

    def calculate_result(self):
        try:
            result = eval(self.inputField.toPlainText())
            self.inputField.setPlainText(str(result))
        except Exception as e:
            self.inputField.setPlainText("Error")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
