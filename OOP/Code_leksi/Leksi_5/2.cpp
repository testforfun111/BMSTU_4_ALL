#include <iostream>

using namespace std;

class A 
{
    private:
        int value = 1;
    
    public:
        A() { value *= 2; }
        A(const A&) { value *= 3; }
        A(A&&) noexcept { value *= 4; }
        ~A() { cout << value << endl; }  
};

A f(A obj) { return obj;}

A f1() { return A();}

A f2()
{
    A obj;
    return obj;
}

int main()
{
    cout << "prim 1" << endl;
    {
        A obj;
        f(obj);
    }

    cout << "prim 2" << endl;
    {
        A obj = f1();
    }

    cout << "prim 3" << endl;
    {
        A obj = f2();
    }
    return 0;
}