def add_two_number(i:int, j:int) -> int or TypeError:
    if type(i)!= int or type(j)!=int:
        raise TypeError()
    return i+j


if __name__== "__main__":
    add_two_number(1,3.1)