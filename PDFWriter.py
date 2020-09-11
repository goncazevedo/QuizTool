from fpdf import FPDF
from Question import Question
from random import randint


def quizGen(questions, theme, dificulty):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial","", 10)
    i = 1
    for q in questions:
        writeQuestion(q, i, pdf)
        i+=1
    pdf.output("quizzes/quiz_{}_{}.pdf".format(dificulty,theme),"F")
    

def writeQuestion(question, number, pdf):
    pdf.write(3, "{}({})- {}\n".format(number,question.dificulty, question.title))
    options  = question.options.copy()
    while options:
        i = randint(0, len(options)-1)
        if options[i].correct:
            pdf.set_font("Arial","B", 10)
        pdf.write(3, "( ){}\n".format(options.pop(i).answer))
        pdf.set_font("Arial","", 10)
    pdf.write(3,"\n")


