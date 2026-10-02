# OOP stands for Object-Oriented Programming. 객체 지향 프로그래밍은 프로그램을 객체 단위로 나누어 개발하는 방법론입니다. 객체는 데이터와 그 데이터를 처리하는 메서드를 포함.
print("//----- OOP 클래스 : start -----//")
print("class MyClass--------------------------------------------")

class MyClass:
    x = 5   

print(MyClass)
# 오브젝트가 아니라 클래스 변수이므로, MyClass.x 로 접근 가능
print(MyClass.x)

# 클래스의 인스턴스를 생성하여 접근 가능
p1 = MyClass()

print(p1)
# 오브젝트의 속성으로 접근 가능
print(p1.x)





print("__init__/Parent Class-------------------------------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Hailey", 34)
print(p1.name)
print(p1.age)

# add proporties to the student class
class Student(Person):
    def __init__(self, name, age, school, grade):
        super().__init__(name, age) 
        self.school = school
        self.grade = grade


st1 = Student("Hailey", 34, "Sejong University", 4)
print(st1)
print(st1.name)
print(st1.age)
print(st1.school)
print(st1.grade)





print("__init__/Parent Class/ex-----------------------------------------")

class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Square(Shape):
    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width

class Circle(Shape):
    def __init__(self, name, color, radius, halfradius):
          super().__init__(name, color)
          self.radius = radius
          self.halfradius = halfradius

sq = Square("Nemo", "yellow", 10, 10)
cr = Circle("Dongle", "red", 5, 2.5)

print("="*8, "Square Class", "="*8)
print(sq.name)
print(sq.color)
print(sq.length)
print(sq.width)
print("="*8, "Circle Class", "="*8)
print(cr.name)
print(cr.color)
print(cr.radius)
print(cr.halfradius)




print("Outer <-> Inner Class-----------------------------------------")

class Outer:
  def __init__(self):
    self.name = "Emil"

    # 외부에서 내부 계층에 접근
  class Outin:
    def __init__(self):
      self.name = "Outin"
      
    def display(self):
      print("Hello from Out to in class")

    # 내부에서 외부 계층에 접근
  class Inout:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")


outer = Outer()             # 외부 클래스 인스턴스 생성

outin = outer.Outin()       # 외부에서 내부 계층에 접근
outin.display()             # Hello from Out to in class

inout = outer.Inout(outer)  # 내부에서 외부 계층에 접근
inout.display()             # Outer class name: Emil


print("//----- OOP 클래스 : end -----//")