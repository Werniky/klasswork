import random

##1
#a = int(input("Введите первое число: ")) 
#b = int(input("Введите второе число: ")) 
#c = int(input("Сумма этих чисел: ")) 
#if a+b==c: 
#        print("Ответ верный!") 
#else: 
#        print("Здесь ошибка!")

##2
#a = random.randint(1,10)
#print("загаданное число",a)
#t = int(input("Я загадал число, угадывай"))
#if t == a:
#    print("Угадал")
#else:
#    print("Не угадал")

##3
#a = "На улице идёт дождь?"
#b = "Пошёл дождь, Возьмите зонтик!"
#c = "Все хорошо можно без него"
#print(b if int(input(a))==1 else c)

##4
#a = int(input("Баллы по русскому"))
#b = int(input("Баллы по математике"))
#c = int(input("Баллы по информатеке"))
#if a + b + c != 270:
#    print ("Не поступил") 
#else:
#    print ("Все ок")

##5
a=int(input("Какое число?"))
if a % 2 == 0 :
    print("чисти")
else:
    print("не чисти")