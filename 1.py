# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


# n = int(input('введите количество монет'))
# count0 = 0
# count1 = 0
# for i in range(n):
#     temp = int(input())
#     if temp == 0:
#         count0+ = 1
#     else:
#         count1+ =  1
# if count0 > count1:
#     print(f"Надо перевернуть {count1} монет")
# else:
#     print(f"Надо перевернуть {count0} монет")



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.


# s = int(input('введите s'))
# p = int(input('введите p'))
# for i in range(1, s):
#     for j in range(1, p):
#         if i+j==s and i*j==p:
#             print(i,j)
        
           



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.


# n = int(input('введите N'))
# st = 0
# while 2 ** st < n:
#     print(2 ** st, end=" ")
#     st+=1