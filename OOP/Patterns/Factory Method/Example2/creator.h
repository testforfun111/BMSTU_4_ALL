#ifndef __CREATOR_H__
#define __CREATOR_H__
#include <iostream>
#include <memory>
using namespace std;
template<typename Tbase, typename ...Args>
class Creator
{
    public:
        virtual ~Creator() = default;
        virtual unique_ptr<Tbase> createProduct(Args ...args) = 0; 
};

template<typename Tbase, typename Tprod, typename ...Args>
class ConCreator : public Creator
{
    public:
        virtual ~ConCreator() override
        {
            std::cout << "Destructor ConCreator\n";
        }
        virtual unique_ptr<Tbase> createProduct(Args ...args) override
        {
            return unique_ptr<Tbase>(new Tprod(args));
        }
};
#endif