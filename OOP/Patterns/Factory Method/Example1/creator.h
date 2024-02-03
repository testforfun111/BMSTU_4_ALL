#pragma once 
#include <iostream>
#include <memory>

using namespace std;
class Product;

class Creator 
{
    public:
        virtual unique_ptr<Product> createProduct() = 0;
};

template <typename Tprod>
class ConCreator : public Creator
{
    public:
        virtual unique_ptr<Product> createProduct() override 
        {
            return unique_ptr<Product>(new Tprod());
        }
};

