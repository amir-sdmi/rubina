num1 = int(input ("type in one number: "))
op = input ("Type in: *, -, / , % ,or *: ")
num2 = int(input ("Type in a secont number: "))
answer = 0
if op == '*' :
    answer = num1*num2
elif op == '+':
    answer = num1+num2
elif op == "/":
    answer = num1/num2
elif op == "-":
    answer = num1-num2
elif op == '%':
    answer = num1%num2
else :
    print ("this is not correct!")

print ("This is the answer: " + str(answer))

