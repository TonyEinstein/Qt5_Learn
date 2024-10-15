import sys
import requests
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressBar
from PySide2.QtCore import QThread, Signal

class Downloader(QThread):
    progress_update = Signal(int)

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.paused = False

    def run(self):
        response = requests.get(self.url, stream=True)
        total_length = int(response.headers.get('content-length'))
        downloaded = 0

        with open('downloaded_file', 'wb') as f:
            for data in response.iter_content(chunk_size=1024):
                if self.paused:
                    while self.paused:
                        pass
                downloaded += len(data)
                f.write(data)
                progress = int(downloaded / total_length * 100)
                self.progress_update.emit(progress)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

class FileDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.progress_bar = QProgressBar()
        self.start_button = QPushButton("Start Download")
        self.pause_button = QPushButton("Pause")
        self.resume_button = QPushButton("Resume")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.pause_button)
        self.layout.addWidget(self.resume_button)
        self.setLayout(self.layout)

        self.downloader = Downloader("https://example.com/file-to-download")
        self.downloader.progress_update.connect(self.update_progress)

        self.start_button.clicked.connect(self.start_download)
        self.pause_button.clicked.connect(self.pause_download)
        self.resume_button.clicked.connect(self.resume_download)

        self.setWindowTitle("File Downloader")
        self.show()

    def start_download(self):
        self.downloader.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def pause_download(self):
        self.downloader.pause()

    def resume_download(self):
        self.downloader.resume()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    downloader_app = FileDownloader()
    sys.exit(app.exec_())