# ###############match 문법####################
# - 문법이란?
# - 변수란?
# #############################################

# //----- match 문법 : start -----//
# (주석 설명 쓰는 곳)
# //------ match 문법 : end ------//

"""
match 문법은 파이썬 3.10 버전부터 지원되는 새로운 구조입니다.
match 문법은 switch/case 문법과 유사하며, 
특정 값에 따라 여러 코드 블록 중 하나를 선택적으로 실행할 수 있도록 합니다.
"""

print("//----- match 문법 : start -----//")
print("day--------------------------------------------------")

day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
     print("Wednesday")
    case 4:
        print("Thursday")
        print("기능정리1")
        print("기능정리2")
        print("기능정리3")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

print("day2--------------------------------------------------")






day2 = 4

match day2:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

    #  일치하는 항목이 없을 때 코드 블록을 실행하려면 마지막 case 값으로 밑줄 문자 (_) 를 사용
    #  마지막 경우에 배치 하는 것이 중요 


print("day3--------------------------------------------------")






day3 = 4

match day3:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")


print("day4--------------------------------------------------")






month = 5
day5 = 4

match day5:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")

print("//------ match 문법 : end ------//")