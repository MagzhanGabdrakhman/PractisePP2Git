class A:
    def show(self): print("A")

class B:
    def show(self): print("B")

class C(A, B): pass

class D(B, A): pass

class E(A, B): pass

class F(B, A): pass

class G(A, B): pass

class H(B, A): pass

class I(A, B): pass

class J(B, A): pass
