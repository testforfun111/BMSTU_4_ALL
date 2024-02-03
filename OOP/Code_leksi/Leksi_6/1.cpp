#include <iostream>
#include <initializer_list>

using namespace std; 

class Complex
{
    private:
        double _re, _im;
    
    public:
        Complex() = default;

        Complex(double r) : Complex(r, 0.0) {}
        
        Complex(int r) : Complex(r, 0.0) {}

        Complex(double r, double i) : _re(r), _im(i) {}

        Complex(const Complex& c) : Complex(c._re, c._im) {}
        Complex(Complex &&C) : Complex(C._re, C._im) {}

        Complex(initializer_list<double> list)
        {
            for (double elem: list) {}
        }

        void set_Real(int r) {this->_re = r;}
        void set_Real(double) = delete;

        static Complex sum(const Complex& c1, const Complex& c2)
        {
            Complex ctmp(c1._re + c2._re, c1._i + c2._im);
            return ctmp;
        }

        Complex& operator=(const Complex& c)
        {
            this->_re = c._re;
            this->_im = c._im;
            return *this;
        }

        Complex& operator=(Complex&& c)
        {
            this->_re = c._re;
            this->_im = c._im;
            return *this;
        }

};

int main()
{
    Complex a1(),
        a2(Complex()),
        b1, 
        b2{},
        b3 = {},
        b4((Complex())),
        b5(Complex{}),
        b6 = Complex{}, 

        c1_1(1.5), c1_2(1), 
        c2 = Complex(5.5), 
        c3{ 2. }, 
        c4 = {3.},
        c5 = Complex({ 4. }), 
        c6 = 4.5, 
        d1(1., 2.), 
        d4 = Complex(4., 5.), 
        d2{2., 3.},
        d3 = {3., 4.},

        d5 = Complex({5., 6.}),
        e1(c1_1), 
        e2 = Complex(c),
        e3 {c3}, 
        e4 = {c4},
        e5 = Complex({c5}),
        e6 = c6, 

        f1(Complex::sum(c1_1, c2));

    b1 = {};
    b2 = Complex{};
    c1_1 = {1.};
    c4 = 4.;
    d1 = {2., 3.};

    e1.set_Real(1);
    return 0;
}