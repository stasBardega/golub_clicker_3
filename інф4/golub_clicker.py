from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys

app = QApplication(sys.argv)


window2_push_button = QPushButton()
window2_push_button.setFixedSize(150, 150)

window = QWidget()
window.setWindowTitle("Golub.clicker")
window.resize(800, 600)

menu_window = QWidget()
menu_window.setWindowTitle("Golub_clicker_menu")
menu_window.resize(800, 600)

window3 = QWidget()
window3.setWindowTitle("Golub_clicker2")
window3.resize(800, 600)

window_setting = QWidget()
window_setting.setWindowTitle("Golub_clicker_setting")
window_setting.resize(800, 600)

current_boost = 1

score1 = 0
score = QLabel()
score.setText(str(score1))
score.setStyleSheet("font-size: 50;")


window3_push_button = QPushButton()
window3_push_button.setText("Наступна локація")
window3_sell = QPushButton()
window3_sell.setText("Ціна: 1м")


current_boost2 = 1

score2 = 0
score2_text = QLabel()
score2_text.setText(str(score2))
score2_text.setStyleSheet("font-size: 45px;")





def on_media_status_changet(status):
     if status == QMediaPlayer.EndOfMedia:
          player.setPosition(0)
          player.play()


player = QMediaPlayer()
url = QUrl.fromLocalFile("music.mp3")
player.setMedia(QMediaContent(url))
player.play()
player.mediaStatusChanged.connect(on_media_status_changet)


setting = QPushButton()
setting.setFixedSize(150, 150)



slider = QSlider()
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue(50)




leave_setting = QPushButton()



name_of_game_menu = QLabel()
name_of_game_menu.setText("Golub clicker")



boost_text2 = QLabel()
boost_text2.setText(f"Сила кліку: {current_boost}")



area = QPushButton()
area.setFixedSize(250, 250)

pixmap = QPixmap("images.jpg")
area.setIcon(QIcon(pixmap))
area.setIconSize(pixmap.size())
area.setStyleSheet("text-align: center;")

pixmap = QPixmap("setting_image.png")
setting.setIcon(QIcon(pixmap))
setting.setIconSize(pixmap.size())
setting.setStyleSheet("text-align: center;")

pixmap = QPixmap("play.jpg")
window2_push_button.setIcon(QIcon(pixmap))
window2_push_button.setIconSize(pixmap.size())
window2_push_button.setStyleSheet("text-align: center;")


window.setWindowIcon(QIcon("menu_image.jpg"))

menu_window.setStyleSheet("background-image: url('menu_image.jpg')")

upgrade_text = QLabel()
boost_text = QLabel()
boost_text.setText(f"Сила кліку: {current_boost}")
upgrade7_sell = QPushButton()
upgrade7_sell.setText("Ціна 35000")
upgrade7 = QPushButton()
upgrade7.setText("+100")
upgrade8_sell = QPushButton()
upgrade8_sell.setText("Ціна 70000")
upgrade8 = QPushButton()
upgrade8.setText("+250")
upgrade9_sell = QPushButton()
upgrade9_sell.setText("Ціна 150000")
upgrade9 = QPushButton()
upgrade9.setText("+500")
upgrade10_sell = QPushButton()
upgrade10_sell.setText("Ціна 500000")
upgrade10 = QPushButton()
upgrade10.setText("+1500")
upgrade6 = QPushButton()
upgrade6.setText("+50")
upgrade6_sell = QPushButton()
upgrade6_sell.setText("Ціна 15000")
upgrade_text.setText("UPGRADES")
upgrade2_sell = QPushButton()
upgrade2_sell.setText("Ціна: 500 кліків")
upgrade2 = QPushButton()
upgrade2.setText("+5")
upgrade3_sell = QPushButton()
upgrade3_sell.setText("Ціна: 1250 кліків")
upgrade3 = QPushButton()
upgrade3.setText("+10")
upgrade4 = QPushButton()
upgrade4_sell = QPushButton()
upgrade4_sell.setText("Ціна: 3000 кліків")
upgrade4.setText("+15")
upgrade5_sell = QPushButton()
upgrade5_sell.setText("Ціна: 7500 кліків")
upgrade5 = QPushButton()
upgrade5.setText("+25")
upgrade_sell = QPushButton()
upgrade_sell.setText("Ціна: 100 кліків")
upgrade = QPushButton()
upgrade.setText("+1")
button_leave = QPushButton()
button_leave.setText("Leave")


tap2_zona = QPushButton()
tap2_zona.setFixedSize(250, 250)

leave_zona2 = QPushButton()
leave_zona2.setText("Leave")
upgrade_2 = QPushButton()
upgrade_2.setText("+ 5")
upgrade_2_text = QPushButton()
upgrade_2_text.setText("Ціна: 150 кліків")
upgrade2_2 = QPushButton()
upgrade2_2.setText("+ 20")
upgrade2_2_text = QPushButton()
upgrade2_2_text.setText("Ціна: 450 кліків")
upgrade3_2 = QPushButton()
upgrade3_2.setText("+ 150")
upgrade3_2_text = QPushButton()
upgrade3_2_text.setText("Ціна: 2500 кліків")
upgrade4_2 = QPushButton()
upgrade4_2.setText("+ 1250")
upgrade4_2_text = QPushButton()
upgrade4_2_text.setText("Ціна: 15000 кліків")
upgrade5_2 = QPushButton()
upgrade5_2.setText("+ 15000")
upgrade5_2_text = QPushButton()
upgrade5_2_text.setText("Ціна: 125000 кліків")
upgrade6_2 = QPushButton()
upgrade6_2.setText("+ 150000")
upgrade6_2_text = QPushButton()
upgrade6_2_text.setText("Ціна: 4.5 млн кліків")
upgrade7_2 = QPushButton()
upgrade7_2.setText("+ 1м")
upgrade7_2_text = QPushButton()
upgrade7_2_text.setText("Ціна: 20 млн кліків ")
upgrade8_2 = QPushButton()
upgrade8_2.setText("+ 10м")
upgrade8_2_text = QPushButton()
upgrade8_2_text.setText("Ціна: 150 млн кліків")
upgrade9_2 = QPushButton()
upgrade9_2.setText("+ 100м")
upgrade9_2_text = QPushButton()
upgrade9_2_text.setText("Ціна: 1 мільярд кліків")
upgrade10_2 = QPushButton()
upgrade10_2.setText("+ 2 мільярда")
upgrade10_2_text = QPushButton()
upgrade10_2_text.setText("Ціна: 10 мільярдів кліків")

layout1_2 = QVBoxLayout()
layout2_2 = QVBoxLayout()
layout3_2 = QVBoxLayout()
layout_4_2 = QVBoxLayout()

layout2_2.setSpacing(0)
layout2_2.setContentsMargins(0, 0, 0, 0)


layout3_2.setSpacing(0)
layout3_2.setContentsMargins(0, 0, 0, 0)

layout1_2.addWidget(tap2_zona)
layout1_2.addWidget(leave_zona2)

layout_4_2.addWidget(boost_text2)
layout_4_2.addWidget(score2_text)

layout_h_1_2 = QHBoxLayout()


window3.setLayout(layout_h_1_2)

pixmap = QPixmap("level2_image.jpg")
tap2_zona.setIcon(QIcon(pixmap))
tap2_zona.setIconSize(pixmap.size())
tap2_zona.setStyleSheet("text-align: center;")

layout1 = QVBoxLayout()
layout3 = QVBoxLayout()
layout4 = QVBoxLayout()
layout5 = QVBoxLayout()
menu_layout = QVBoxLayout()
setting_layout = QVBoxLayout()

layout3.setSpacing(0)
layout3.setContentsMargins(0, 0, 0, 0)

layout5.setSpacing(0)
layout5.setContentsMargins(0, 0, 0, 0)

frame = QFrame()
frame_layout = QVBoxLayout()
frame_layout2 = QVBoxLayout()
frame_layout3 = QVBoxLayout()
frame_layout4 = QVBoxLayout()
frame_layout5 = QVBoxLayout()
frame_layout6 = QVBoxLayout()
frame_layout7 = QVBoxLayout()
frame_layout8 = QVBoxLayout()
frame_layout9 = QVBoxLayout()
frame_layout10 = QVBoxLayout()
frame_layout11 = QVBoxLayout()
frame_layout12 = QVBoxLayout()
frame_layout13 = QVBoxLayout()
frame_layout14 = QVBoxLayout()
frame_layout15 = QVBoxLayout()
frame_layout16 = QVBoxLayout()
frame_layout17 = QVBoxLayout()
frame_layout18 = QVBoxLayout()
frame_layout19 = QVBoxLayout()
frame_layout20 = QVBoxLayout()
frame_layout21 = QVBoxLayout()

frame_layout21.addWidget(upgrade10_2)
frame_layout21.addWidget(upgrade10_2_text)

frame_layout20.addWidget(upgrade9_2)
frame_layout20.addWidget(upgrade9_2_text)

frame_layout19.addWidget(upgrade8_2)
frame_layout19.addWidget(upgrade8_2_text)

frame_layout18.addWidget(upgrade7_2)
frame_layout18.addWidget(upgrade7_2_text)

frame_layout17.addWidget(upgrade6_2)
frame_layout17.addWidget(upgrade6_2_text)

frame_layout16.addWidget(upgrade5_2)
frame_layout16.addWidget(upgrade5_2_text)

frame_layout15.addWidget(upgrade4_2)
frame_layout15.addWidget(upgrade4_2_text)

frame_layout14.addWidget(upgrade3_2)
frame_layout14.addWidget(upgrade3_2_text)

frame_layout13.addWidget(upgrade2_2)
frame_layout13.addWidget(upgrade2_2_text)

frame_layout12.addWidget(upgrade_2)
frame_layout12.addWidget(upgrade_2_text)

frame_layout11.addWidget(window3_push_button)
frame_layout11.addWidget(window3_sell)

frame_layout10.addWidget(upgrade10)
frame_layout10.addWidget(upgrade10_sell)

frame_layout9.addWidget(upgrade9)
frame_layout9.addWidget(upgrade9_sell)

frame_layout8.addWidget(upgrade8)
frame_layout8.addWidget(upgrade8_sell)

frame_layout7.addWidget(upgrade7)
frame_layout7.addWidget(upgrade7_sell)

frame_layout6.addWidget(upgrade6)
frame_layout6.addWidget(upgrade6_sell)

frame_layout3.addWidget(upgrade)
frame_layout3.addWidget(upgrade_sell)

frame_layout4.addWidget(upgrade4)
frame_layout4.addWidget(upgrade4_sell)

frame_layout5.addWidget(upgrade5)
frame_layout5.addWidget(upgrade5_sell)

frame_layout2.addWidget(upgrade3)
frame_layout2.addWidget(upgrade3_sell)

frame_layout.addWidget(upgrade2)
frame_layout.addWidget(upgrade2_sell)

frame_layout.setSpacing(0)
frame_layout.setContentsMargins(0, 0, 0, 0)




layout1.addWidget(area)
layout1.addWidget(button_leave)




layout4.addWidget(boost_text)
layout4.addWidget(score)



menu_layout.addWidget(name_of_game_menu, alignment=Qt.AlignCenter)
menu_layout.addWidget(window2_push_button, alignment=Qt.AlignCenter)
menu_layout.addWidget(setting, alignment=Qt.AlignCenter)


setting_layout.addWidget(slider, alignment=Qt.AlignCenter)
setting_layout.addWidget(leave_setting)


layout2 = QHBoxLayout()



layout5.addLayout(frame_layout10)
layout5.addLayout(frame_layout9)
layout5.addLayout(frame_layout8)
layout5.addLayout(frame_layout7)
layout5.addLayout(frame_layout6)
layout3.addLayout(frame_layout)
layout3.addLayout(frame_layout2)
layout3.addLayout(frame_layout3)
layout3.addLayout(frame_layout4)
layout3.addLayout(frame_layout5)
layout4.addLayout(frame_layout11)
layout2.addLayout(layout1)
layout2.addLayout(layout3)
layout2.addLayout(layout5)
layout2.addLayout(layout4)



layout2_2.addLayout(frame_layout12)
layout2_2.addLayout(frame_layout13)
layout2_2.addLayout(frame_layout14)
layout2_2.addLayout(frame_layout15)
layout2_2.addLayout(frame_layout16)

layout3_2.addLayout(frame_layout17)
layout3_2.addLayout(frame_layout18)
layout3_2.addLayout(frame_layout19)
layout3_2.addLayout(frame_layout20)
layout3_2.addLayout(frame_layout21)




window.setLayout(layout2)
menu_window.setLayout(menu_layout)
window_setting.setLayout(setting_layout)




layout_h_1_2.addLayout(layout1_2)
layout_h_1_2.addLayout(layout2_2)
layout_h_1_2.addLayout(layout3_2)
layout_h_1_2.addLayout(layout_4_2)




game_over = False


def score_2():
    global score2
    score2 += current_boost2
    score2_text.setText(str(score2))


def leave_level_2():
    window.hide()
    window_setting.hide()
    window3.hide()
    menu_window.show()


def setting_leave():
     window_setting.hide()
     window.hide()
     window3.hide()
     menu_window.show()

def music_editor(value):
     player.setVolume(value)


def setting_window():
     menu_window.hide()
     window.hide()
     window3.hide()
     window_setting.show()

def level2():
    global score1
    if score1 >= 1000000:
         menu_window.hide()
         window.hide()
         window3.show()

def start_game():
     menu_window.hide()
     window.show()

def leave():
    window.hide()
    menu_window.show()

def scoree():
    global score1
    score1 += current_boost
    score.setText(str(score1))


    if score1 >= 500:
        pixmap = QPixmap("imageeeee.jpg")
        area.setIcon(QIcon(pixmap))
        area.setIconSize(pixmap.size())
        area.setStyleSheet("text-align: center;")

    if score1 >= 1500:
        pixmap = QPixmap("golub.jpg")
        area.setIcon(QIcon(pixmap))
        area.setIconSize(pixmap.size())
        area.setStyleSheet("text-align: center;")

    



def upgrade_clicked():
    global current_boost, score1
    if score1 >= 100:
        score1 -= 100
        current_boost += 1
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade2_clicked():
        global current_boost, score1
        if score1 >= 500:
            score1 -= 500
            current_boost += 5
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade3_clicked():
        global current_boost, score1
        if score1 >= 1250:
            score1 -= 1250
            current_boost += 10
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade4_clicked():
        global current_boost, score1
        if score1 >= 3000:
            score1 -= 3000
            current_boost += 15
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade5_clicked():
        global current_boost, score1
        if score1 >= 7500:
            score1 -= 7500
            current_boost += 25
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade6_clicked():
        global current_boost, score1
        if score1 >= 15000:
            score1 -= 15000
            current_boost += 50
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade7_clicked():
    global current_boost, score1
    if score1 >= 35000:
        score1 -= 35000
        current_boost += 100
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade8_clicked():
    global current_boost, score1
    if score1 >= 70000:
        score1 -= 70000
        current_boost += 250
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade9_clicked():
    global current_boost, score1
    if score1 >= 150000:
        score1 -= 150000
        current_boost += 500
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade10_clicked():
    global current_boost, score1
    if score1 >= 0:
        score1 -= 0
        current_boost += 1500
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")









def upgrade_clicked_2():
    global current_boost2, score2
    if score2 >= 150:
        score2 -= 150
        current_boost2 += 5
        score2_text.setText(str(score2))
        boost_text2.setText(f"Сила кліку: {current_boost2}")

def upgrade2_clicked_2():
    global current_boost2, score2
    if score2 >= 450:
        score2 -= 450
        current_boost2 += 20
        score2_text.setText(str(score2))
        boost_text2.setText(f"Сила кліку: {current_boost2}")

def upgrade3_clicked_2():
    global current_boost2, score2
    if score2 >= 2500:
        score2 -= 2500
        current_boost2 += 150
        score2_text.setText(str(score2))
        boost_text2.setText(f"Сила кліку: {current_boost2}")

def upgrade4_clicked_2():
    global current_boost2, score2
    if score2 >= 15000:
        score2 -= 15000
        current_boost2 += 1250
        score2_text.setText(str(score2))
        boost_text2.setText(f"Сила кліку: {current_boost2}")

def upgrade5_clicked_2():
    global current_boost2, score2
    if score2 >= 125000:
        score2 -= 125000
        current_boost2 += 15000
        score2_text.setText(str(score2))
        boost_text2.setText(f"Сила кліку: {current_boost2}")

def upgrade6_clicked_2():
    global current_boost2, score2
    if score2 >= 4500000:
        score2 -= 4500000
        current_boost2 += 150000
        score2_text.setText(str(score2))
        boost_text2.setText(f"Сила кліку: {current_boost2}")

def upgrade7_clicked_2():
    global current_boost2, score2
    if score2 >= 20000000:
        score2 -= 20000000
        current_boost2 += 1000000
        score2_text.setText(str(score2))
        boost_text2.setText(f"Сила кліку: {current_boost2}")

def upgrade8_clicked_2():
    global current_boost2, score2
    if score2 >= 150000000:
        score2 -= 150000000
        current_boost2 += 10000000
        score2_text.setText(str(score2))
        boost_text2.setText(f"Сила кліку: {current_boost2}")

def upgrade9_clicked_2():
    global current_boost2, score2
    if score2 >= 1000000000:
        score2 -= 1000000000
        current_boost2 += 100000000
        score2_text.setText(str(score2))
        boost_text2.setText(f"Сила кліку: {current_boost2}")

def upgrade10_clicked_2():
    global current_boost2, score2
    if score2 >= 10000000000:
        score2 -= 10000000000
        current_boost2 += 2000000000
        score2_text.setText(str(score2))
        boost_text2.setText(f"Сила кліку: {current_boost2}")


tap2_zona.clicked.connect(score_2)
leave_zona2.clicked.connect(leave_level_2)
leave_setting.clicked.connect(setting_leave)
slider.valueChanged.connect(music_editor)
setting.clicked.connect(setting_window)
button_leave.clicked.connect(leave)
area.clicked.connect(scoree)
upgrade.clicked.connect(upgrade_clicked)
upgrade2.clicked.connect(upgrade2_clicked)
upgrade3.clicked.connect(upgrade3_clicked)
upgrade4.clicked.connect(upgrade4_clicked)
upgrade5.clicked.connect(upgrade5_clicked)
upgrade6.clicked.connect(upgrade6_clicked)
upgrade7.clicked.connect(upgrade7_clicked)
upgrade8.clicked.connect(upgrade8_clicked)
upgrade9.clicked.connect(upgrade9_clicked)
upgrade10.clicked.connect(upgrade10_clicked)
window2_push_button.clicked.connect(start_game)
window3_push_button.clicked.connect(level2)
upgrade_2.clicked.connect(upgrade_clicked_2)
upgrade2_2.clicked.connect(upgrade2_clicked_2)
upgrade3_2.clicked.connect(upgrade3_clicked_2)
upgrade4_2.clicked.connect(upgrade4_clicked_2)
upgrade5_2.clicked.connect(upgrade5_clicked_2)
upgrade6_2.clicked.connect(upgrade6_clicked_2)
upgrade7_2.clicked.connect(upgrade7_clicked_2)
upgrade8_2.clicked.connect(upgrade8_clicked_2)
upgrade9_2.clicked.connect(upgrade9_clicked_2)
upgrade10_2.clicked.connect(upgrade10_clicked_2)


upgrade.setStyleSheet("background-color: blue;")
upgrade_sell.setStyleSheet("background-color: yellow;")
upgrade2.setStyleSheet("background-color: blue;")
upgrade2_sell.setStyleSheet("background-color: yellow;")
upgrade3.setStyleSheet("background-color: blue;")
upgrade3_sell.setStyleSheet("background-color: yellow;")
upgrade4.setStyleSheet("background-color: blue;")
upgrade4_sell.setStyleSheet("background-color: yellow;")
upgrade5.setStyleSheet("background-color: blue;")
upgrade5_sell.setStyleSheet("background-color: yellow;")
upgrade6.setStyleSheet("background-color: blue;")
upgrade6_sell.setStyleSheet("background-color: yellow;")
upgrade7.setStyleSheet("background-color: blue;")
upgrade7_sell.setStyleSheet("background-color: yellow;")
upgrade8.setStyleSheet("background-color: blue;")
upgrade8_sell.setStyleSheet("background-color: yellow;")
upgrade9.setStyleSheet("background-color: blue;")
upgrade9_sell.setStyleSheet("background-color: yellow;")
upgrade10.setStyleSheet("background-color: blue;")
upgrade10_sell.setStyleSheet("background-color: yellow;")
name_of_game_menu.setStyleSheet("font-size: 50px")
window.setStyleSheet("background-color: lightgreen;")
button_leave.setStyleSheet("background-color: red;")
window3_push_button.setStyleSheet("background-color: grey;")
window3_sell.setStyleSheet("background-color: grey;")



menu_window.show()
app.exec_()