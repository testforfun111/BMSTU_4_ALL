#include "creator.h"
#include "product.h"

int main()
{
    shared_ptr<Creator> cr(new ConCreator<ConProduct>());
    shared_ptr<Product> prod = cr->createProduct();

    prod->run();
    return 0;
}