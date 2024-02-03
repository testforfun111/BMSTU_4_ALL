#include <iostream>
#include <memory>
#include <map>
#include <initializer_list>

using namespace std;

class Product;

//creator
class Creator
{
    public:
        virtual unique_ptr<Product> createProduct() = 0; 
};

template<class Tprod>
class ConCreator: public Creator 
{
    public:
        virtual unique_ptr<Product> createProduct() override
        {
            return unique_ptr<Product>(new Tprod());
        }
};

//product
class Product 
{
    public:
        virtual ~Product() = default;
        virtual void run() = 0;
};

class ConProduct1: public Product
{
    public:
        ConProduct1() 
        {
            cout << "Constructor ConProduct1\n";
        }
        virtual ~ConProduct1() 
        {
            cout << "Destructor ConProduct1\n";
        }

        virtual void run()
        {
            cout << "Run ConProduct1\n";
        }
};

class ConProduct2: public Product
{
    public:
        ConProduct2() 
        {
            cout << "Constructor ConProduct2\n";
        }
        virtual ~ConProduct2() 
        {
            cout << "Destructor ConProduct2\n";
        }

        virtual void run()
        {
            cout << "Run ConProduct2\n";
        }
};

class CrCreator
{
    public:
        template<class Tprod>
        static unique_ptr<Creator> createConCreator()
        {
            return unique_ptr<Creator>(new ConCreator<Tprod>());
        }
};

//solution
class Solution
{
    using CreateCreator = unique_ptr<Creator>(*)();
    using CallBackMap = map<size_t, CreateCreator>;

    public:
        Solution() = default;
        Solution(initializer_list<pair<size_t, CreateCreator>> list);

        bool registration(size_t id, CreateCreator createfun); //add to list
        bool check(size_t id) {return callback.erase(id) == 1;}

        unique_ptr<Creator> create(size_t id);
    private:
        CallBackMap callback;
};

Solution::Solution(initializer_list<pair<size_t, CreateCreator>> list)
{
    for (auto elem : list)
        this->registration(elem.first, elem.second);
}

bool Solution::registration(size_t id, CreateCreator createfun)
{
    return callback.insert(CallBackMap::value_type(id, createfun)).second;
}

unique_ptr<Creator> Solution::create(size_t id)
{
    CallBackMap::const_iterator it = callback.find(id);
    if (it == callback.end())
    {
        return nullptr;
    }
    return unique_ptr<Creator>((it->second)());
}
int main()
{
    shared_ptr<Solution> solution(new Solution({ {1, &CrCreator::createConCreator<ConProduct1>} }));
    
    solution->registration(2, &CrCreator::createConCreator<ConProduct2>);
    
    shared_ptr<Creator> cr(solution->create(2));
    shared_ptr<Product> ptr = cr->createProduct();
    ptr->run();
    return 0;
}