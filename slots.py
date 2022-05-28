"""
객체내에 있는 변수들은 __dict__ 를 통해서 관리가 된다.
__slots__ 을 통해 변수를 관리:
파이썬 인터프리터에게 통보 해당 클래스가 가지는 속성을제한한다.
__dict__ 를 통해 관리되는 객체의 성능을 최적화 한다 
-> 다수의 객체 생성시 메모리 사용 공간 대폭 감소한다. 

"""

# from curses import ACS_GEQUAL
# from unicodedata import name


class WithoutSlotClass:
     def __init__(self,name,age):
          self.name=name
          self.age=age


wos=WithoutSlotClass("amamov",12)

# print(wos.__dict__) # 인스턴스에 대한 namespace를 dictionary형태로 

# wos.__dict__["hello"]="world"  # dictionary 형태라 가능함. 

# print(wos.__dict__


class WithSlotClass:
    __slots__=["name","age"]   # slots 로 attribute를 제한해서 메모리가 덜 먹음. 

    def __init__(self,name,age):
        self.name=name
        self.age=age

ws=WithSlotClass("amamov",12)


# print(ws.__dict__) # slots 가 있으면 dict 가 없음. slots 에서 관리함. 
print(ws.__slots__) 


# 성능 테스트 메모리 사용량 비교

import timeit

def repeat(obj):
    def inner():
        obj.name="amamov"
        obj.age=222
        del obj.namenpm install -g pyright
    return inner

use_slot_time=timeit.repeat(repeat(ws),number=9999)p
no_slot_time=timeit.repeat(repeat(wos),number=9999)p

print("use slot:", min(use_slot_time))
print("no slot:", min(no_slot_time))