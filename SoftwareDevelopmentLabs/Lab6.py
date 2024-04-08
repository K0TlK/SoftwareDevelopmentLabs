import sys

from PyQt6 import QtWidgets, QtSql, QtGui


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


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Store Manager')
        self.resize(800, 600)

        # Создаем модели для исполнителей, песен и альбомов
        self.artists_model = QtSql.QSqlTableModel(self)
        self.artists_model.setTable('Artists')
        self.artists_model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
        self.artists_model.select()

        self.songs_model = QtSql.QSqlTableModel(self)
        self.songs_model.setTable('Songs')
        self.songs_model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
        self.songs_model.select()

        self.albums_model = QtSql.QSqlTableModel(self)
        self.albums_model.setTable('Albums')
        self.albums_model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
        self.albums_model.select()

        # Создаем представления для моделей
        self.artists_view = QtWidgets.QTableView()
        self.artists_view.setModel(self.artists_model)

        self.songs_view = QtWidgets.QTableView()
        self.songs_view.setModel(self.songs_model)

        self.albums_view = QtWidgets.QTableView()
        self.albums_view.setModel(self.albums_model)

        # Создаем вкладки для исполнителей, песен и альбомов
        self.tab_widget = QtWidgets.QTabWidget()
        self.tab_widget.addTab(self.artists_view, "Artists")
        self.tab_widget.addTab(self.songs_view, "Songs")
        self.tab_widget.addTab(self.albums_view, "Albums")
        self.setCentralWidget(self.tab_widget)

        # Создаем панель инструментов с кнопками для управления данными и переключения вкладок
        toolbar = QtWidgets.QToolBar("Manage")
        self.addToolBar(toolbar)

        add_button = QtGui.QAction('Add Row', self)
        add_button.triggered.connect(self.add_row)
        save_button = QtGui.QAction('Save Changes', self)
        save_button.triggered.connect(self.save_changes)
        delete_button = QtGui.QAction('Delete Row', self)
        delete_button.triggered.connect(self.delete_row)

        switch_to_artists = QtGui.QAction('Switch to Artists', self)
        switch_to_artists.triggered.connect(lambda: self.tab_widget.setCurrentIndex(0))
        switch_to_songs = QtGui.QAction('Switch to Songs', self)
        switch_to_songs.triggered.connect(lambda: self.tab_widget.setCurrentIndex(1))
        switch_to_albums = QtGui.QAction('Switch to Albums', self)
        switch_to_albums.triggered.connect(lambda: self.tab_widget.setCurrentIndex(2))

        toolbar.addAction(add_button)
        toolbar.addAction(save_button)
        toolbar.addAction(delete_button)
        toolbar.addSeparator()
        toolbar.addAction(switch_to_artists)
        toolbar.addAction(switch_to_songs)
        toolbar.addAction(switch_to_albums)

    def add_row(self):
        # Получаем текущий индекс вкладки
        current_index = self.tab_widget.currentIndex()

        # Определяем, какая вкладка сейчас активна
        if current_index == 0:  # Вкладка "Artists"
            self.artists_model.insertRows(self.artists_model.rowCount(), 1)
        elif current_index == 1:  # Вкладка "Songs"
            self.songs_model.insertRows(self.songs_model.rowCount(), 1)
        elif current_index == 2:  # Вкладка "Albums"
            self.albums_model.insertRows(self.albums_model.rowCount(), 1)

    def save_changes(self):
        # Сохраняем изменения во всех моделях
        self.artists_model.submitAll()
        self.songs_model.submitAll()
        self.albums_model.submitAll()

    def delete_row(self):
        # Получаем текущий индекс вкладки
        current_index = self.tab_widget.currentIndex()

        # Определяем, какая вкладка сейчас активна
        if current_index == 0:  # Вкладка "Artists"
            selected_rows = self.artists_view.selectionModel().selectedRows()
            for row in reversed(selected_rows):
                self.artists_model.removeRow(row.row())
        elif current_index == 1:  # Вкладка "Songs"
            selected_rows = self.songs_view.selectionModel().selectedRows()
            for row in reversed(selected_rows):
                self.songs_model.removeRow(row.row())
        elif current_index == 2:  # Вкладка "Albums"
            selected_rows = self.albums_view.selectionModel().selectedRows()
            for row in reversed(selected_rows):
                self.albums_model.removeRow(row.row())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    if not create_connection():
        sys.exit(-1)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
