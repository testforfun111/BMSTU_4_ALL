#include <iostream>

void f(int) {}

int main()
{
    int i = 0;

    int &lref1 = i;
    int &lref2(i);
    int &lref3 {i};
    int &lref4 = {i};

    int& lv1 = i;
    int& lv2 = 2; // Error 2 not is lvalue
    int& lv3 = i + 1; //Error 
    const int& lv4 = i + 1; // create object 
    ++lv1;

    int&& rv1 = i; // Error 
    int&& rv2 = 2; //ok 
    int&& rv3 = i + 1; // ok 
    const int&& rv3 = i + 1; 
    ++rv2;

    int&& rv5 = rv2; //error 
    int& lv5 = rv2;  //ok 

    int&& rv6 = (int) i;
    int&& rv7 = std::move(i);


}