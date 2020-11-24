from turtle import *

colormode(255)
woerterbuch = {'I':'Ich', 'You':'Du', 'We':'Wir', 'Like':'mögen', 'Love':'lieben', 'eat':'essen', 'Cake':'Kuchen', 'Apple':'Apfel'}


# create inverted dictionary
def invert(olddict):
    newdict = {}
    for item in olddict.items():
        newdict[item[1]] = item[0]
    return newdict


# append german grammatical cases
def appendcases(dictionary, key, value):
    dictionary[key] = value
    return dictionary


# translate sentence
def translate(sentence, dictionary):
    translated_list = []
    sentence = sentence.split()
    for word in sentence:
        word = word.lower()
        translated_list.append(dictionary[word])
    translated_sentence = " ".join(translated_list)
    return(translated_sentence)


# paint heart and replay
def paintheart(sentence):
    sentence = sentence.split()
    if sentence[0] == "I":
        fillcolor("red")
        pencolor("red")
        begin_fill()
        setheading(90)
        forward(120)
        left(45)
        circle(50,180)
        goto(0, 0)
    if sentence[1] == "Love":
        setheading(90)
        forward(120)
        right(225)
        circle(50,-180)
        goto(0, 0)
    if sentence[2] == "You":
        end_fill()
        hideturtle()
        sentence = " ".join(sentence)
    sentence += str(" Too, Honey")
    penup()
    goto(0, 80)
    color(41,253,41)
    style = ('Verdana', 18, 'bold italic')
    write(sentence, font=style, align='center')
    

woerterbuch = invert(woerterbuch)
appendcases(woerterbuch, "ich", "I")
appendcases(woerterbuch, "liebe", "Love")
appendcases(woerterbuch, "dich", "You")
#appendcases(woerterbuch, "Liebe", "Love")

sayIt = textinput("Hello Darling", "Please Type: 'Ich Liebe Dich' ")
listen()

confession = translate(sayIt, woerterbuch)
paintheart(confession)




done()

