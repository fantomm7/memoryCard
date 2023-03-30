#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint 

class Vopros():
    def __init__(self, q, r, w, ww, www):
        self.q = q
        self.r = r
        self.w = w
        self.ww = ww
        self.www = www
app = QApplication([])
mw = QWidget()
mw.setWindowTitle("Memorя card")
mw.resize(500, 500)
mw.show()
vlist = []
vlist.append(Vopros("На каком языке говорят в Пруксии?", "Нет такой страны!", "Азербайджанском", "Лунгском", "Русском"))
vlist.append(Vopros("2*x=8", "x=1200/300", "x=0.75", "x=1/8", "x=3.99"))
vlist.append(Vopros("Если в стакан воды кинуть маленький кусочек льда, вода замёрзнет?", "Охладится", "Всё превратится в лёд", "Лёд растает", "хз"))
vlist.append(Vopros("Ты солнышко?", "да", "нет", "нет", "нет"))
vlist.append(Vopros("А.С.Пушкин родился в Питере", "неправда", "правда", "В Новосибирске", "в Пруссии"))
vlist.append(Vopros("Егор молодец)", "да", "неправильно", "нет", "и это тоже нет!"))
vlist.append(Vopros("5*x=y, если", "y=5x", "x=y", "y=2x", "y=5/x"))

q = QLabel("тут должОн быть вопрос")
gr1 = QGroupBox("варианты")
an1 = QRadioButton("111111")
an2 = QRadioButton("222222")
an3 = QRadioButton("333333")
an4 = QRadioButton("444444")
mbtn = QPushButton("Ответить")

gr11 = QButtonGroup()
gr11.addButton(an1)
gr11.addButton(an2)
gr11.addButton(an3)
gr11.addButton(an4)

l0 = QVBoxLayout()
l1 = QHBoxLayout() 
l2 = QHBoxLayout()

l1.addWidget(an1, alignment = Qt.AlignCenter)
l1.addWidget(an2, alignment = Qt.AlignCenter)
l2.addWidget(an3, alignment = Qt.AlignCenter)
l2.addWidget(an4, alignment = Qt.AlignCenter)

l0.addLayout(l1)
l0.addLayout(l2)
gr1.setLayout(l0)

gr2 = QGroupBox("итог")
res = QLabel("Правильно/Неправильно")
good = QLabel("Правильный ответ")

l4 = QVBoxLayout()
l4.addWidget(res, alignment = Qt.AlignTop)
l4.addWidget(good, alignment = Qt.AlignCenter)
gr2.setLayout(l4)
gr2.hide()

def check():
    if mbtn.text()=="Ответить":
        isRight()
    else:
        sledVoprTwo()

an = [an1, an2, an3, an4]

def sledVopr():
    mbtn.setText("Ответить")
    gr1.show()
    gr2.hide() 
    gr11.setExclusive(False)
    an1.setChecked(False)
    an2.setChecked(False)
    an3.setChecked(False)
    an4.setChecked(False)
    gr11.setExclusive(True)

v = Vopros("Вопрос", "1", "2", "3", "4")

def ask(vv: Vopros):
    shuffle(an)
    an[0].setText(vv.r)
    an[1].setText(vv.w)
    an[2].setText(vv.ww)
    an[3].setText(vv.www)
    q.setText(vv.q)
    good.setText(vv.r)
    sledVopr()

def isRight():
    if an[0].isChecked():
        res.setText("маладэс")
        otvetil()
    else:
        if an[1].isChecked() or an[2].isChecked() or an[3].isChecked():
            res.setText("не маладэс")
            otvetil()
    

def otvetil():
    mbtn.setText("Следующий вопрос")
    gr1.hide()
    gr2.show()

def sledVoprTwo():
    voprRand =randint(0, len(vlist)-1) 
    vvv = vlist[voprRand]
    ask(vvv)


mbtn.clicked.connect(check)
ml = QVBoxLayout()
ml.addWidget(q, alignment = Qt.AlignCenter)
ml.addWidget(gr1, alignment = Qt.AlignCenter)
ml.addWidget(gr2, alignment = Qt.AlignCenter)
ml.addWidget(mbtn, alignment = Qt.AlignCenter)
mw.setLayout(ml)
app.exec()