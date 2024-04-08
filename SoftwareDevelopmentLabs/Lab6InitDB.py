import sys
from PyQt6 import QtWidgets, QtSql
from PyQt6.QtSql import QSqlDatabase


def create_connection():
    """Создает подключение к базе данных SQLite."""
    # Добавляем базу данных SQLite
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('music_store.db')  # Указываем имя файла базы данных SQLite
    if not db.open():
        error_msg = QtWidgets.QMessageBox()
        error_msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        error_msg.setText("Не удалось подключиться к базе данных")
        error_msg.setInformativeText(db.lastError().text())
        error_msg.setWindowTitle("Ошибка подключения")
        error_msg.exec()
        return False
    return True

    # Попытка открыть соединение
    if not db.open():
        print(f"Не удалось подключиться к базе данных: {db.lastError().text()}")
        return False
    return True


def create_tables():
    """Создает таблицы в базе данных."""
    query = QtSql.QSqlQuery()
    # Создание таблицы Исполнители
    query.exec("""
        CREATE TABLE IF NOT EXISTS Artists (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            genre VARCHAR(100)
        );
    """)
    # Создание таблицы Альбомы
    query.exec("""
        CREATE TABLE IF NOT EXISTS Albums (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            artist_id INTEGER REFERENCES Artists(id),
            release_year INTEGER
        );
    """)
    # Создание таблицы Песни
    query.exec("""
        CREATE TABLE IF NOT EXISTS Songs (
            id SERIAL PRIMARY KEY,
            album_id INTEGER REFERENCES Albums(id),
            title VARCHAR(255),
            duration INTEGER
        );
    """)


if __name__ == "__main__":
    available_drivers = QSqlDatabase.drivers()
    print(available_drivers)
    if create_connection():
        print("Подключение к базе данных успешно установлено.")
        create_tables()
    else:
        print("Подключение к базе данных не удалось.")
