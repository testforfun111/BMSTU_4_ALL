#include "creator.h"
#include "product.h"
#include <iostream>
#include <memory>

using namespace std;

using TbaseCreator = Creator<Product, int, double>;
class User
{
    public:
        void use(shared_ptr<TbaseCreator>& cr)
        {
            shared_ptr<Product> ptr = cr->createProduct(1, 100.);
            ptr->run();
        }
};

int main()
{
    shared_ptr<TbaseCreator> cr(new ConCreator<Product, ConProduct, int, double>());
    unique_ptr<User> us = make_unique<User>();
    
    us->use(cr);
    return 0;
}