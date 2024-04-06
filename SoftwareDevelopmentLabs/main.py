import sys
from PyQt6.QtWidgets import QApplication


def run_lab(lab_module):
    """Функция для запуска лабораторной работы."""
    MainWindow = lab_module.MainWindow  # Импортируем класс MainWindow из модуля
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()


def main():
    labs = {
        '1': 'Lab1',
        '2': 'Lab2',
        '3': 'Lab3',
        '4': 'Lab4',
        '5': 'Lab5',
        '6': 'Lab6'
    }
    # Меню для выбора лабораторной работы
    while True:
        print("Выберите лабораторную работу для запуска:")
        for key, value in labs.items():
            print(f"{key}: {value}")
        print("7: Выход")
        choice = input("Введите номер (1-7): ")

        if choice in labs:
            lab_module = __import__(labs[choice])
            run_lab(lab_module)
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")


if __name__ == '__main__':
    main()
