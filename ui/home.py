from PyQt6.QtWidgets import QWidget,QVBoxLayout,QLabel

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        title = QLabel("Home Page")
        layout.addWidget(title)
        self.setWindowTitle("Home")
        self.setLayout(layout)