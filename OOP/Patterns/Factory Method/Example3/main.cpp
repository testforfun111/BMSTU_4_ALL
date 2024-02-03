#include <iostream>
#include <memory>

using namespace std;

class Product;

class Creator 
{
    public:
        shared_ptr<Product> getProduct();
    protected:
        virtual shared_ptr<Product> createProduct() = 0;
    private:
        shared_ptr<Product> product;
};

template<typename Tprod>
class ConCreator: public Creator
{
    protected:
        virtual shared_ptr<Product> createProduct() override
        {
            return shared_ptr<Product>(new Tprod()); 
        }
};

shared_ptr<Product> Creator::getProduct()
{
    if (!product)
        product = this->createProduct();
    return product;
}

class Product
{
    public:
        virtual ~Product() = default;
        virtual void run() = 0;
};

class ConProduct : public Product
{
    public:
        ConProduct() { cout << "Constructor ConProduct\n";}
        virtual ~ConProduct() override
        {
            cout << "Destructor ConProduct\n";
        }
        virtual void run() override 
        {
            cout << "Function run in ConProduct\n";
        }
};

int main()
{
    shared_ptr<Creator> cr(new ConCreator<ConProduct>());

    shared_ptr<Product> ptr1 = cr->getProduct();
    shared_ptr<Product> ptr2 = cr->getProduct();

    cout << ptr1.use_count() << endl;
    return 0;
}