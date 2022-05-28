class Robot : 

    population=0  
    
   
    def __init__(self,name,age):
        self.name=name 
        self.__age=age    # Private 값을 못바꾸게 함. 
        Robot.population+=1
        
    def say_hi(self): 
        print(f"Greetings, my masters call me {self.name}")
    
    def cal_add(self,a,b): 
        return a+b

    def die(self):
        print(f"{self.name} is dead")
        Robot.population-=1
        if Robot.population==0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robots working")

    @classmethod          
    def how_many(cls):   
        print(f"we have {cls.population} robots")


class Siri(Robot):

    def __init__(self,name,age):
        super().__init__(name,age)
        #print(self.__age) -> 아직 은닉이라 에러남.
        self.__age=999  # 새로운 정의 기존에 self.__age 와 다르게 새변수로 봄
        print(self.__age)


ss=Robot("yss",8)


#ss.age=-999 # 나이가 그렇게 많다고? namespace 가 보호가 안됐음

ssss=Siri("iphone8",9)


    # def __say_hi(self):  method 나 클래스 변수 앞에도 __ 두개 붙이면 private

     #   print(f"Greetings, my masters call me {self.name}")
     # 외부 접근 금지
