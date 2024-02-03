#ifndef __PRODUCT_H__
#define __PRODUCT_H__
#include <iostream>

class Product 
{
    public:
        virtual ~Product() = default;
        virtual void run() = 0;
};

class ConProduct : public Product
{
    private:
        int price;
        double value;
    public:
        ConProduct(int c, double p) : price(c), value(p)
        {
            std::cout << "Constructor ConProduct\n";
        }
        virtual ~ConProduct() override 
        {
            std::cout << "Destructor ConProduct\n";
        }

        virtual void run() override
        {
            std::cout << "Run ConProduct\n";
        }   
};

#endif