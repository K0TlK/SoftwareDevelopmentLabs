import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QFont, QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.detail_expanded = False  # Для отслеживания состояния расширенного текста
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 300, 500)  # Стандартные размеры окна
        self.setWindowTitle("Об авторе")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        images = ["images/Фон.jpg", "images/Фото.png"]
        for image in images:
            try:
                with open(image, 'rb'):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    label.setScaledContents(True)
                    if image == "images/Фон.jpg":
                        label.setGeometry(0, 0, 300, 150)
                    elif image == "images/Фото.png":
                        label.setGeometry(115, 20, 100, 100)
            except FileNotFoundError as error:
                print(f"Файл изображения не найден.\nОшибка: {error}")

    def buttonClicked(self):
        self.close()

    def moreDetailsClicked(self):
        if not self.detail_expanded:
            self.resize(300, 600)  # Увеличение размера окна
            self.more_details_label.setText("А я ещё я очень хочу пиццу")  # Отображение дополнительного текста
            self.detail_expanded = True
        else:
            self.resize(300, 500)  # Возврат к исходным размерам окна
            self.more_details_label.setText("")
            self.detail_expanded = False

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
        about_label.setText("Unity Developer с опытом разработки IAP, UI, интеграции SDK и архитектуры мини-игр. Работал в 'СОФТИНТЕРМОБ' и 'BrainyLab'.")
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

        # Добавление дополнительной метки для текста
        self.more_details_label = QLabel("", self)
        self.more_details_label.setWordWrap(True)
        self.more_details_label.setGeometry(15, 470, 270, 100)

        more_button = QPushButton("Подробнее", self)
        more_button.move(15, 470)
        more_button.clicked.connect(self.moreDetailsClicked)

        ok_button = QPushButton("OK", self)
        ok_button.move(115, 470)
        ok_button.clicked.connect(self.buttonClicked)


# Запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
