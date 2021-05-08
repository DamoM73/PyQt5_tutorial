import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from Ui_MainWindow import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.enter_btn.clicked.connect(self.greet)

    def show(self):
        self.main_win.show()

    def greet(self):
        name = self.ui.name_input.text()
        greeting = f"Hello {name}. How are you"
        self.ui.greeting_lb.setText(greeting)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
