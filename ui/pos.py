from PyQt6.QtWidgets import QWidget,QVBoxLayout,QLabel


class PosTerminalPage(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("POS Terminal")
        layout = QVBoxLayout()
        title = QLabel("Welcome to Pos Terminal")
        layout.addWidget(title)
        
        self.setLayout(layout)