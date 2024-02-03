#include <iostream>
#include <ctime>
#include <cmath>

using namespace std;
#define TIMES 1e5

void cout_time(clock_t time, const char* action)
{
    cout << "   " << action << ": " << ((double)time) / TIMES << " ms.";
}

template <typename Type>
Type sum(Type a, Type b)
{
    Type result = 0;
    clock_t start_time, res_time = 0;

    for (int i = 0; i < TIMES; i++)
    {
        start_time = clock();
        result = a + b;
        res_time += clock() - start_time;
    }

    cout_time(res_time, "Sum");

    return result;
}

template <typename Type>
Type sum_asm(Type a, Type b)
{
    Type result = 0;
    clock_t start_time, res_time = 0;

    for (int i = 0; i < TIMES; i++)
    {
        start_time = clock();
        __asm {
            fld a
            fld b
            faddp ST(1), ST(0)
            fstp result
        }
        res_time += clock() - start_time;
    }

    cout_time(res_time, "Sum");

    return result;
}

template <typename Type>
Type mul(Type a, Type b)
{
    Type result = 0;
    clock_t start_time, res_time = 0;

    for (int i = 0; i < TIMES; i++)
    {
        start_time = clock();
        result = a * b;
        res_time += clock() - start_time;
    }

    cout_time(res_time, "Mul");

    return result;
}

template <typename Type>
Type mul_asm(Type a, Type b)
{
    Type result = 0;
    clock_t start_time, res_time = 0;

    for (int i = 0; i < TIMES; i++)
    {
        start_time = clock();
        __asm {
            fld a
            fld b
            fmulp ST(1), ST(0)
            fstp result
        }
        res_time += clock() - start_time;
    }

    cout_time(res_time, "Mul");

    return result;
}

template <typename Type>
Type sub(Type a, Type b)
{
    Type result = 0;
    clock_t start_time, res_time = 0;

    for (int i = 0; i < TIMES; i++)
    {
        start_time = clock();
        result = a - b;
        res_time += clock() - start_time;
    }

    cout_time(res_time, "Sub");

    return result;
}

template <typename Type>
Type sub_asm(Type a, Type b)
{
    Type result = 0;
    clock_t start_time, res_time = 0;

    for (int i = 0; i < TIMES; i++)
    {
        start_time = clock();
        __asm {
            fld a
            fld b
            fsubp ST(1), ST(0)
            fstp result
        }
        res_time += clock() - start_time;
    }

    cout_time(res_time, "Sub");

    return result;
}

template <typename Type>
Type div(Type a, Type b)
{
    Type result = 0;
    clock_t start_time, res_time = 0;

    for (int i = 0; i < TIMES; i++)
    {
        start_time = clock();
        result = a / b;
        res_time += clock() - start_time;
    }

    cout_time(res_time, "Div");

    return result;
}

template <typename Type>
Type div_asm(Type a, Type b)
{
    Type result = 0;
    clock_t start_time, res_time = 0;

    for (int i = 0; i < TIMES; i++)
    {
        start_time = clock();
        __asm {
            fld a
            fld b
            fdivp ST(1), ST(0)
            fstp result
        }
        res_time += clock() - start_time;
    }

    cout_time(res_time, "Div");

    return result;
}

template <typename Type>
void time_measure(Type a, Type b)
{
    cout << "   ASM:";
    sum_asm(a, b);
    mul_asm(a, b);
    sub_asm(a, b);
    div_asm(a, b);
    cout << endl << "   CPP:";
    sum(a, b);
    mul(a, b);
    sub(a, b);
    div(a, b);
}

double sin_asm()
{
    double result = 0.0;
    __asm
    {
        fldpi
        fsin
        fstp result
    }
    return result;
}

double sin_half_asm()
{
    double result = 0.0;
    double divide = 2.0;
    __asm
    {
        fldpi
        fld divide;
        fdiv ST(1), ST(0)
        fsin
        fstp result
    }
    return result;
}


int main()
{
    float f1 = 1.1f;
    float f2 = 2.3f;
    cout << "FLOAT:" << endl;
    time_measure(f1, f2);

    double d1 = 2.3;
    double d2 = 5.6;
    cout << "\nDOUBLE:" << endl;
    time_measure(d1, d2);

    cout << endl << "CMP sin():" << endl;
    printf("sin(3.14)         = %.20f\n", sin(3.14));
    printf("sin(3.141596)     = %.20f\n", sin(3.141596));
    //printf("sin(M_PI)         = %.20f\n", sin(M_PI));
    printf("sin_asm(3.141596) = %.20f\n", sin_asm());
    cout << endl;
    printf("sin(3.14 / 2)          = %.20f\n", sin(3.14 / 2.0));
    printf("sin(3.141596 / 2)      = %.20f\n", sin(3.141596 / 2.0));
    //printf("sin(M_PI/ 2.0)         = %.20f\n", sin(M_PI / 2.0));
    printf("sin_half_asm(3.141596) = %.20f\n", sin_half_asm());

}