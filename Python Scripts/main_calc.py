from calc import*
expression = []

def push9():
	expression.append('9')
	ui.label.setText("".join(expression))
def push8():
	expression.append('8')
	ui.label.setText("".join(expression))
def push7():
	expression.append('7')
	ui.label.setText("".join(expression))
def push6():
	expression.append('6')
	ui.label.setText("".join(expression))
def push5():
	expression.append('5')
	ui.label.setText("".join(expression))
def push4():
	expression.append('4')
	ui.label.setText("".join(expression))
def push3():
	expression.append('3')
	ui.label.setText("".join(expression))
def push2():
	expression.append('2')
	ui.label.setText("".join(expression))
def push1():
	expression.append('1')
	ui.label.setText("".join(expression))
def push0():
	expression.append('0')
	ui.label.setText("".join(expression))

def pushadd():
	expression.append('+')
	ui.label.setText("".join(expression))
def pushminus():
	expression.append('-')
	ui.label.setText("".join(expression))
def pushmul():
	expression.append('x')
	ui.label.setText("".join(expression))
def pushdiv():
	expression.append('/')
	ui.label.setText("".join(expression))
def pushmod():
	expression.append('%')
	ui.label.setText("".join(expression))
def pushpower():
	expression.append('^')
	ui.label.setText("".join(expression))


def pushAC():
	expression = []
	ui.label.setText("".join(expression))
def pushdel():
	try:
		expression.pop()
		ui.label.setText("".join(expression))
	except:
		pass
def pushpoint():
	expression.append('.')
	ui.label.setText("".join(expression))
def pushequal():
	global expression
	print()
	try:
		while('^' in expression):
			index = expression.index('^')
			expression[index] = '**'
		while('x' in expression):
			index = expression.index('x')
			expression[index] = '*'

		expression = "".join(expression)
		value = eval(expression)
		expression = [str(value)]
	except:
		expression = ['Error']
	ui.label.setText("".join(expression))

import sys
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

ui.label.setText("0")

ui.pushButton_9.clicked.connect(lambda:push9())
ui.pushButton_8.clicked.connect(lambda:push8())
ui.pushButton_7.clicked.connect(lambda:push7())
ui.pushButton_6.clicked.connect(lambda:push6())
ui.pushButton_5.clicked.connect(lambda:push5())
ui.pushButton_4.clicked.connect(lambda:push4())
ui.pushButton_3.clicked.connect(lambda:push3())
ui.pushButton_2.clicked.connect(lambda:push2())
ui.pushButton_1.clicked.connect(lambda:push1())
ui.pushButton_0.clicked.connect(lambda:push0())


ui.pushButton_power.clicked.connect(lambda:pushpower())
ui.pushButton_mod.clicked.connect(lambda:pushmod())
ui.pushButton_div.clicked.connect(lambda:pushdiv())
ui.pushButton_mul.clicked.connect(lambda:pushmul())
ui.pushButton_minus.clicked.connect(lambda:pushminus())
ui.pushButton_add.clicked.connect(lambda:pushadd())

ui.pushButton_point.clicked.connect(lambda:pushpoint())
ui.pushButton_del.clicked.connect(lambda:pushdel())
ui.pushButton_AC.clicked.connect(lambda:pushAC())
ui.pushButton_equal.clicked.connect(lambda:pushequal())

Form.show()
sys.exit(app.exec_())

print("Done")