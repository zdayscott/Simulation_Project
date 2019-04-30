from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Backend

import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Tweet Simulator")
        twitter_icon = QIcon("twitter_icon.png")
        self.setWindowIcon(twitter_icon)
        self.setMinimumWidth(750)
        self.setMinimumHeight(750)

        # custom style sheet
        self.styleSheet = """
        
        QPushButton#button {
            background-color: #1e90ff;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;
        }
        
        QPushButton#button:pressed {
            background-color: #0000ff;
            border-style: inset;
        }
        
        QPushButton#reset {
            background-color: #ff0000;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;
        }
        
        QPushButton#reset:pressed {
            background-color: #8b0000;
            border-style: inset;
        }
        QWidget {
            background-color: white;
        }
        """

        self.setStyleSheet(self.styleSheet)
        layout = QGridLayout()
        self.setLayout(layout)

        # label above hate scale to display current amount of hate
        self.hate_label = QLabel("Scale of Hate: 0")

        # create slider for the hate scale
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setValue(0)
        self.slider.setMinimum(0)
        self.slider.setMaximum(5)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTracking(1)
        self.slider.valueChanged.connect(self.update_hate)

        # create entry box for user
        self.entry_box = QLineEdit()
        self.entry_box.setPlaceholderText("Event")

        # create drop down list box
        self.option_list = QListWidget()
        self.option_list.setMaximumHeight(100)
        self.option_list.addItem("Place")
        self.option_list.addItem("Event")
        self.option_list.addItem("Person")

        # create small icon for generic profile image
        self.generic_profile_image = QPixmap()
        self.generic_profile_image.load("profile_pic_2.png")
        self.generic_profile_image = self.generic_profile_image.scaledToHeight(75)
        self.generic_profile_image = self.generic_profile_image.scaledToWidth(75)
        self.profile_pic_label = QLabel()
        self.profile_pic_label.setPixmap(self.generic_profile_image)

        # create button to submit Tweet
        tweet_button = QPushButton("Tweet")
        tweet_button.setObjectName("button")
        tweet_button.clicked.connect(self.get_input)

        # create button to reset all user input
        reset_button = QPushButton("Reset")
        reset_button.setObjectName("reset")
        reset_button.clicked.connect(self.reset_info)

        # create left frame to handle user input
        self.left_frame = QFrame()
        self.left_frame.setLineWidth(4)
        self.left_frame.setMinimumHeight(self.frameGeometry().width() / 2)
        self.left_frame.setMinimumWidth(400)
        self.left_frame.setFrameShadow(QFrame.Plain)
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setStyleSheet("background-color: WHITE")
        layout.addWidget(self.left_frame, 0, 0)

        # create internal layout for left frame and add all the widgets to take user input
        left_frame_layout = QVBoxLayout()
        self.left_frame.setLayout(left_frame_layout)
        self.left_frame.setStyleSheet(self.styleSheet)
        left_frame_layout.addStretch(1)
        left_frame_layout.addWidget(self.profile_pic_label)
        left_frame_layout.addWidget(self.entry_box, 1, Qt.AlignTop)
        left_frame_layout.addWidget(self.hate_label)
        left_frame_layout.addWidget(self.slider, 1, Qt.AlignTop)
        left_frame_layout.addWidget(self.option_list, 1, Qt.AlignTop)
        left_frame_layout.addWidget(tweet_button)
        left_frame_layout.addWidget(reset_button)

        # create label to hold trumps profile pic and load picture into label
        self.trump_pic_label = QLabel()
        self.trump_profile_pic = QPixmap()
        self.trump_profile_pic.load("trump_pic.png")
        self.trump_pic_label.setPixmap(self.trump_profile_pic)

        # create right frame to handle output
        self.right_frame = QFrame()
        self.right_frame.setLineWidth(4)
        self.right_frame.setMinimumWidth(self.frameGeometry().width() / 2)
        self.right_frame.setMinimumHeight(400)
        self.right_frame.setFrameShadow(QFrame.Plain)
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setStyleSheet(self.styleSheet)
        layout.addWidget(self.right_frame, 0, 1)

        # create small frame to hold generated tweet
        self.tweet_frame = QFrame()
        self.tweet_frame.setLineWidth(4)
        self.tweet_frame.setMinimumWidth(self.right_frame.width())
        self.tweet_frame.setMinimumHeight(self.right_frame.height() / 2)
        self.tweet_frame.setStyleSheet("background-color: #191970; color: white; font: bold 14px")
        self.tweet_frame.hide()

        # label to hold Trumps profile avatar
        trump_profile_label = QLabel()
        trump_profile_avatar = QPixmap()
        trump_profile_avatar.load("trump_profile.png")
        trump_profile_avatar = trump_profile_avatar.scaledToWidth(80, 80)
        trump_profile_label.setStyleSheet("border-radius: 40px;")
        trump_profile_label.setPixmap(trump_profile_avatar)

        # label for Trump's Name
        self.trump_name = QLabel()
        self.trump_name.setText("Donald J. Trump")

        # label for Trump's twitter handle
        self.trump_twitter_handle = QLabel()
        self.trump_twitter_handle.setText("@realDonaldTrump")

        # label to hold tweet body
        self.tweet_body = QLabel()
        self.tweet_body.setStyleSheet("color: white; font: 14px;")
        self.tweet_body.setWordWrap(True)

        # create internal horizontal box layout for tweet_frame
        self.tweet_frame_horz_layout = QHBoxLayout()
        self.tweet_frame_horz_layout.addWidget(trump_profile_label, 0, Qt.AlignTop)
        self.tweet_frame_horz_layout.addWidget(self.trump_name, 0, Qt.AlignTop)
        self.tweet_frame_horz_layout.addWidget(self.trump_twitter_handle, 1, Qt.AlignTop)

        # create internal vertical Box Layout to align tweet body
        # this Box Layout will contain horizontal box layout used for
        # profile_avatar and trumps name
        self.tweet_frame_vert_layout = QVBoxLayout()
        self.tweet_frame_vert_layout.addLayout(self.tweet_frame_horz_layout)
        self.tweet_frame_vert_layout.addWidget(self.tweet_body, 1, Qt.AlignTop)
        self.tweet_body.setIndent(100)

        # apply box layouts to tweet frame
        self.tweet_frame.setLayout(self.tweet_frame_vert_layout)

        # create internal layout for right frame to display generated tweet
        self.right_frame_layout = QGridLayout()
        self.right_frame.setLayout(self.right_frame_layout)
        self.right_frame_layout.addWidget(self.trump_pic_label, 0, 0)
        self.right_frame_layout.addWidget(self.tweet_frame, 1, 0)

        # init tweet contents
        self.tweet_content = "tweet"

    # function to update the current hate label
    def update_hate(self, val):
        self.hate_label.setText("Scale of Hate: " + str(val))
        self.get_input()

    # get all uer input
    def get_input(self):
        print("Slider value: ", self.slider.value())
        print("Entry box value: ", self.entry_box.text())
        if self.option_list.currentItem():
            selected_item = self.option_list.currentItem()
            print("List Box value: ", selected_item.text())
        self.gen_tweet()

    # reset all input methods
    def reset_info(self):
        self.entry_box.clear()
        self.slider.setValue(0)
        self.option_list.clearSelection()
        self.entry_box.setFocus()
        self.tweet_body.setText("")
        self.tweet_frame.hide()

    def gen_tweet(self):
        self.tweet_frame.show()
        inp = self.entry_box.text()
        self.tweet_content = Backend.MarkovTrumpReactiveTweetGen(inp)
        self.display_tweet(self.tweet_content)
        # self.reset_info()

    def display_tweet(self, tweet):
        self.tweet_body.setText(tweet)


app = QApplication(sys.argv)

screen = Window()
screen.show()
sys.exit(app.exec_())
