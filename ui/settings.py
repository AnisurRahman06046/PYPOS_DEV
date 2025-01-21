from PyQt6.QtWidgets import QWidget,QVBoxLayout,QLabel


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Settings")
        
        layout = QVBoxLayout()
        title = QLabel("Welcome to Setting Page")
        layout.addWidget(title)
        self.setLayout(layout)