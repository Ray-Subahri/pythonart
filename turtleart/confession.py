from turtle import *

woerterbuch = {'I':'Ich', 'You':'Du', 'We':'Wir', 'Like':'mögen', 'Love':'lieben', 'eat':'essen', 'Cake':'Kuchen', 'Apple':'Apfel'}

# create inverted dictionary
def invert(olddict):
    newdict = {}
    for item in olddict.items():
        newdict[item[1]] = item[0]
    return newdict

# translate sentence
def translate(sentence, dictionary):
    translated_list = []
    sentence = sentence.split()
    for word in sentence:
        translated_list.append(dictionary[word])
    translated_sentence = " ".join(translated_list)
    return(translated_sentence)

# append german grammatical cases
def appendcases(dictionary, key, value):
    dictionary[key] = value
    return dictionary

# paint heart and print "I Love You"
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
        print(sentence)
    


woerterbuch = invert(woerterbuch)
appendcases(woerterbuch, "dich", "You")
appendcases(woerterbuch, "liebe", "Love")
confession = translate("Ich liebe dich", woerterbuch)
paintheart(confession)

done()

