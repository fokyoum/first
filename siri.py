

# 여러 로봇이 공통된 기능이 있다고 하자
# 추상화 -> 공통된 속성이나 행위를 묶는것.


class Robot : 

    """
    Author : 우성
    Role : Robot
    """
    
    # Class 변수 , instance 들이 공유하는 변수
    population=0  # __init__ 은 instance 찍어낼때마다 실행인데
    
    # 생성자 함수 , instance가 생성될때 초기화함수
    def __init__(self,name,):
        self.name=name # self는 각각의 instance을 뜻함
        Robot.population+=1
        
    def say_hi(self):  # instance method
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

    @classmethod           #decorator : 모든함수에 적용되는 공통된 함수로 decoration (이미 만든것)
    def how_many(cls):     # __init은 self를 받지만, cls를 받는다.
        print(f"we have {cls.population} robots")
                       # cls 는 class 


    @staticmethod   # @@@@ 이걸 써주면 siri.this_is_robot_class도 가능
    def this_is_robot_class(): #self, cls 둘다 아닌경우
        print("yes!!")  # 이 경우 Robot.this_is_robot_class로 출력은 되!
                       # 그러나 이경우 가급적 staticmethod 라고 적는다. 

# siri=Robot("siri",2103978812)
# jarvis=Robot("siri",83838483030)
# bixby=Robot("bixby",122323213)
# bixby2=Robot("bixby2",122323213 )

# print(Robot.population)

# print(siri.name)
# siri.say_hi()
# #jarvis.say_hi()  # siri.say_hi() 는 독립적
# #siri.cal_add(2,3)

# #Robot.how_many()  # Class method

#siri.die()
#jarvis.die()

# print(Robot.__dict__) # class의 namespace
# print(siri.__dict__) # instance의 namespace 

#왜 instance method는 class namespace 안에 있을까? 
# instance method namespace memory 공간을 아끼기 위해

#siri.say_hi() 여기서 say_hi는 instance namespace에 없지만
#파이썬 자체에서 instance namespace에 없으면 class namespace에 호출
# 이원리로 

# print(siri.population) #얘도 가능 
# siri.how_many() # 얘도 가능

# siri.say_hi() #(o)
# Robot.say_hi() #(x) 오히려 class namespace 에 있지만 클래스에서 호출하면 에러
# Robot.say_hi(siri) # 얘는 가능 근데 안쓰겠지

# print(dir(siri))   #Instance siri를 통하여 접근할수 있는 키값들 (메소드,속성)

# print(Robot.__doc__) #개발자가 쓴 Descrition 을 쓰기 위해서 ~! 
# print(siri.__class__)

droid1=Robot("R2-D2")
droid1.say_hi()

print(dir(droid1)) -> __