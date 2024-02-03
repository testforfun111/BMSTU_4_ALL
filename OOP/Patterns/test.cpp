#include <iostream>
#include <string>
using namespace std;

class A
{
public:
    A (char* s) { cout << "Creature A" << s << ";" << endl; }
};
    
class B : public A
{
public:
    B() : A (" from B") { cout << "Creature B;" << endl; }
};
    
class C : public B, public A // В класс C подобъект класса А будет
{                            // входить два раза.
public:
    C() : A(" from C") { cout << "Creature C;" << endl; }
};
     
int main()
{
    C obj;
    return 0;
}