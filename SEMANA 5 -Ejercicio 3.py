#ejercicio 
def is_triangle(a,b,c):
    if a + b <= c or b + c <= a or  c + a <= b:
        return False
def is_tream (a,b,c):
    if a > b and a > c:
        return a**2 == b**2 + c**2
    if b > a and b > c:
        return b**2 == a**2 + c**2
    if c > a and c > b:
        return c**2 == b**2 + a**2
    return True


if __name__ == '__main__':
    print (is_tream(4,2,3))
    print (is_tream(2,5,7))


# def is_triangle(a, b, c):
#     if a + b > c and b + c > a and a + c > b:
#         return True

# def is_trianguleRect(a,b,c):
#     if not is_triangle(a,b,c):
#         return False
#     if c > a and c > b:
#         return c**2 == a**2 + b**2
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2