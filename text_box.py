import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle("Hello World")

        # Set layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Type somehting into the box below")
        my_label.setFont(qtg.QFont("Helvetica",24))
        self.layout().addWidget(my_label)

        # Create an spin box
        my_text = qtw.QTextEdit(self,
            acceptRichText=True,
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Hello World!",
            readOnly=False
            )

        # Change font size of spinbox
        # my_spin.setFont(qtg.QFont("Helvetica",18))
            
        
        # put combo box on screen
        self.layout().addWidget(my_text)


        # Create a button
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()


        def press_it():
            # Add name to label
            my_label.setText(f"You typed {my_text.toPlainText()}!")
            my_text.setPlainText("You clicked the button")
            



app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()