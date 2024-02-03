#include <iostream>
using namespace std;

class A 
{
    private:
        int a;
        mutable int b;
    
    public:
        int f()& { cout << "int()&" << endl; return ++a;}
        int f() const& 
        {
            cout << "int() const &" << endl;
            // ++a; // Error 
            return ++b;
        }
        int f()&& { cout << "int()&&" << endl; return b += a;}
};

A func(const A& obj)
{
    return obj;
}

int main()
{
    A obj1;
    const A obj2{};
    
    obj1.f();

    obj2.f();

    std::move(obj1).f();

    A().f();

    func(obj1).f();
    
    return 0;
}