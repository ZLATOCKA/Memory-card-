#создай приложение для запоминания информацииfrom PyQt5.QtCore import Qt 
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self,question1, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1    
        self.wrong2 = wrong2
        self.wrong3 = wrong3

#создание приложения и главного окна
def show_question():
    button.setText("Ответить")
    ansGroupDox.hide()
    RadioGroupBox.show()
    

    RadioGroup.setExclusive(False)    
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)


def show_result():
    button.setText("Следующий вопрос")
    ansGroupDox.show()
    RadioGroupBox.hide()

def next_question():
    main_win.total+=1
    print("Статистика\n" + "Всего вопросов:" + str(main_win.total) + "\nПравильных ответов:" + str(main_win.score))
    cur_question = randint(0, len(question_list) - 1)
    if cur_question >= len(question_list):
        cur_question = 0
    q = question_list[cur_question]
    ask(q)



def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question1)
    answer2.setText(q.right_answer)
    show_question()

def show_correct(res):
    answer1.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно")
        main_win.score+=1
        print("Статистика\n" + "Всего вопросов:" + str(main_win.total) + "\nПравильных ответов:" + str(main_win.score))
        print("Рейтинг:" ,main_win.score/main_win.total*100)
    else:
        show_correct("Неправильно")
        print("Неверно")
        print("Рейтинг:" ,main_win.score/main_win.total*100)


def clic_OK():
    if button.text() == "Ответить":
        check_answer()
    else:
        next_question()



app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle("Memory Card")
main_win.resize(600,400)


RadioGroupBox = QGroupBox("Варианты ответов")
question = QLabel('Какой национальност не существует?')
btn_answer1 = QRadioButton("Энцы")
btn_answer2 = QRadioButton("Смурфы")
btn_answer3 = QRadioButton("Чулымцы")
btn_answer4 = QRadioButton("Алеуты")
button = QPushButton("Ответить")

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]    

hl = QHBoxLayout()
hl.addWidget(btn_answer1)
hl.addWidget(btn_answer2)

hl2 = QHBoxLayout()
hl2.addWidget(btn_answer3)
hl2.addWidget(btn_answer4)

RadioGroup = QButtonGroup() 
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

layout_main = QVBoxLayout()
layout_main.addLayout(hl)
layout_main.addLayout(hl2)
RadioGroupBox.setLayout(layout_main)
RadioGroupBox.show()


ansGroupDox = QGroupBox("Результат теста")
answer1 = QLabel('Правильно/Неправильно')
answer2 = QLabel('Правильный ответ')


v_l = QVBoxLayout()
v_l.addWidget(answer1)
v_l.addWidget(answer2)
ansGroupDox.setLayout(v_l)
ansGroupDox.hide()
vline = QVBoxLayout()
vline.addWidget(question)
vline.addWidget(RadioGroupBox)
vline.addWidget(ansGroupDox)
vline.addWidget(button)

main_win.setLayout(vline)

main_win.score = 0
main_win.total = 0
question_list = []

q4 = Question


q1 = Question("В каком лицее учился А.С.Пушкин?","Царскосельский лицей", "Благородный пансион при Московском университете",  "Казанский университет", "Муз. училище им. Горьгоко")
q2 = Question("Год написания Капитанской дочки?", "1836", "1867","1863","1863")
question_list.append(q1)
q = Question("В каком году умер писатель А.С.Пушкин?", "1837", "1937", "1838", "1873")
question_list.append(q2)
question_list.append(q)

button.clicked.connect(clic_OK)
next_question()





main_win.show()
app.exec_()















