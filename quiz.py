from Question import Question
from Option import Option
from collections import defaultdict
from random import randint
import PDFWriter
import xlrd

def sheetReader(sheet):    
    themes = []
    questions = {}
    qs = []
    ptheme = ""
    for i in range(1,sheet.nrows):
        row =  sheet.row_values(i)
        opts = []
        for i in range(1,5):
            if i == 4:
                op = Option(row[i], True)
            else:
                op = Option(row[i], False)
            opts.append(op)
        if row[6] not in themes: 
            themes.append(row[6])
        if row[6] != ptheme:
            qs = []
        qs.append(Question(row[0],row[5],opts))
        questions[row[6]] = qs
        ptheme = row[6]
    return [questions, themes]

def questionSelection(questions, d):
    if d == "f":
        return dificultySeparator(6,4,0,questions)
    elif d == "m":
        return dificultySeparator(3,6,1,questions)
    elif d == "d":
        return dificultySeparator(0,4,6,questions)


def dificultySeparator(f, m, d, questions):
    resp = []
    qs = questions.copy()
    while qs or len(resp)>10:
        i = randint(0, len(qs)-1)
        aux = qs.pop(i)
        if (aux.dificulty == "f" and f>0) or (aux.dificulty == "m" and m>0) or (aux.dificulty == "d" and d>0):
            resp.append(aux)
    return resp



wb = xlrd.open_workbook("Perguntas.xlsx") 
sheet = wb.sheet_by_index(0) 

questions, themes = sheetReader(sheet)

menu = ""
while menu != "n":
    for i in range(len(themes)):
        print("\t{}-{}".format(i, themes[i]))
    t = int(input("Selecione o tema do quiz: "))

    d = input("\n\tf-facil\n\tm-medio\n\td-dificil\nSelecione a dificuldade do quiz: ")

    aux = questions[themes[t]]

    quiz = questionSelection(aux, d)

    while len(quiz)<10:
        print("\nNão existem perguntas suficientes para a dificuldade escolhida!")
        d = input("\tf-facil\n\tm-medio\n\td-dificil\nPor favor selecione outra dificuldade: ")
        quiz = questionSelection(aux, d)


    PDFWriter.quizGen(quiz, themes[t], d)
    print("\nO quiz sobre {} foi gerado com sucesso!\n".format(themes[t]))
    menu = input("Deseja gerar outro quiz?(s/n)\n")
    
    


