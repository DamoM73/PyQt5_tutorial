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

        # Create an combo box
        my_combo = qtw.QComboBox(self,
            editable = True, 
            insertPolicy=qtw.QComboBox.InsertAtTop)
        # Add Items to the the combobox
        my_combo.addItem("Pepperoni")
        my_combo.addItem("Cheese")
        my_combo.addItem("Mushroom")
        my_combo.addItem("Peppers")
        # put combo box on screen
        self.layout().addWidget(my_combo)


        # Create a button
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()


        def press_it():
            # Add name to label
            my_label.setText(f"You picked {my_combo.currentText()}!")
            



app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()