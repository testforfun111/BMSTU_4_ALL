#include <iostream>

using namespace std;

void f1(int& x) {cout << "int&" << endl;}
void f1(const int& x) {cout << "const int&" << endl;}

void f2(int& x) {cout << "int&" << endl;}
void f2(int x) {cout << "int" << endl;}

void f3(const int& x) {cout << "const int&" << endl;}
void f3(int&& x) {cout << "int&& " << endl;}

void f4(int& x) {cout << "int&" << endl;}
void f4(int&& x) {cout << "int&& " << endl;}

int main()
{
    int i = 0;
    const int ci = 0;
    int& lv = i;
    const int& clv = ci; 
    int&& rv = i + 1;

    cout << "function1" << endl;
    f1(i); //int&
    f1(ci); //const int&
    f1(lv); //int&
    f1(clv); //ci&
    f1(rv); // int&
    cout << "function2\n";
    // f2(i); // Error 
    f2(ci); //int
    // f2(lv); //int&
    f2(clv); //ci&
    // f2(rv); // int&
    cout << "function3" << endl;
    f3(i); //const int&
    f3(ci); //const int&
    f3(lv); //const int&
    f3(clv); //const int&
    f3(rv); // const int&

    cout << "function3" << endl;
    f4(i); //int&
    // f4(ci); //error 
    f4(lv); //int&
    // f4(clv); //error 
    f4(rv); // int&
    return 0;
}