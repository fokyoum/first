#[클래스 상속] 

# 1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속한다.

# 2. 자식 클래스에서 별도의 메서드나 속성을 추가할수 있다.

# 3. 메서드 오버라이딩

# 4. super()

# 5. Python 의 모든 클래스는 object 클래스를 상속한다. : 모든것은 객체이다. 

# MyClass.mro()  -> 상속관계를 보여준다. 

class Robot :  # class 대문자 : or class Robot(object):
    population=0  
   
    def __init__(self,name):
        self.name=name 
        Robot.population+=1
        
        
    def say_hi(self):  # instance method
        # code 생략 자연어~~~ + CNN 
        print(f"Greetings, my masters call me {self.name}")
    
    def cal_add(self,a,b): # 여기서 a,b 인자는 이 함수만을 위한거지
        return a+b

    def die(self):
        print(f"{self.name} is dead")
        Robot.population-=1
        if Robot.population==0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robots working")

  


    @staticmethod   # @@@@ 이걸 써주면 siri.this_is_robot_class도 가능
    def this_is_robot_class(): #self, cls 둘다 아닌경우
        print("yes!!")  # 이 경우 Robot.this_is_robot_class로 출력은 되!
                       # 그러나 이경우 가급적 staticmethod 라고 적는다. 




    def __str__(self): # 결국 print(객체) 표현 Overwriting
        return f"{self.name} robot!!"

    def __call__(self):
        print("call@@")
        return f"{self.name} call"


class Siri(Robot):  # method overwriting 같은 이름 func 을 쓰면 덮어씌어진다. 
    
    def __init__(self,name,age):  # overwriting 됨 Robot.population 삭제됨
        super().__init__(name)   # super() 는 부모 class 라고 생각하면됨
        self.age=age       # Robot.population 굳이 안써도 자연스럽게 불러드림.

    @classmethod           #decorator : 모든함수에 적용되는 공통된 함수로 decoration (이미 만든것)
    def how_many(cls):     # __init은 self를 받지만, cls를 받는다.
        print(f"we have {cls.population} robots")
                       # cls 는 class 

    def call_me(self):
        print("네?")

    def cal_mul(self,a,b):
        self.a=a  # 새롭게 정의 보통 생성자에서 정의내려야함. 
        return a*b

    def cal_flexible(self,a,b):
        super().say_hi() # by apple 이 안나와 super 로 기존꺼 쓰는거니깐
        return self.cal_mul(a,b)+self.cal_add(a,b)+super().cal_add(a,b)

    def say_hi(self): #say_hi 의 overwriting
        print(f"Greetings, my masters call me {self.name}.by apple")
    
    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple!!! ")

    @classmethod         
    def how_many(cls):    # classmethod 도 overwriting 됨
        return f"we have {cls.population} robots by apple"
                       #


siri=Siri("iphone8","19")


#print(Siri.mro())

#print(Robot.mro())  # mro 는 상속관계를 보여주는데 왜 아래와 같이 나올까???

#<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]
#<class '__main__.Robot'>, <class 'object'>]  원래는  class Robot(object) 인데 object 가 생략됨 
# 모든 class 는 object 를 상속 받는다. 

print(object)
print(dir(object))
print(object.__name__)

print(int.mro()
print(int.__init__(8.9))
print(int(8.9)) # str, bool ,float 등도 다 클래스임


# print(siri)   # __str__ 이 실행됨

# print(siri.cal_add(2,3))

# siri.call_me()

# print(siri.cal_mul(1,8))

# print(siri.a) # 위에 cal_mul 에서 a=1 값이 namespace로 들어가므로 
 
# Siri.hello_apple() # Classmethod Siri 가 붙지. 

# siri.say_hi()

# print(Siri.how_many())

# siri.cal_flexible(1,3)
