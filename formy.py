import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle("Hello World")

        # Set layout
        #self.setLayout(qtw.QVBoxLayout())
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Add stuff
        label_1 = qtw.QLabel("This is a cool label Row")
        label_1.setFont(qtg.QFont("Helvetica",24))
        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        # add rows to app
        form_layout.addRow(label_1)
        form_layout.addRow("First Name", f_name)
        form_layout.addRow("Last Name", l_name)
        form_layout.addRow(qtw.QPushButton("Click me", clicked= lambda: press_it()))

        # Show the app
        self.show()

        def press_it():
            label_1.setText(f"{f_name.text()} you clicked the button")


app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()