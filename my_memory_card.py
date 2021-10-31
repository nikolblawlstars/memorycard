from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle
from random import randint

class Question():
    def __init__(self,question, right_aswer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_aswer = right_aswer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Столица Японии?', 'Токио', 'Шанхай','Киев','Пиза'))
question_list.append(Question('Столица Италии?', 'Рим', 'Милан','Венеция','Нефполь'))
question_list.append(Question('Столица Франции?', 'Париж', 'Лондон','Мадрид','Берлин'))


app = QApplication([])


window = QWidget()
window.setWindowTitle('Party Card')

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Столица США?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вашингтон')
rbtn_2 = QRadioButton('Нью Йорк')
rbtn_3 = QRadioButton('Лос-Анжелес')
rbtn_4 = QRadioButton('Лас Вегас')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)



layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout() 

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)

layout_line3.addWidget(btn_OK, stretch = 3)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) 

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q:Question):

    shuffle(answers)
    answers[0].setText(q.right_aswer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_aswer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():

    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score +=1
        print("Статистика\n=Всего вопросов: ",window.total, "\n=Правильных ответов: ", window.score)
        print("Рейтинг: ", (window.score/window.total * 100), "%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print("Рейтинг: ", (window.score/window.total * 100), "%")
def next_question():
    window.total +=1
    print("Статистика\n=Всего вопросов: ",window.total, "\n=Правильных ответов: ", window.score)
    cur_question = randint(0, len(question_list) - 1) 
    q = question_list[cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.setLayout(layout_card)
window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.show()
window.setStyleSheet('background-color: #86bf96')
btn_OK.setStyleSheet('background-color: #96d6d6')
window.resize(350,350)
app.exec()