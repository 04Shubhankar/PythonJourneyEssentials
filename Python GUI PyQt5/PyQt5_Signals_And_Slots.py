import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# Define a Window class that inherits from QWidget
class Window(QWidget):
    def __init__(self):
        super().__init__()  # Call the parent class (QWidget) initializer
        
        # Create a label and set its initial text
        self.label = QLabel("Hello, World!")
        
        # Create a button and set its text
        self.button = QPushButton("Click Me")

        # Connect the button's clicked signal to the change_text method
        # This means that when the button is clicked, the change_text method will be executed
        self.button.clicked.connect(self.change_text)

        # Set up a vertical layout and add widgets to it
        layout = QVBoxLayout()  # QVBoxLayout arranges widgets vertically
        layout.addWidget(self.label)  # Add the label to the layout
        layout.addWidget(self.button)  # Add the button below the label
        self.setLayout(layout)  # Apply the layout to the Window

    # Define a slot method that changes the label's text
    def change_text(self):
        self.label.setText("Button clicked!")  # Update the label text when the button is clicked

# Main entry point for the application
if __name__ == '__main__':
    # Create an application instance (needed for any PyQt application)
    app = QApplication(sys.argv)
    
    # Create an instance of the Window class
    window = Window()
    window.show()  # Show the window
    
    # Execute the application's event loop
    sys.exit(app.exec_())
