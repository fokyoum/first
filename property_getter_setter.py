

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
        return a+b

    @classmethod          
    def how_many(cls):   
        print(f"we have {cls.__population} robots")

# droid = Robot("R2-D2",2)  # AGE 에 접근하려면??

droid=Robot("R2-D2",2)

#droid.age=7   # 즉 new_age 에 값을 넣어서 self.__age 값이 생성되고 setter 함수를 통하여 값이 변경됨 .

# droid.age=-99

print(droid.age)

print(droid.name)