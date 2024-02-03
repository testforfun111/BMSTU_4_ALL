#pragma once
#include <time.h>
class BaseVector
{
public:
    BaseVector();
    virtual ~BaseVector() = 0;

    virtual bool empty() const = 0;
    virtual size_t size() const = 0;
    size_t print()
    {
        return this->num_elem;
    }
protected:
    size_t num_elem = 0;
};
