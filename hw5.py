def read_single_digit(digit):
    
    if digit == 0:
        return "영"
    elif digit == 1:
        return "일"
    elif digit == 2:
        return "이"
    elif digit == 3:
        return "삼"
    elif digit == 4:
        return "사"
    elif digit == 5:
        return "오"
    elif digit == 6:
        return "육"
    elif digit == 7:
        return "칠"
    elif digit == 8:
        return "팔"
    elif digit == 9:
        return "구"


def read_number(num):
    hundreds_digit = num // 100
    tens_digit = (num % 100) // 10
    ones_digit = num % 10

    hundreds = read_single_digit(hundreds_digit)
    tens = read_single_digit(tens_digit)
    ones = read_single_digit(ones_digit)

    print(f'{hundreds} {tens} {ones}') 
            

num = int(input('세 자리 정수 입력: '))
result = read_number(num)

