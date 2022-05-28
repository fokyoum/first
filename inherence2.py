from ast import Pass


class A:
    pass

class B:
    pass

class C:
    pass

class D(A,B,C):   # 전체를 다 받을수 있음 (다중상속) 별로 쓰이진 않지만, 부품을 조립용으로 쓰임
    pass

print(D.mro())