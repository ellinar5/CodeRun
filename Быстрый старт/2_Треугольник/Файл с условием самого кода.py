import sys


def main():
    
    """
    Проверка значений происходит так:
    1) число_1 + число_2 > число_3
    2) число_1 + число_3 > число_2
    3) число_2 + число_3 > число_1
    """

    number_1 = int(input())
    number_2 = int(input())
    number_3 = int(input())

    if (number_1 + number_2) > number_3 and (number_1 + number_3) > number_2 and (number_2 +number_3) > number_1:
        print("YES")
    

    else:
        print("NO")


if __name__ == '__main__':
    main()
