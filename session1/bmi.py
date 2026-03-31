#age = input ("Wie alt bist du? :")
weight = float(input ("Wie schwer bist du? :"))
height = float(input ("Wie groß bist du? :"))
#bmi = somethinge like an caculator, that doctors use.
bmi = weight/(height*height)
print('your bmi is : ' + str(bmi))


if bmi<18.5:
    print('du bist dünn')
elif bmi>25:
    print("du bist fett")
else :
    print("Du bist normal")