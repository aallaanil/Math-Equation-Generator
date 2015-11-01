import random
from Tkinter import *


max = [10,100,1000] #max number generated
numDec1= 0 #number of decimals to round to for the first number
theOperators = ["+", "-", "x", "/"]
percentMode = True

#Class for the window display
class Window (Tk):	

	def __init__ (self):
		Tk.__init__(self)
		self.title("Math Generator")
		self.canvas = Canvas(self)
		self.canvas.pack(fill=BOTH, expand=1)
		self.button = Button(self, text = "New Equation", command = self.displayEquation)
		self.button.pack(side="bottom", fill='both', expand=False, padx=50, pady=20)

	def displayEquation(self):
		self.canvas.delete("all")
		theStr = genEquation(percentMode)
		self.canvas.create_text(110, 150, font = ("Arial", 20), anchor = W, text = theStr)

#Generates a random equation		
def genEquation (percentMode):
	#Generate the first number
	#firstNum = random.random()*max[random.randrange(len(max))]
	firstNum = random.uniform(1, 100)
	
	#Generate the second number
	if percentMode:
		secondNum = random.random()
		numDec2 = 2
		
	else:
		#secondNum = random.random()*max[random.randrange(len(max))]
		secondNum = random.uniform(1, 100)
		numDec2 = numDec1
	
	#Generate a random operator
	if percentMode:
		theOperator = "x"
	else:	
		theOperator = theOperators[random.randrange(len(theOperators))]
	
	#Generate the equation
	theStr = str(round(firstNum,numDec1)) + " " + theOperator + " " + str(round(secondNum, numDec2)*100) + "%"
	return theStr
	

#Run	
root = Window()
root.mainloop()
