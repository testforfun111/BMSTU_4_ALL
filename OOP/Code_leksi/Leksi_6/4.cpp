#include <iostream>

using namespace std;

class A 
{
    public:
        A(const char *s) {cout << "Class A "<< s << endl; }
};

class B : virtual public A 
{
    public:
        B (const char* s) : A(s)
        {
            cout << "Class B " << s << endl;
        }
};

class C : virtual public A 
{
    public:
        C (const char* s) : A(s)
        {
            cout << "Class C " << s << endl;
        }
};

class D : public B, public C
{
    public:
        D() : B("D"), C("D"), A("E")  // why use A
        {
            cout << "Class D" << endl;
        }
};

int main()
{
    D obj;
    return 0;
}