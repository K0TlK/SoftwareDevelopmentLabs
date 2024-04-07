import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.total_expense = 0  # Общие расходы на топливо
        self.initializeUI()

    def initializeUI(self):
        """Инициализация пользовательского интерфейса главного окна."""
        self.setWindowTitle("Трекер расходов на топливо")
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()  # Центральный виджет для содержания всех элементов
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Подпись и поле ввода для расстояния
        distance_label = QLabel("Введите пройденное расстояние (км):", self)
        self.distance_input = QLineEdit(self)
        layout.addWidget(distance_label)
        layout.addWidget(self.distance_input)

        # Подпись и поле ввода для стоимости топлива
        cost_label = QLabel("Введите стоимость топлива (за литр):", self)
        self.cost_input = QLineEdit(self)
        layout.addWidget(cost_label)
        layout.addWidget(self.cost_input)

        # Кнопка добавления записи
        add_button = QPushButton("Добавить расход", self)
        add_button.clicked.connect(self.add_expense)
        layout.addWidget(add_button)

    def add_expense(self):
        """Добавление записи о расходах и обновление общих расходов."""
        try:
            distance = float(self.distance_input.text())
            cost_per_liter = float(self.cost_input.text())
            expense = distance * cost_per_liter  # Простая модель расчёта расхода
            self.total_expense += expense

            # Отображение общих расходов
            self.show_total_expense()
        except ValueError:
            # Обработка ошибки ввода нечисловых данных
            QMessageBox.warning(self, "Ошибка ввода", "Пожалуйста, введите корректные числовые значения.")

    def show_total_expense(self):
        """Отображение общих расходов на топливо через QMessageBox."""
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Общий расход на топливо")
        msg_box.setText(f"Общий расход на топливо составляет: {self.total_expense:.2f} руб.")
        msg_box.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
