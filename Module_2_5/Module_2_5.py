# #Defauly function
# from platform import win32_ver
#
#
# def say_helo(name):
#     name = []
# name = input('Write your dumb friends: ')
# print(name)
#
# #returnable function
# import random
# def random_number():
#     numbers = [1, 2]
#     decision = random.choice(numbers)
#     your_number = int(input("Write your number 1 or 2: "))
#     if your_number == decision:
#        a = True
#     else:
#         a = False
#     return a
# huy = random_number()
# print(huy)

#acceptable and returnable function и сделать распаковку словаря!
# import random
# def schedule(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#     luckyOne = random.choice(tickets)
#     tickets.remove(luckyOne)
#
#     luckyTwo = random.choice(tickets)
#     tickets.remove(luckyTwo)
#
#     luckyThree = random.choice(tickets)
#     tickets.remove(luckyThree)
#
#     luckyFour = random.choice(tickets)
#     tickets.remove(luckyFour)
#
#     luckyFive = random.choice(tickets)
#     tickets.remove(luckyFive)
#
#     luckySix = random.choice(tickets)
#     tickets.remove(luckySix)
#
#     luckySeven = random.choice(tickets)
#     tickets.remove(luckySeven)
#
#
#     days = {Monday : luckyOne, Tuesday : luckyTwo, Wednesday : luckyThree, Thursday : luckyFour, Friday : luckyFive,
#             Saturday : luckySix, Sunday : luckySeven}
#
#
#
#     return days
#
# days = schedule('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
#                 'Saturday', 'Sunday')
# print(days)

#matrixInRealLife
def get_matrix(n, m, value):
    matrix = [ ]
    for i in range(n):
        matrix.append([ ])
        for j in range(m):
            matrix[i].append(value)
    return matrix

result1 = get_matrix(5, 5, 99)

result2 = get_matrix(7, 7, 7)

result3 = get_matrix(6, 6, 6)

print(result1)

print(result2)

print(result3)


