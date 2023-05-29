# Найти сумму цифр трехзначного числа
print("Введите трехзначное число")
n = int(input())
sum=0
if 999>=n>=100:
    while n>0:
        sum+=n%10
        n//=10
print(f"Сумма цифр числа равна {sum}")

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
print("Введите общее количество журавликов")
S = int(input())
if S%6!=0: print("Общее количество должно быть кратно 6ти. Ответ для введенного числа приведен с округлением")
PS = S//6
K = PS*4
print(f"Петя и Сережа сделали по {PS}, Катя сделала {K}")

# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
print("Введите шестизначное число")
num = int(input())
sum_1=0
sum_2=0
if 999999>=num>=100000:
    while num>1000:
        sum_1+=num%10
        num//=10
    while num>0:
        sum_2+=num%10
        num//=10
else: print("Некорректный ввод")
if sum_1==sum_2: print("Да")
else: print("Нет")

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
print("Введите количество долек первой стороны шоколадки")
n = int(input())
print("Введите количество долек второй стороны шоколадки")
m = int(input())
print("Введите количество долек, которое необходимо отделить одним разломом")
k = int(input())
if k%n==0 or k%m==0 and k<=m*n:
    print("Можно")
else:
    print("Нельзя")