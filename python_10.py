listem1 = [1,2,3,4]
listem2 = [3,34,5,6]
listem3 = ['a', 'b', 'c', 'd']

list(zip(listem1, listem2))

list(zip(listem1, listem2, listem3))

listem1 = [1,2,3,4,5,6,7,8]
listem2 = [3,34,5,6]
listem3 = ['a' , 'b', 'c', 'd']
list(zip(listem1,listem2,listem3))

# input('Yes veya No giriniz: ') == 'yes'

# input('Yes veya No giriniz: ') == 'yes'

# input('Yes veya No giriniz: ').lower() == 'yes' 

# input('Yes veya No giriniz: ').lower() == 'yes'

# input('Yes veya No giriniz: ').lower() == 'yes'

# input('Yes veya No giriniz: ').lower().strip() == 'yes'

# sonuc = input('Yes veya No giriniz: ').lower().strip() == 'yes'
# print(f'Your Entered {sonuc}')

# sonuc = input('Yes veya No giriniz: '). lower() . strip() == 'yes'
# print(f'Your Entered {sonuc}')

# convert = input("Enter Yes or No : ").title().strip() == "Yes"
# print("You entered", convert)

# print(f"Your Entered {input('Yes veya No giriniz: '). lower().strip() == 'yes'}")

course = 'clarusway'
if course == "clarusway":
    print("you guaranteed the job")
else:
    print("think about it again")

sayi = 5
if sayi < 10 :
    print('Sayi 10 dan kucuk')
else :
    print('Sayi 10 dan kucuk degil') 

sayi = 15
if sayi < 10 :
    print('Sayi 10 dan kucuk')
else :
    print('Sayi 10 dan kucuk degil')

# acemilerin yazisi
b_degeri = True
if b_degeri == True: 
    print('Deger True')
else:
    print('deger FAlse')

# acemilerin yazisi
b_degeri = False
if b_degeri == True:
    print('Deger True')
else:
    print('deger FAlse')

b_degeri = False
if b_degeri:
    print('Deger True')
else:
    print('deger FAlse')    

b_degeri = True
if b_degeri:
    print('Deger True')
else:
    print('deger FAlse')

number = 5
if number <= 3:
    print("Number is smaller than or equal to 3")
else: # Optional clause (you can only have one else)
    print("Number is bigger than 3")

course = 'clarusway'
if course == "clarusway":
    print("you guaranteed the job")
else:
    print("think about it again")

# number = int(input("please enter a number: "))
# if number % 2 == 0:
#     print("your number is even")
# else:
#     print("your number is odd")

numb = 3
if numb % 2 :
    print(f'{numb} is even')
else :
    print(f'{numb} is odd')

# x = int(input("Enter a number please:"))
# if x%2 == 0 :
#     print(x, "is even")
# else :
#     print(x,"is odd")

# girdi = int(input('Bir tamsayi giriniz : '))
# if girdi % 2 == 0:
#     print(f'Girdiginiz sayi olan {girdi} cifttir.')
# else:
#     print(f'Girdiginiz sayi olan {girdi} tektir.')

5.0 % 2

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#     print("{0} is Even".format(num))
# else:
#     print("{0} is Odd".format(num))

# girdi = int(input('Bir tamsayi giriniz : '))
# if girdi % 2 == 0:
#     print(f'Girdiginiz sayi olan {girdi} cifttir.')
# else:
#     print(girdi , 'sayisi tektir')

# girdi = int(input('Bir tamsayi giriniz : '))
# if girdi>0:
#     print('Pozitif Sayi')
# else :
#     print('negatif sayi')

# num = float(input("Enter a number: "))
# if num > 0:
#     print("Positive number")
# else:
#     print("Negative number")

num1 = 4
num2 = 5
if num1<num2 :
    print(f'Buyuk olan sayi {num2}')
else:
    print(f'Buyuk olan sayi {num1}')

num1 = 4
num2 = 5
if num1<num2 :
    buyuk = num2
else:
    buyuk = num1
print('buyuk olan sayi',buyuk)

# sayilar = input('Iki sayiyi aralarında virgul olacak sekilde giriniz')
# sayilar

# sayilar = input('Iki sayiyi aralarında virgul olacak sekilde giriniz').split(',')
# sayilar

# sayilar = input('Iki sayiyi aralarında virgul olacak sekilde giriniz').split(',')
# sayi1 = sayilar[0]
# sayi1

# sayilar = input('Iki sayiyi aralarında virgul olacak şekilde giriniz'). split(',')
# sayi1 = int(sayilar[0])
# sayi1

# sayilar = input('Iki sayiyi aralarında virgul olacak sekilde giriniz').split(',')
# sayi1 = int(sayilar[0])
# sayi2 = int(sayilar[1])
# if sayi1<sayi2 :
#     buyuk = sayi2
# else:
#     buyuk = sayi1
# print('buyuk olan sayi', buyuk)

# num1 = float(input("Enter first number:"))
# num2 = float(input("Enter second number:"))
# if (num1 > num2) :
#     larger = num1
# else:
#     larger = num2
# print("The large number is", larger)

bool_deger = True
if bool_deger:
    print('Yes')
else:
    print('Nope')

bool_value = False # can be True or False
if bool_value:
    print("Yes")
else :
    print("No")

audience = "baby"
if audience == "kid":
    print("it is free to go to cinema")
elif audience == "teen":
    print("discounted price!")
elif audience == "adult":
    print("normal price")
else:
    print("No such audience, stay at your home!")

# number_1 = int(input("Enter the number 1: "))
# number_2 = int(input("Enter the number 2: "))
# number_3 = int(input("Enter the number 3:"))
# numbers = (number_1, number_2, number_3)
# print(max(numbers))

sayi1 = 9
sayi2 = 8
sayi3 = 7
if sayi1 > sayi2 and sayi1 > sayi3:
    print('En buyuk sayi ', sayi1)
elif sayi2 > sayi1 and sayi2 > sayi3:
    print('En buyuk sayi ', sayi2)
else:
    print('En buyuk sayi ', sayi3)

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# if (num1 >= num2) and (num1 >= num3):
#     largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#     largest = num2
# else:
#     largest = num3
# print("The largest number is", largest)

# sayi = int(input('Bir sayi giriniz'))
# if sayi>0:
#     print('pozitif')
# elif sayi<0 :
#     print('Negatif')
# else:
#     print('Sifir')

# sayi = int(input('Bir sayi giriniz'))
# if sayi>0:
#     print('pozitif')
# if sayi<0 :
#     print('Negatif')
# if sayi == 0:
#     print('Sifir')

# sayi = int(input('Notunu yaz'))
# if sayi>80:
#     print('Aferin')
# elif sayi >60 :
#     print('iyi')
# elif sayi>40 :
#     print('Calis')
# else:
#     print('gecmis olsun')

# sayi = int(input('Notunu yaz'))
# if sayi>80:
#     print( 'Aferin')
# if sayi >60 :
#     print('iyi')
# if sayi>40 :
#     print('Calis')
# if sayi <= 40:
#     print('gecmis olsun')

# num = float(input("Enter a number: "))
# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")

audience_group = 'kid', 'teen', 'adult'
audience = "teen"
if audience in audience_group:
    if audience == "kid":
        print("it is free to go to cinema")
    elif audience == "teen":
        print("discounted price!")
    else: # audience == "adult":
        print("normal price")
else:
    print("No such audience, stay at your home!")

# score = int (input("Enter your score :"))
# if score >= 90:
#     if score >= 95:
#         Score_letter="A+"
#     else:
#         Score_letter="A"
# elif score >= 80:
#     if score >= 85:
#         Score_letter="B+"
#     else:
#         Score_letter="B"
# else:
#     Score_letter="below B"
# print ("Your degree: %s" % Score_letter)

# girdi = input('Istediğin kadar sayiyi aralarina bosluk birakarak yaz. ').split()
# girdi
# sayilar = list(map(int,girdi))
# sayilar
# print(f'En buyuk sayi {max(sayilar) }')

a = {1,2,3}

a = set('warning' )
b = set('bearing' )
print(a - b)

type( {})

a = set('warning')
b = set('bearing')
print(a.difference(b))

a = set('warning')
b = set('bearing' )
print(b.difference(a))

a = set( 'warning' )
b = set( 'bearing' )
print(b - a)

number = 0
while number < 6:
    print(number)
    number += 1
print('now, number is bigger or equal to 6')

my_list=["a", "b", "c", "d", "e"]
a = 0
while a < len(my_list) :
    print('square of {} is : {}' .format(a, a ** 2))
    a+=1