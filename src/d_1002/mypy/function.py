print("//----- function 문법 : start -----//")
print("function1--------------------------------------------")

# 값을 실행한 결과를 전달 : return
def my_function(num1):
    result = num1 + 100
    return result

sum = my_function(10)

print(sum)





print("function2--------------------------------------------")
# 매개변수의 parameter 갯수를 맞춰야 한다. 맞지 않으면 TypeError 발생
def my_function2(fname, lname):
    print(fname + " " + lname)

my_function2("Hailey", "Kim")

# my_function2("Hailey")
# TypeError: my_function2() missing 1 required positional argument: 'lname'





print("function3--------------------------------------------")
# 기본 매개변수 값 설정 : parameter에 default 값을 설정하면, 호출시 해당 parameter를 생략 가능
def my_function(country = "korea"):
  # 공통 출력 기능
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()





print("function4--------------------------------------------")
# parameter를 호출할 때, parameter 이름을 지정하여 값을 전달 가능
def my_function(animal, name):
   print("I have a", animal)
   print("My", animal + " 'is named", name)

my_function(animal = "dog", name = "Buddy")
# parameter 순서와 상관없이 호출 가능
my_function(name = "Buddy", animal = "dog")

print("//------ function 문법 : end ------//")