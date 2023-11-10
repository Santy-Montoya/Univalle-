# list comprehension

square = []

# def function_square():
#     for i in range(10):
#         square.append(pow(i,2))
#     return square

# if __name__ == '__main__':
#     print(function_square())

square = [i**2 for i in range(10) if i > 2]
print(square)