# include <iostream>

using namespace std;

class A
{
public:
	void f() { cout << "Executing f() from A;" << endl; }
	void f(int i) { cout << "Executing f(int) from A;" << endl; }
    void g(int i) { cout << "Executing g(int) from A;" << endl; }
};

class B : virtual public A
{
public:
	void f() { cout << "Executing f() from B;" << endl; }
	using A::f;
};

class C : virtual public A {};

class D : virtual public C, virtual public B {};

int main()
{
	D obj;

	obj.f();
	obj.f(1);
    obj.g(1);
    return 0;
}
