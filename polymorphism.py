"""
Polymorphism (다형성 )
여러 형태를 가질수 있다. 즉 객체를 부품화 할수 있다.
같은 형태의 코드가 다른 동작을 하도록 하는것.

Composition 

완전 상속이 아닌, 다른 클래스의 일부 메서드를 사용하고 싶지만 상속은 피하는 경우
1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야한다.
2. 부모 클래스의 매서드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가. 

"""

class Robot : 

    __population=0  
    
   
    def __init__(self,name,age):
        self.__name=name 
        self.__age=age    # Private 값을 못바꾸게 함. 
        Robot.__population+=1


    @property
    def name(self):
        return f"yoon {self.__name}"


    @property
    def age(self):
        return self.__age

    @age.setter  # property(getter) 의 동일 함수이름 + .setter : 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때. 
    def age(self,new_age): # 함수도 동일하게
        if new_age<0:
            raise TypeError("invalid range")  # TypeError, KeyError 등 다양  try except raise 셋다 알고 있기. 
        else: 
            print(new_age)
            self.__age = new_age

    @age.setter  # property(getter) 의 동일 함수이름 + .setter : 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때. 
    def age(self,new_age): # 함수도 동일하게
        if new_age-self.__age==1:
            self.__age=new_age
        else: 
            raise ValueError("inappropiate value")


    def __say_hi(self): 
        print(f"Greetings, my masters call me {self.name}")
    
    def cal_add(self,a,b): 
        return a+b+2     # cal_add 가 수정되면 아래 자식 class 가 다바뀔텐데??


    @classmethod          
    def how_many(cls):   
        print(f"we have {cls.__population} robots")

# droid = Robot("R2-D2",2)  # AGE 에 접근하려면??

droid=Robot("R2-D2",2)

#droid.age=7   # 즉 new_age 에 값을 넣어서 self.__age 값이 생성되고 setter 함수를 통하여 값이 변경됨 .

# droid.age=-99

print(droid.age)

print(droid.name)

class Siri(Robot):
    def say_apple(self):
        print("hello my apple")

class SiriKo(Robot):
    def say_apple(self):
        print("안녕하세요")

class Bixby(Robot):
    def say_samsung(self):
        print("안녕하세요")

class BixbyCal:

    def __init__(self,name,age):
        self.Robot=Robot(name,age)

    def cal_add(self,a,b):
        return self.Robot.cal_add(a,b)