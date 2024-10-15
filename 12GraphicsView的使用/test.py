import sys
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import *
from PySide2.QtMultimediaWidgets import *
from PySide2.QtCore import Qt, QUrl

class VideoPlayer(QWidget):
    def __init__(self):
        super(VideoPlayer, self).__init__()

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)

        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")
        self.fullscreen_button = QPushButton("Full Screen")
        self.seek_slider = QSlider(Qt.Horizontal)
        self.seek_slider.sliderMoved.connect(self.set_position)

        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.pause)
        self.stop_button.clicked.connect(self.stop)
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.fullscreen_button)
        layout.addWidget(self.seek_slider)

        self.setLayout(layout)

    def play(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            return
        if self.media_player.state() == QMediaPlayer.PausedState:
            self.media_player.play()
        else:
            file_dialog = QFileDialog()
            video_file, _ = file_dialog.getOpenFileName(self, "Open Video", "", "Video Files (*.mp4 *.avi *.mov)")
            if video_file:
                media_content = QMediaContent(QMediaResource(QUrl.fromLocalFile(video_file)))
                self.media_player.setMedia(media_content)
                self.media_player.play()

    def pause(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()

    def stop(self):
        self.media_player.stop()

    def set_position(self, position):
        self.media_player.setPosition(position)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())