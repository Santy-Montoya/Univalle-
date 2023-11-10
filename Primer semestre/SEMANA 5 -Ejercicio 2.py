#funtions simple 
#triangle 

def is_triangle(a,b,c):
    if a + b <= c or b + c <= a or  c + a <= b:
        return False
    return True
if __name__ == '__main__':
    print (is_triangle(1,1,1))
    print (is_triangle(1,1,3))
    print (is_triangle(1,1,2))
    print (is_triangle(2,1,2))