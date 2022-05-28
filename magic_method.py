class Robot : 

    """
    Author : 우성
    Role : Robot
    """
    
    # Class 변수 , instance 들이 공유하는 변수
    population=0  # __init__ 은 instance 찍어낼때마다 실행인데
    
    # 생성자 함수 , instance가 생성될때 초기화함수
    def __init__(self,name):
        self.name=name # self는 각각의 instance을 뜻함
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

    @classmethod           #decorator : 모든함수에 적용되는 공통된 함수로 decoration (이미 만든것)
    def how_many(cls):     # __init은 self를 받지만, cls를 받는다.
        print(f"we have {cls.population} robots")
                       # cls 는 class 


    @staticmethod   # @@@@ 이걸 써주면 siri.this_is_robot_class도 가능
    def this_is_robot_class(): #self, cls 둘다 아닌경우
        print("yes!!")  # 이 경우 Robot.this_is_robot_class로 출력은 되!
                       # 그러나 이경우 가급적 staticmethod 라고 적는다. 




    def __str__(self): # 결국 print(객체) 표현 Overwriting
        return f"{self.name} robot!!"

    def __call__(self):
        print("call@@")
        return f"{self.name} call"


droid1=Robot("R2-D2")
droid1.say_hi()
rint(dir(droid1))

#magic method : 형식  __xx__

#(1) __str__


print(droid1)   #<__main__.Robot object at 0x0000017E239D89A0> 이거 봐도 알겠니?
                 #객체를 어떻게든 꾸겨서 보여준거지
                 #객체를 보여주기 위해서 __str__ 존재함 

droid1() # 일반 method 함수처럼 instance 는 callable하지 않음. 
         # __call__ 넣으면 callable 즉 class 안에 모든것은 객체
         #함수또한 callable 인 상태일뿐임. 

