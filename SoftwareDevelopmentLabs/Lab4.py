import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QMessageBox, QComboBox, QCheckBox, QTableWidget, QTableWidgetItem,
                             QTextEdit, QListWidget, QSlider)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_balance = 0.0
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Семейный бюджет")
        self.setGeometry(100, 100, 800, 600)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        # Ввод доходов и расходов
        input_layout = QHBoxLayout()
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Сумма")
        input_layout.addWidget(self.amount_input)

        self.category_input = QComboBox()
        self.category_input.addItems(["Еда", "Транспорт", "Жилье", "Развлечения"])
        input_layout.addWidget(self.category_input)

        self.is_expense = QCheckBox("Расход")
        input_layout.addWidget(self.is_expense)

        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_transaction)
        input_layout.addWidget(add_button)

        main_layout.addLayout(input_layout)

        # Отслеживание баланса
        self.balance_label = QLabel(f"Текущий баланс: {self.current_balance} руб.")
        main_layout.addWidget(self.balance_label)

        self.transaction_history = QTableWidget(0, 3)
        self.transaction_history.setHorizontalHeaderLabels(["Сумма", "Категория", "Тип"])
        main_layout.addWidget(self.transaction_history)

        # Анализ расходов
        analysis_layout = QHBoxLayout()
        self.analysis_text = QTextEdit()
        analysis_layout.addWidget(self.analysis_text)

        analyze_button = QPushButton("Анализ расходов")
        analyze_button.clicked.connect(self.analyze_expenses)
        analysis_layout.addWidget(analyze_button)

        main_layout.addLayout(analysis_layout)

        central_widget.setLayout(main_layout)

    def add_transaction(self):
        amount = float(self.amount_input.text())
        category = self.category_input.currentText()
        is_expense = self.is_expense.isChecked()

        row_position = self.transaction_history.rowCount()
        self.transaction_history.insertRow(row_position)
        self.transaction_history.setItem(row_position, 0, QTableWidgetItem(f"{amount:.2f}"))
        self.transaction_history.setItem(row_position, 1, QTableWidgetItem(category))
        self.transaction_history.setItem(row_position, 2, QTableWidgetItem("Расход" if is_expense else "Доход"))

        if is_expense:
            self.current_balance -= amount
        else:
            self.current_balance += amount

        self.balance_label.setText(f"Текущий баланс: {self.current_balance} руб.")

    def analyze_expenses(self):
        expenses = {}
        for row in range(self.transaction_history.rowCount()):
            amount, category, type_ = [self.transaction_history.item(row, col).text() for col in range(3)]
            if type_ == "Расход":
                if category not in expenses:
                    expenses[category] = 0
                expenses[category] += float(amount)

        analysis_result = "Анализ расходов по категориям:\n"
        for category, total in expenses.items():
            analysis_result += f"{category}: {total:.2f} руб.\n"

        self.analysis_text.setText(analysis_result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
