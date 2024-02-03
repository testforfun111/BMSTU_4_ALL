#ifndef BaseVector_h
#define BaseVector_h

#include <time.h>
class BaseVector
{
    public:
        BaseVector();
        virtual ~BaseVector() = 0;

        virtual bool empty() const = 0;
        virtual size_t size() const = 0;

    protected:
        size_t num_elem = 0;
};

#endif /* BaseVector_h */
