import sys
from PyQt5 import QtWidgets
import sqlite3

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connection()

    def connection(self):
        self.conn = sqlite3.connect("Users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("Create Table if not exists Members(Id integer primary key, Player_Id integer, NickName text, Name text , "
                            "Surname text, Email text unique not null, Password text not null,Phone text, Age integer, BirthDate datetime);")
        self.conn.commit()

    def init_ui(self):
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.text_input = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text_input)
        v_box.addStretch()
        v_box.addWidget(self.login)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("True or False")
        self.login.clicked.connect(self.enter)
        self.show()

    def enter(self):
        name = self.username.text()
        watchword = self.password.text()

        self.cursor.execute("Select * from members where NickName = ? and Password = ?", (name, watchword))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.text_input.setText("No record found with given info.\n Did you forget your password?")
        else:
            self.text_input.setText("Welcome to True False")


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.setGeometry(150, 150, 400, 400)
sys.argv(app.exec_())
