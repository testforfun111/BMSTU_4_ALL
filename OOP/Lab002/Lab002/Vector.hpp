#pragma once
#include <iostream>
#include <stdlib.h>
#include <cstddef>
#include <cmath>

#include "Vector.h"
#include "my_error.h"
#define M_PI 3.14

using namespace std;

template<typename Type>
Vector<Type>::Vector()
{
    num_elem = 0;
    new_dyn_mem(num_elem);
}

template<typename Type>
Vector<Type>::Vector(size_t num_elements)
{
    if (num_elements < 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    num_elem = num_elements;
    new_dyn_mem(num_elem);

    if (!data_list)
        throw memError(__FILE__, typeid(*this).name(), __LINE__);

    Iterator<Type> iter(*this);
    for (; iter; iter++)
        *iter = 0;
}

template<typename Type>
Vector<Type>::Vector(const Vector<Type>& vec)
{
    num_elem = vec.num_elem;
    new_dyn_mem(num_elem);

    Iterator<Type> iter_new(*this);
    Iterator<Type> iter(vec);
    for (; iter_new; iter++, iter_new++)
        *iter_new = *iter;
}

template<typename Type>
template<Convertable<Type> Type1>
Vector<Type>::Vector(const Vector<Type1>& vec)
{
    num_elem = vec.size();
    new_dyn_mem(num_elem);
    Iterator<Type> iter_new = this->begin();
    for (const auto& elem : vec)
    {
        *iter_new = elem;
        iter_new++;
    }
}

template<typename Type>
Vector<Type>::Vector(size_t num_elements, Type* vec)
{
    if (num_elements <= 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    num_elem = num_elements;
    new_dyn_mem(num_elem);

    Iterator<Type> iter(*this);
    for (size_t i = 0; iter; i++, iter++)
        *iter = vec[i];
}

template<typename Type>
Vector<Type>::Vector(size_t num_elements, Type& first, ...)
{
    if (num_elements <= 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    num_elem = num_elements;
    new_dyn_mem(num_elem);

    if (!data_list)
        throw memError(__FILE__, typeid(*this).name(), __LINE__);

    Iterator<Type> iter(*this);
    va_list ap;
    va_start(ap, first);
    for (; iter; iter++)
    {
        *iter = first;
        first = va_arg(ap, Type);
    }
    va_end(ap);
}

template<typename Type>
Vector<Type>::Vector(std::initializer_list<Type> args)
{
    if (args.size() == 0)
        Vector();

    num_elem = size_t(args.size());
    new_dyn_mem(num_elem);

    Iterator<Type> iter(*this);
    for (auto& element : args)
    {
        *iter = element;
        iter++;
    }
}

template<typename Type>
Vector<Type>::Vector(Vector<Type>&& vec) noexcept
{
    num_elem = vec.num_elem;
    this->data_list = vec.data_list;
    vec.num_elem = 0;
    vec.data_list = nullptr;
}

template<typename Type>
template<Convertable <Type> Type1>
Vector<Type>::Vector(Vector<Type1>&& vec) noexcept
{
    num_elem = vec.num_elem;
    this->data_list = vec.data_list;
    vec.num_elem = 0;
    vec.data_list = nullptr;
}

template<typename Type>
template<ConvertableContainer<Type> Type1>
Vector<Type>::Vector(const Type1& container)
{
    num_elem = container.size();
    new_dyn_mem(num_elem);
    Iterator<Type> iter_new(*this);
    Iterator<Type1> old_iter = container.begin();
    for (; iter_new; iter_new++, old_iter++)
        *iter_new = *old_iter;
}

template <typename Type>
template<ConvertableIterator<Type> Type1>
Vector<Type>::Vector(const Type1& begin, const Type1& end)
{
    int len = 0;
    for (Type1 iter = begin; iter != end; iter++)
        len++;
    new_dyn_mem(len);
    num_elem = len;
    Iterator<Type> iter_new(*this);

    for (Type1 iter = begin; iter != end; iter++)
        *iter_new = *iter;
}

template<typename Type>
Vector<Type>::~Vector()
{
    if (data_list)
        data_list.reset();
}

template<typename Type>
Vector<Type>& Vector<Type>::operator =(const Vector<Type>& vec)
{
    num_elem = vec.num_elem;
    new_dyn_mem(num_elem);

    Iterator<Type> iter_new(*this);
    Iterator<Type> iter(vec);
    for (; iter_new; iter_new++, iter++)
        *iter_new = *iter;

    return *this;
}

template<typename Type>
template<Convertable<Type> Type1>
Vector<Type>& Vector<Type>::operator =(const Vector<Type1>& vec)
{
    num_elem = vec.num_elem;
    new_dyn_mem(num_elem);

    Iterator<Type> iter_new(*this);
    Iterator<Type1> iter(vec);

    for (; iter_new; iter_new++, iter++)
        *iter_new = static_cast<Type>(*iter);
    return *this;
}

template<typename Type>
Vector<Type>& Vector<Type>::operator =(const Type& container)
{
    num_elem = container.size();
    new_dyn_mem(num_elem);

    Iterator<Type> iter_new = this->begin();
    Iterator<Type> iter_old = container.begin();
    for (; iter_new; iter_new++, iter_old++)
        *iter_new = *iter_old;
    return *this;
}

template<typename Type>
template<ConvertableContainer<Type> Type1>
Vector<Type>& Vector<Type>::operator =(const Type1& containter)
{
    num_elem = container.size();
    new_dyn_mem(num_elem);

    Iterator<Type> iter_new = this->begin();
    Iterator<Type1> iter_old = containter.begin();

    for (; iter_new; iter_new++, iter_old++)
        *iter_new = static_cast<Type>(*iter_old);
    return *this;
}

template<typename Type>
Vector<Type>& Vector<Type>::operator =(Vector<Type>&& vec) noexcept
{
    num_elem = vec.num_elem;
    new_dyn_mem(num_elem);
    data_list = vec.data_list;
    vec.data_list.reset();

    return *this;
}

template<typename Type>
Vector<Type>& Vector<Type>::operator =(std::initializer_list<Type> args)
{
    num_elem = size_t(args.size());
    new_dyn_mem(num_elem);

    Iterator<Type> iter(*this);
    for (auto& element : args)
    {
        *iter = element;
        iter++;
    }

    return *this;
}

template <typename Type>
template <Convertable<Type> Type1>
Vector<Type>& Vector<Type>::operator = (std::initializer_list<Type1> args)
{
    num_elem = size_t(args.size());
    new_dyn_mem(num_elem);

    Iterator<Type> iter(*this);

    for (auto& element : args)
    {
        *iter = element;
        iter++;
    }
    return *this;
}

template <typename Type>
template<TypeAdded<Type> Type1>
Vector<Type> Vector<Type>::operator +(const Vector<Type1>& vec) const
{
    if (num_elem <= 0 || vec.num_elem <= 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    size_t max_len = max(num_elem, vec.num_elem);
    Vector<Type> new_vector(max_len);
    sum_vectors(new_vector, *this, vec);

    return new_vector;
}

template <typename Type>
template<TypeAdded<Type> Type1>
Vector<Type>& Vector<Type>::operator +=(const Vector<Type1>& vec)
{
    if (num_elem <= 0 || vec.num_elem <= 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    sum_vectors(*this, *this, vec);

    return *this;
}

template <typename Type>
template<TypeAdded<Type> Type1>
Vector<Type> Vector<Type>::sum(const Vector<Type1>& vector) const
{
    return operator+(vector);
}

template <typename Type>
template<TypeAdded<Type> Type1>
Vector<Type>& Vector<Type>::sumEqual(const Vector<Type1>& vector)
{
    return operator+=(vector);
}

template <typename Type>
template<TypeSubtracted<Type> Type1>
Vector<Type> Vector<Type>::operator -(const Vector<Type1>& vec) const
{
    if (num_elem < 0 || vec.num_elem < 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    size_t max_len = max(num_elem, vec.num_elem);
    Vector<Type> new_vector(max_len);
    difference_vectors(new_vector, *this, vec);

    return new_vector;
}

template <typename Type>
template<TypeSubtracted<Type> Type1>
Vector<Type>& Vector<Type>::operator -=(const Vector<Type1>& vec)
{
    if (num_elem < 0 || vec.num_elem < 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    difference_vectors(*this, *this, vec);

    return *this;
}

template<typename Type>
template<TypeSubtracted<Type> Type1>
Vector<Type> Vector<Type>::sub(const Vector<Type1>& vector) const
{
    return operator -(vector);
}

template<typename Type>
template<TypeSubtracted<Type> Type1>
Vector<Type>& Vector<Type>::subEqual(const Vector<Type1>& vector)
{
    return operator -=(vector);
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector<Type> Vector<Type>::operator &(const Vector<Type1>& vec)
{
    if (num_elem != 3)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    double x = data_list[1] * vec.data_list[2] - data_list[2] * vec.data_list[1];
    double y = data_list[2] * vec.data_list[0] - data_list[0] * vec.data_list[2];
    double z = data_list[0] * vec.data_list[1] - data_list[1] * vec.data_list[0];
    Vector<Type> new_vector(3, x, y, z);
    return new_vector;
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector<Type>& Vector<Type>::operator &=(const Vector<Type1>& vec)
{
    if (num_elem != 3)
        return *(new Vector<Type>);

    double x = data_list[1] * vec.data_list[2] - data_list[2] * vec.data_list[1];
    double y = data_list[2] * vec.data_list[0] - data_list[0] * vec.data_list[2];
    double z = data_list[0] * vec.data_list[1] - data_list[1] * vec.data_list[0];

    *this = Vector<Type>(3, x, y, z);
    return *this;
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector<Type> Vector<Type>::commutative (const Vector<Type1>& vec)
{
    if (num_elem != 3)
        return *(new Vector<Type>);

    double x = vec.data_list[1] * data_list[2] - vec.data_list[2] * data_list[1];
    double y = vec.data_list[2] * data_list[0] - vec.data_list[0] * data_list[2];
    double z = vec.data_list[0] * data_list[1] - vec.data_list[1] * data_list[0];
    *this = Vector<Type>(3, x, y, z);
    return *this;
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector<Type> Vector<Type>::operator *(const Type1& mult) const
{
    if (num_elem <= 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);
    Vector<Type> new_vector(*this);
    Iterator<Type> iter(new_vector);
    for (; iter; iter++)
        *iter *= mult;

    return new_vector;
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector<Type>& Vector<Type>::operator *=(const Type1& mult)
{
    if (num_elem <= 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    Iterator<Type> iter(*this);
    for (; iter; iter++)
        *iter *= mult;

    return *this;
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector<Type> Vector<Type>::mulNum(const Type1& mult) const
{
    return operator *(mult);
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector<Type>& Vector<Type>::mulNumEqual(const Type1& mult)
{
    return operator *=(mult);
}

template <typename Type>
template<TypeMultiplied<Type> Type1>
Type Vector<Type>::operator *(const Vector<Type1>& vec) const
{
    if (num_elem < 0 || vec.num_elem < 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    size_t max_len = max(num_elem, vec.num_elem);
    Vector<Type> new_vector(max_len);
    mult_vectors(new_vector, *this, vec);

    return new_vector.sum_all_elem();
}

template <typename Type>
template<TypeMultiplied<Type> Type1>
Type Vector<Type>::scalarMul(const Vector<Type1>& vec) const
{
    return operator *(vec);
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector <Type> Vector <Type>::operator ^(const Vector<Type1>& vec) const
{
    if (num_elem < 0 || vec.num_elem < 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);
    size_t max_len = max(num_elem, vec.num_elem);
    Vector<Type> new_vector(max_len);
    mult_vectors(new_vector, *this, vec);
    return new_vector;
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector<Type>& Vector <Type>::operator ^=(const Vector<Type1>& vec)
{
    if (num_elem < 0 || vec.num_elem < 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);
    mult_vectors(*this, *this, vec);
    return *this;
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector <Type> Vector <Type>::mulElement(const Vector<Type1>& vec) const
{
    return operator ^(vec);
}

template<typename Type>
template<TypeMultiplied<Type> Type1>
Vector<Type>& Vector <Type>::mulElementEqual(const Vector<Type1>& vec)
{
    return operator ^=(vec);
}

template<typename Type>
template<TypeDivided<Type> Type1>
Vector<Type> Vector<Type>::operator /(const Type1& div) const
{
    if (!div)
        throw zero_divError(__FILE__, typeid(*this).name(), __LINE__);

    Type div_new = 1 / div;
    Vector<Type>new_vector(*this);
    new_vector *= div_new;

    return new_vector;
}

template<typename Type>
template<TypeDivided<Type> Type1>
Vector<Type>& Vector<Type>::operator /=(const Type1& div)
{
    if (!div)
        throw zero_divError(__FILE__, typeid(*this).name(), __LINE__);

    Type div_new = 1 / div;
    *this *= div_new;

    return *this;
}

template<typename Type>
template<TypeDivided<Type> Type1>
Vector<Type> Vector<Type>::divNum(const Type1& div) const
{
    return operator /(div);
}

template<typename Type>
template<TypeDivided<Type> Type1>
Vector<Type>& Vector<Type>::divNumEqual(const Type1& div)
{
    return operator /=(div);
}



template <typename Type>
Vector<Type> Vector<Type>::operator -()
{
    Vector<Type> new_vector(*this);
    Iterator<Type> iter(new_vector);
    for (; iter; iter++)
        *iter = -*iter;

    return new_vector;
}

template <typename Type>
Vector<Type> Vector<Type>::neg()
{
    return operator -();
}

template <typename Type>
bool Vector<Type>::operator ==(const Vector<Type>& vec) const
{
    int equal = 1;
    if (num_elem != vec.num_elem)
        return false;
    else
    {
        Iterator<Type> iter1(*this);
        Iterator<Type> iter2(vec);

        for (; iter1 && equal; iter1++, iter2++)
            if (fabs(*iter1 - *iter2) > EPS)
                equal = 0;
    }
    return equal;
}

template <typename Type>
bool Vector<Type>::operator !=(const Vector<Type>& vec) const
{
    if (*this == vec)
        return false;
    else
        return true;
}

template <typename Type>
bool Vector<Type>::isEqual(const Vector<Type>& vec) const
{
    return operator ==(vec);
}

template <typename Type>
bool Vector<Type>::isNotEqual(const Vector<Type>& vec) const
{
    return operator !=(vec);
}

template<typename Type>
Type& Vector<Type>::operator [](size_t index)
{
    return get_elem_Vector(index);
}

template<typename Type>
const Type& Vector<Type>::operator [](size_t index) const
{
    return get_elem_Vector(index);
}

template<typename Type>
Type& Vector<Type>::get_elem_Vector(size_t index)
{
    if (index < 0 || index >= num_elem)
        throw indexError(__FILE__, typeid(*this).name(), __LINE__);

    Iterator<Type> iter(*this);
    for (size_t i = 0; i < index; i++, iter++)
        ;

    return *iter;
}

template<typename Type>
const Type& Vector<Type>::get_elem_Vector(size_t index) const
{
    if (index < 0 || index >= num_elem)
        throw indexError(__FILE__, typeid(*this).name(), __LINE__);

    Iterator<Type> iter(*this);
    for (size_t i = 0; i < index; i++, iter++)
        ;

    return *iter;
}

template<typename Type>
bool Vector<Type>::set_elem_Vector(size_t index, const Type& num)
{
    if (index < 0 || index >= num_elem)
        return false;

    get_elem_Vector(index) = num;
    return true;
}

template<typename Type>
bool Vector<Type>::is_single() const
{
    if (abs(this->len() - 1) < EPS)
        return true;
    else
        return false;
}

template<typename Type>
bool Vector<Type>::is_zero() const
{
    if (this->len() == 0)
        return true;
    else
        return false;
}

template<typename Type>
size_t Vector<Type>::size() const
{
    return num_elem;
}

template<typename Type>
bool Vector<Type>::empty() const
{
    return num_elem == 0;
}

template<typename Type>
Type Vector<Type>::len(void) const
{
    if (num_elem < 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    Iterator<Type> iter(*this);
    double sum = 0;
    for (; iter; iter++)
        sum += *iter * *iter;

    return sqrt(sum);
}

template<typename Type>
Vector<Type> Vector<Type>::get_single_vector() const
{
    Vector<Type> new_vector(*this);
    Type len = this->len();

    Iterator<Type> iter(new_vector);
    for (; iter; iter++)
        *iter /= len;

    return new_vector;
}

template<typename Type>
double Vector<Type>::angle_between_vectors(const Vector<Type>& vec) const
{
    if (!this->len() || !vec.len())
        throw zero_divError(__FILE__, typeid(*this).name(), __LINE__);

    double angle = (*this * vec) / (this->len() * vec.len());
    return acos(angle) * 180 / M_PI;
}

template<typename Type>
bool Vector<Type>::is_collinearity(const Vector<Type>& vec) const
{
    if (this->angle_between_vectors(vec) < EPS)
        return true;
    else
        return false;
}

template<typename Type>
bool Vector<Type>::is_orthogonality(const Vector<Type>& vec) const
{
    if (abs(this->angle_between_vectors(vec) - 90) < EPS)
        return true;
    else
        return false;
}

template<typename Type>
Iterator<Type> Vector<Type>::begin() noexcept
{
    Iterator<Type> iterator(*this);
    return iterator;
}

template<typename Type>
Iterator<Type> Vector<Type>::end() noexcept
{
    Iterator<Type> iterator(*this);
    return iterator + size;
}

template<typename Type>
Iterator<Type> Vector<Type>::begin() const noexcept
{
    Iterator<Type> constIterator(*this);
    return constIterator;
}

template<typename Type>
Iterator<Type> Vector<Type>::end() const noexcept
{
    Iterator<Type> constIterator(*this);
    return constIterator + this->num_elem;
}

template<typename Type>
Iterator<Type> Vector<Type>::rend() noexcept
{
    Iterator<Type> constIterator(*this);
    return constIterator;
}

template<typename Type>
Iterator<Type> Vector<Type>::rbegin() noexcept
{
    Iterator<Type> iter(*this);
    return iter + this->num_elem;
}

template<typename Type>
ConstIterator<Type> Vector<Type>::c_begin() const noexcept
{
    ConstIterator<Type> Iter(*this);
    return Iter;
}

template<typename Type>
ConstIterator<Type> Vector<Type>::c_end() const noexcept
{
    ConstIterator<Type> Iter(*this);
    return Iter + this->num_elem;
}

template<typename Type>
ConstIterator<Type> Vector<Type>::cr_begin() const noexcept
{
    ConstIterator<Type> Iter(*this);
    return Iter + this->num_elem;
}

template<typename Type>
ConstIterator<Type> Vector<Type>::cr_end() const noexcept
{
    ConstIterator<Type> Iter(*this);
    return Iter;
}

template<typename Type>
Type Vector<Type>::sum_all_elem()
{
    if (num_elem <= 0)
        throw emptyError(__FILE__, typeid(*this).name(), __LINE__);

    Iterator<Type> iter(*this);
    Type sum = 0;
    for (; iter; iter++)
        sum += *iter;

    return sum;
}

template <typename Type>
template<TypeAdded<Type> Type1>
void Vector<Type>::sum_vectors(Vector<Type>& result, const Vector<Type>& vec1, const Vector<Type1>& vec2) const
{
    Iterator<Type> iter_result(result);
    Iterator<Type> iter_vec1(vec1);
    Iterator<Type1> iter_vec2(vec2);
    for (size_t i = 0; iter_result; i++, iter_result++, iter_vec1++, iter_vec2++)
    {
        if (i >= vec1.num_elem)
            *iter_result = *iter_vec2;
        else if (i >= vec2.num_elem)
            *iter_result = *iter_vec1;
        else
            *iter_result = *iter_vec1 + *iter_vec2;
    }
}

template <typename Type>
template<TypeSubtracted<Type> Type1>
void Vector<Type>::difference_vectors(Vector<Type>& result, const Vector<Type>& vec1, const Vector<Type1>& vec2) const
{
    Iterator<Type> iter_result(result);
    Iterator<Type> iter_vec1(vec1);
    Iterator<Type1> iter_vec2(vec2);
    for (size_t i = 0; iter_result; i++, iter_result++, iter_vec1++, iter_vec2++)
    {
        if (i >= vec1.num_elem)
            *iter_result = -*iter_vec2;
        else if (i >= vec2.num_elem)
            *iter_result = *iter_vec1;
        else
            *iter_result = *iter_vec1 - *iter_vec2;
    }
}

template <typename Type>
template<TypeMultiplied<Type> Type1>
void Vector<Type>::mult_vectors(Vector<Type>& result, const Vector<Type>& vec1, const Vector<Type1>& vec2) const
{
    Iterator<Type> iter_result(result);
    Iterator<Type> iter_vec1(vec1);
    Iterator<Type1> iter_vec2(vec2);
    for (size_t i = 0; iter_result; i++, iter_result++, iter_vec1++, iter_vec2++)
    {
        if (i >= vec1.num_elem || i >= vec2.num_elem)
            *iter_result = 0;
        else
            *iter_result = *iter_vec1 * *iter_vec2;
    }
}

template<typename Type>
std::ostream& operator <<(std::ostream& os, const Vector<Type>& vec)
{
    Iterator<Type> iter(vec);

    if (!iter)
    {
        os << "Vector is empty.";
        return os;
    }

    os << '(' << *iter;
    for (iter++; iter; iter++)
        os << ", " << *iter;
    os << ')';

    return os;
}

template <typename Type>
void Vector<Type>::new_dyn_mem(size_t num_elements)
{
    data_list.reset(new Type[num_elements]);
}