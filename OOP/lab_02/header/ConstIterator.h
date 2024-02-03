#ifndef Const_Iter_h
#define Const_Iter_h

#include "BaseIter.h"
#include "my_errors.h"
// #include <Iterator>
template<class Type>
class Vector;

template<typename Type>
class ConstIterator : public BaseIter
{
    public:
        using iterator_category = std::random_access_iterator_tag;
        using value_type = Type;
        using pointer = Type*;
        using reference = Type&;
        using difference_type = ptrdiff_t;

    public:
        ConstIterator(const ConstIterator<Type>& iter);
        ConstIterator(const Vector<Type>& vec);
        // ConstIterator()
        virtual ~ConstIterator() = default;
        
        const reference operator*() const;
        const pointer operator->() const;
        operator bool() const;

        ConstIterator<Type>& operator=(const ConstIterator<Type>& iter);

        ConstIterator<Type>& operator+=(int n);
        ConstIterator<Type> operator+(int n) const;
        ConstIterator<Type>& operator++();
        ConstIterator<Type> operator++(int);

        ConstIterator<Type>& operator-=(int n);
        ConstIterator<Type> operator-(int n) const;
        ConstIterator<Type>& operator--();
        ConstIterator<Type> operator--(int);

        bool operator<=(const ConstIterator<Type>& b) const;
        bool operator<(const ConstIterator<Type>& b) const;
        bool operator>=(const ConstIterator<Type>& b) const;
        bool operator>(const ConstIterator<Type>& b) const;
        bool operator==(const ConstIterator<Type>& b) const;
        bool operator!=(const ConstIterator<Type>& b) const;

        bool check_exist() const;

    private:
        std::weak_ptr<Type[]> ptr;
};

template<class Type>
ConstIterator<Type>::ConstIterator(const Vector<Type>& vec)
{
    index = 0;
    num_elem = vec.num_elem;
    ptr = vec.data_list;
}

template<class Type>
ConstIterator<Type>::ConstIterator(const ConstIterator<Type>& iter)
{
    ptr = iter.ptr;
    index = iter.index;
    num_elem = iter.num_elem;
}

template<class Type>
const typename ConstIterator<Type>::reference ConstIterator<Type>::operator*() const
{
    check_exist();
    std::shared_ptr<Type[]> copy_ptr = ptr.lock();
    return copy_ptr[index];
}

template<class Type>
const typename ConstIterator<Type>::pointer ConstIterator<Type>::operator->() const
{
    check_exist();
    std::shared_ptr<Type[]> copy_ptr = ptr.lock();
    return copy_ptr.get() + index;
}

template<class Type>
ConstIterator<Type>& ConstIterator<Type>::operator=(const ConstIterator<Type>& iter)
{
    check_exist();
    ptr = iter.ptr;
    index = iter.index;
    num_elem = iter.num_elem;
    return *this;
}

template<class Type>
ConstIterator<Type>& ConstIterator<Type>::operator+=(int n)
{
    check_exist();
    index += n;

    return *this;
}

template<class Type>
ConstIterator<Type> ConstIterator<Type>::operator+(int n) const
{
    check_exist();
    ConstIterator<Type> iter(*this);
    if (index + n <= num_elem)
        iter += n;

    return iter;
}

template<class Type>
ConstIterator<Type> ConstIterator<Type>::operator++(int)
{
    check_exist();
    ConstIterator<Type> it(*this);

    if (index < num_elem)
        ++(*this);

    return it;
}

template<class Type>
ConstIterator<Type>& ConstIterator<Type>::operator++()
{
    check_exist();
    if (index < num_elem)
        ++index;

    return *this;
}

template<class Type>
ConstIterator<Type>& ConstIterator<Type>::operator-=(int n)
{
    check_exist();
    if (index >= n - 1)
        index -= n;

    return *this;
}

template<class Type>
ConstIterator<Type> ConstIterator<Type>::operator-(int n) const
{
    check_exist();

    ConstIterator<Type> iter(*this);
    if (index >= n - 1)
        iter -= n;

    return iter;
}

template<class Type>
ConstIterator<Type> ConstIterator<Type>::operator--(int)
{
    check_exist();
    ConstIterator<Type> it(*this);
    if (index >= 0)
        --(*this);

    return *it;
}

template<class Type>
ConstIterator<Type>& ConstIterator<Type>::operator--()
{
    check_exist();
    if (index >= 0)
        --index;

    return *this;
}

template<class Type>
bool ConstIterator<Type>::operator<=(const ConstIterator<Type>& iter) const
{
    check_exist();

    return ptr <= iter.ptr;
}

template<class Type>
bool ConstIterator<Type>::operator<(const ConstIterator<Type>& iter) const
{
    check_exist();

    return ptr < iter.ptr;
}

template<class Type>
bool ConstIterator<Type>::operator>=(const ConstIterator<Type>& b) const
{
    check_exist();

    return ptr >= b.ptr;
}

template<class Type>
bool ConstIterator<Type>::operator>(const ConstIterator<Type>& b) const
{
    check_exist();

    return ptr > b.ptr;
}

template<class Type>
bool ConstIterator<Type>::operator==(const ConstIterator<Type>& iter) const
{
    check_exist();

    return ptr == iter.ptr;
}

template<class Type>
bool ConstIterator<Type>::operator!=(const ConstIterator<Type>& iter) const
{
    check_exist();

    return ptr != iter.ptr;
}

template<class Type>
ConstIterator<Type>::operator bool() const
{
    check_exist();
    bool res = true;
    if (index >= num_elem || index < 0 || (num_elem == 0))
        res = false;
    return res;
}

template<class Type>
bool ConstIterator<Type>::check_exist() const
{
    if (!ptr.expired())
        return true;

    throw deletedObj();
    return false;
}

#endif /* class_Iter_h */
