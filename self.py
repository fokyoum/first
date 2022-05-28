# self 의 이해
# self 는 인스턴스 객체이다.
# 클래스 안에 있는 self 의 주소와 만들어진 self의 주소는 같다.
# 즉 self 는 instance 자체이다. 

class SelfTest: 

    name="amamov"

    def __init__(self,x):
        self.x=x
    
    # 클래스 메서드

    @classmethod
    def func1(cls):  # cls 는 class 그 자체가 나온다. 
        print(f"cls:{cls}")
        print("func1")
    
    # 인스탄스 method
    def func2(self):
        print(f"self:{self}")
       
        print("Class 안의 self 주소 : ",id(self))
        print("func2")

test_obj=SelfTest(17)

test_obj.func2()
SelfTest.func1()

print("인스턴스의 주소:",id(test_obj))

"""    
Class 안의 self 주소 :  2303807423536
func2
cls:<class '__main__.SelfTest'>      
func1
인스턴스의 주소: 2303807423536

"""

test_obj.func1() # class method 에 넣어도 동작됨. class 로나옴
print(test_obj.name) # 이것도 나옴 class 변수도 호출 가능  

