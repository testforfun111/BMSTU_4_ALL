#pragma once

#include "Iterator.h"

template<class Type>
Iterator<Type>::Iterator(const Vector<Type>& vec)
{
    index = 0;
    num_elem = vec.num_elem;
    ptr = vec.data_list;
}

template<class Type>
Iterator<Type>::Iterator(const Iterator<Type>& iter)
{
    ptr = iter.ptr;
    index = iter.index;
    num_elem = iter.num_elem;
}

template<class Type>
typename Iterator<Type>::reference Iterator<Type>::operator*()
{
    check_exist();
    std::shared_ptr<Type[]> copy_ptr = ptr.lock();
    return copy_ptr[index];
}

template<class Type>
typename Iterator<Type>::pointer Iterator<Type>::operator->()
{
    check_exist();
    std::shared_ptr<Type[]> copy_ptr = ptr.lock();
    return copy_ptr.get() + index;
}

template<class Type>
typename Iterator<Type>::reference Iterator<Type>::operator [](int index)
{
    check_exist();
    std::shared_ptr<Type[]> copy_ptr = ptr.lock();
    return *(copy_ptr.get() + this->index + index);
}

template<class Type>
Iterator<Type>& Iterator<Type>::operator=(const Iterator<Type>& iter)
{
    check_exist();
    ptr = iter.ptr;
    index = iter.index;
    num_elem = iter.num_elem;
    return *this;
}

template<class Type>
Iterator<Type>& Iterator<Type>::operator+=(int n)
{
    check_exist();
    index += n;

    return *this;
}

template<class Type>
Iterator<Type> Iterator<Type>::operator+(int n) const
{
    check_exist();
    Iterator<Type> iter(*this);
    if (index + n <= num_elem)
        iter += n;

    return iter;
}

template<class Type>
Iterator<Type> Iterator<Type>::operator++(int)
{
    check_exist();
    Iterator<Type> it(*this);

    if (index < num_elem)
        ++(*this);

    return it;
}

template<class Type>
Iterator<Type>& Iterator<Type>::operator++()
{
    check_exist();
    if (index < num_elem)
        ++index;

    return *this;
}

template<class Type>
Iterator<Type>& Iterator<Type>::operator-=(int n)
{
    check_exist();
    if (index >= n - 1)
        index -= n;

    return *this;
}

template<class Type>
Iterator<Type> Iterator<Type>::operator-(int n) const
{
    check_exist();

    Iterator<Type> iter(*this);
    if (index >= n - 1)
        iter -= n;

    return iter;
}

template<class Type>
Iterator<Type> Iterator<Type>::operator--(int)
{
    check_exist();
    Iterator<Type> it(*this);
    if (index >= 0)
        --(*this);

    return *it;
}

template<class Type>
Iterator<Type>& Iterator<Type>::operator--()
{
    check_exist();
    if (index >= 0)
        --index;

    return *this;
}

template <class Type>
Iterator<Type>::difference_type Iterator<Type>::operator - (const Iterator<Type>& other) const
{
    check_exist();
    return this->index - other.index;
}
template<class Type>
bool Iterator<Type>::operator<=(const Iterator<Type>& iter) const
{
    check_exist();

    return ptr <= iter.ptr;
}

template<class Type>
bool Iterator<Type>::operator<(const Iterator<Type>& iter) const
{
    check_exist();

    return ptr < iter.ptr;
}

template<class Type>
bool Iterator<Type>::operator>=(const Iterator<Type>& b) const
{
    check_exist();

    return ptr >= b.ptr;
}

template<class Type>
bool Iterator<Type>::operator>(const Iterator<Type>& b) const
{
    check_exist();

    return ptr > b.ptr;
}

template<class Type>
bool Iterator<Type>::operator==(const Iterator<Type>& iter) const
{
    check_exist();

    return ptr == iter.ptr;
}

template<class Type>
bool Iterator<Type>::operator!=(const Iterator<Type>& iter) const
{
    check_exist();

    return ptr != iter.ptr;
}

template<class Type>
typename Iterator<Type>::difference_type Iterator<Type>::operator-(const Iterator<Type>& other) const
{
    check_exist();
    Iterator<Type> min;
    Iterator<Type> max;

    if (*this < other)
    {
        min = *this;
        max = other;
    }
    else
    {
        min = other;
        max = *this;
    }
    ptrdiff_t count = 0;
    for (Iterator<Type> i = min; i < max; i++, count++);
    return count;
}

template<class Type>
Iterator<Type>::operator bool() const
{
    check_exist();
    bool res = true;
    if (index >= num_elem || index < 0 || (num_elem == 0))
        res = false;
    return res;
}

template<class Type>
bool Iterator<Type>::check_exist() const
{
    if (!ptr.expired())
        return true;

    throw deletedObj(__FILE__, typeid(*this).name(), __LINE__);
    return false;
}