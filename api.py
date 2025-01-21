import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class ApiFetcher(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize API token
        self.api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoic3RhZmYiLCJmaXJzdE5hbWUiOiJadWxrYXIiLCJsYXN0X25hbWUiOiJOaW5lIiwiZW1haWwiOiJ6bnM2MDFAZ21haWwuY29tIiwicGhvbmUiOiIwMTg2OTA4NDYyMCIsInBhc3N3b3JkIjoicGFzc3dvcmQiLCJpYXQiOjE3MzcyODQ2MjMsImV4cCI6MTgzMTk1NzQyM30.mJx4Jcm0PZ2w1u1KI2jWz9_oIaYfh6l0Hayr83MhbUs"
        
        self.manager = QNetworkAccessManager(self)
        self.manager.finished.connect(self.on_finished)

        # Set up the UI
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Fetching data...", self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setWindowTitle("Fetch Data from REST API")
        self.setGeometry(100, 100, 300, 100)

        # Call the API when the application starts
        self.fetch_data()

    def fetch_data(self):
        # Replace with your actual API URL
        url = QUrl("https://anzaar-api.bitcommerz.com/api/v1/order/get-for-pos")
        request = QNetworkRequest(url)

        # Set the Authorization header with the token
        request.setRawHeader(b"Authorization", f"Bearer {self.api_token}".encode())

        # Send GET request with the token in the header
        self.manager.get(request)

    def on_finished(self, reply: QNetworkReply):
        # Check if the request was successful
        if reply.error() == QNetworkReply.NetworkError.NoError:
            data = reply.readAll().data().decode()
            self.label.setText(f"Response: {data}")
        else:
            self.label.setText(f"Error: {reply.errorString()}")
        reply.deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ApiFetcher()
    window.show()
    sys.exit(app.exec())
