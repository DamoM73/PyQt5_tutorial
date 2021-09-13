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
        my_label = qtw.QLabel("Pick something from the list")
        my_label.setFont(qtg.QFont("Helvetica",24))
        self.layout().addWidget(my_label)

        # Create an spin box
        my_spin = qtw.QSpinBox(self,
            value=10,
            maximum=100,
            minimum=0,
            singleStep=5,
            prefix="#",
            suffix=" order")

        # Change font size of spinbox
        my_spin.setFont(qtg.QFont("Helvetica",18))
            
        
        # put combo box on screen
        self.layout().addWidget(my_spin)


        # Create a button
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()


        def press_it():
            # Add name to label
            my_label.setText(f"You picked {my_spin.value()}!")
            



app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()