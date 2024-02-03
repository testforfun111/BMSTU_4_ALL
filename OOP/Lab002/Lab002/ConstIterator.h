#pragma once

#include "BaseIter.h"
#include "my_error.h"
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

    difference_type operator-(ConstIterator<Type>& other) const;

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