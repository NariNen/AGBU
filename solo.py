# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))
#
# bmi = weight / (height ** 2)
#
# while True:
#     if bmi < 18.5:
#         print("Underweight")
#         break
#     elif bmi < 25:
#         print("Normal")
#         break
#     elif bmi < 30:
#         print("Overweight")
#         break
#     else:
#         print("Obesity")
#         break
# n = int(input("please enter some number"))
# result = sum(range(1, n+1))
# print(result)
# txt = "hello"
# print(max(text))
# def func(x):
#     res = 0
#     for i in range(x):
#         res += i
#     return res
#
#
# print(func(3))
#
# n = [2, 4, 6, 8]
# res = 1
# for x in n[1:3]:
#     res *= x
# print(res)
# car = {
#     'brand':'BMW',
#     'year': 2018,
#     'color': 'red',
#     'mileage': 15000
# }
# print(car(input("please")))
# print()
# x = list(str(input()))
# rev = x[::-1]
# print(rev[0])
def calculate_average(myList):
    # result = 1
    lenght = len(mylist)
    summy = sum(myList)

    # for i in mylist:
    #     result = i + result
    # return result / lenght

# myList = [10, 20, 30, 40, 50]
# print(myList)
# print(calculate_average(myList))
# ---------------
def calculate_average(myList):
    sumOfList = sum(myList)
    lenOfList = len(myList)
    average = sumOfList / lenOfList
    return average


myList = [10, 20, 30, 40, 50]
+
result = calculate_average(myList)
print("Average of Mylist is:", result)