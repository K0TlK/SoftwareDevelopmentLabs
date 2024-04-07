import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QFont, QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 300, 500)  # Увеличенные размеры для более комфортного отображения информации
        self.setWindowTitle("Об авторе")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        # Пути к изображениям
        images = ["images/Фон.jpg", "images/Фото.png"]
        for image in images:
            try:
                with open(image, 'rb'):  # Убедиться, что файл существует
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    label.setScaledContents(True)
                    if image == "images/Фон.jpg":
                        label.setGeometry(0, 0, 300, 150)  # Немного измененные размеры для более лучшего соответствия
                    elif image == "images/Фото.png":
                        label.setGeometry(115, 20, 100, 100)  # Централизованное размещение
            except FileNotFoundError as error:
                print(f"Файл изображения не найден.\nОшибка: {error}")

    def buttonClicked(self):
        self.close()

    def setUpMainWindow(self):
        self.createImageLabels()

        user_label = QLabel(self)
        user_label.setText("Константин Дьяченко")
        user_label.setFont(QFont("Arial", 16))
        user_label.move(50, 150)

        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Arial", 14))
        bio_label.move(15, 170)

        about_label = QLabel(self)
        about_label.setText(
            "Unity Developer с опытом разработки IAP, UI, интеграции SDK и архитектуры мини-игр. Работал в 'СОФТИНТЕРМОБ' и 'BrainyLab'.")
        about_label.setWordWrap(True)
        about_label.move(15, 190)

        skills_label = QLabel(self)
        skills_label.setText("Навыки")
        skills_label.setFont(QFont("Arial", 14))
        skills_label.move(15, 270)

        languages_label = QLabel(self)
        languages_label.setText("C#, Unity, Python и другие")
        languages_label.move(15, 290)

        experience_label = QLabel(self)
        experience_label.setText("Опыт работы")
        experience_label.setFont(QFont("Arial", 14))
        experience_label.move(15, 320)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Москва и Новосибирск, 2 года и 4 месяца")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 340)

        self.button = QPushButton("OK", self)
        self.button.move(115, 460)  # Централизованная кнопка
        self.button.clicked.connect(self.buttonClicked)


# Запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
