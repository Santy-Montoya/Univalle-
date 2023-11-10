# def suma (num):
#     if num == 1:
#         return 1
#     else: 
#         return num + suma (num - 1)
    
# if __name__ == '__main__':
#     print(suma(10))

def collatz (num):
    print (num)
    if num == (1):
        return 1
    elif num % 2 == 0:
        return collatz (num/2)
    else:
        return collatz (num*3 + 1)
    
print(collatz(10))
   


    
