#pragma once
#include <iostream>

class Product
{
    public:
        virtual ~Product() = 0;
        virtual void run() = 0;
};

Product::~Product() {}

class ConProduct : public Product
{
    public:
        virtual ~ConProduct() override {std::cout << "Destructor\n";}
        virtual void run() override {
            std::cout << "Run Conproduct!\n";
        }
};

