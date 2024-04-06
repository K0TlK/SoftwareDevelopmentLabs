import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()  # Инициализация пользовательского интерфейса

    def initializeUI(self):
        """Настройка параметров окна приложения."""
        self.setGeometry(100, 100, 350, 380)  # Размеры и позиция окна
        self.setWindowTitle("Пример QLabel")  # Заголовок окна
        self.setupMainWindow()  # Настройка содержимого окна
        self.show()  # Показать окно

    def setupMainWindow(self):
        """Создание и настройка виджетов в главном окне."""
        # Создание и настройка текстовой метки
        greeting_label = QLabel(self)
        greeting_label.setText("Привет!")
        greeting_label.move(155, 15)

        # Путь к изображению
        image_path = "images/Земля.png"
        try:
            with open(image_path, 'rb') as file:
                # Убедиться, что файл изображения существует
                world_label = QLabel(self)
                pixmap = QPixmap(image_path)
                pixmap = pixmap.scaled(300, 300)  # Масштабирование изображения
                world_label.setPixmap(pixmap)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print(f"Файл изображения не найден.\nОшибка: {error}")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Создание приложения
    window = MainWindow()  # Создание окна
    sys.exit(app.exec())  # Запуск приложения
