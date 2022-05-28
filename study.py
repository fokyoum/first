class Cal:

    def __init__(self,a,b): # 생성자함수 Constructor, 클래스가 메모리가 올라왔을때 
       self.a=a                # 즉 INSTANCE 를 만들었을때 즉시 실행!!!!
       self.b=b                # self 는 instance 를 만들었을때 그 instance를 지칭 
                               # self 말고 딴것 써도되긴해   

    def add(self):  #self 를 써주는 이유 instance 안에 namespace에서 접근할수있도록
        return self.a+self.b      #instance 안에 namespace에서 이미 a,b 정의되어서 a,b삭제

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b
    
cal1 = Cal(1,2)  # self 가 cal1 을 가리킨다. 
cal2 = Cal(3,4)  # 새로운 쿠키 독립적인 

print(cal1.a)  # cal. 만 눌러도 뒤에 a,b 생성되지? 인스턴스 안에 namespace임
print(cal1.b)
print(cal1.add())

print(cal2.a)
print(cal2.b)   # CTRL + / 주석처리 

cal1.a=7   # namespace 안에는 1이었는데 7로 변경 가능해!! 
           # NAMESPACE 안에 수정하면 전체 함수(A,B) 안에 A도 다바뀜.