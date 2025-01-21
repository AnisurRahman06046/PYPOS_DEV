from PyQt6.QtWidgets import QWidget,QVBoxLayout,QLabel


class StaffPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        title = QLabel("Welcome to Staff page")
        layout.addWidget(title)
        self.setWindowTitle("Staff")
        self.setLayout(layout)