#pragma once

#include "BaseIter.h"
#include "my_error.h"
#include <iterator>
template<VectorType Type>
class Vector;

template<typename Type>
class Iterator : public BaseIter
{
public:
    using iterator_category = std::random_access_iterator_tag;
    using value_type = Type;
    using pointer = Type*;
    using reference = Type&;
    using difference_type = ptrdiff_t;

public:
    Iterator(const Iterator<Type>& iter);
    Iterator(const Vector<Type>& vec);

    virtual ~Iterator() = default;

    reference operator*();
    pointer operator->();
    reference operator [](int index);

    explicit operator bool() const;

    Iterator<Type>& operator=(const Iterator<Type>& iter);

    Iterator<Type>& operator+=(int n);
    Iterator<Type> operator+(int n) const;
    Iterator<Type>& operator++();
    Iterator<Type> operator++(int);

    Iterator<Type>& operator-=(int n);
    Iterator<Type> operator-(int n) const;
    Iterator<Type>& operator--();
    Iterator<Type> operator--(int);

    difference_type operator-(const Iterator<Type>& other) const;

    bool operator<=(const Iterator<Type>& b) const;
    bool operator<(const Iterator<Type>& b) const;
    bool operator>=(const Iterator<Type>& b) const;
    bool operator>(const Iterator<Type>& b) const;
    bool operator==(const Iterator<Type>& b) const;
    bool operator!=(const Iterator<Type>& b) const;

    bool check_exist() const;

private:
    std::weak_ptr<Type[]> ptr;
};
