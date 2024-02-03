#pragma once
#include <stdarg.h>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <memory>
#include <stdexcept>
#include <string.h>
#include <concepts>
#include "my_concepts.h"
#include "BaseVector.h"
#include "Iterator.h"
#include "ConstIterator.h"
#define EPS 1e-5

template<VectorType Type>
class Vector : public BaseVector
{
public:
    using value_type = Type;
    using iterator = Iterator<Type>;
    using const_iterator = ConstIterator<Type>;
    using size_type = size_t;
public:
    friend class Iterator<Type>;
    friend class ConstIterator<Type>;

    Vector();
    explicit Vector(size_t num_elements);
    explicit Vector(const Vector<Type>& vec);
    template <Convertable<Type> Type1>
    explicit Vector(const Vector<Type1>& vec);
    Vector(size_t num_elements, Type* vec);
    Vector(size_t num_elements, Type& first, ...);
    Vector(std::initializer_list<Type> args);
    Vector(Vector<Type>&& vec) noexcept;
    template <Convertable <Type> Type1>   //ko can
    Vector(Vector<Type1>&& vec) noexcept;
    template <ConvertableContainer<Type> Type1>
    Vector(const Type1& container);
    template <ConvertableIterator<Type> Type1>
    Vector(const Type1& begin, const Type1& end);

    ~Vector();

    Vector<Type>& operator =(const Vector<Type>& vec);
    template <Convertable<Type> Type1>
    Vector<Type>& operator = (const Vector<Type1>& vec);
    Vector<Type>& operator =(const Type& container);
    template <ConvertableContainer<Type> Type1>
    Vector<Type>& operator =(const Type1& container);
    Vector<Type>& operator =(Vector<Type>&& vec) noexcept;
    Vector<Type>& operator =(std::initializer_list<Type> args);
    template <Convertable<Type> Type1>
    Vector<Type>& operator =(std::initializer_list<Type1> args);

    template<TypeAdded<Type> Type1>
    Vector<Type> operator +(const Vector<Type1>&) const;
    template<TypeAdded<Type> Type1>
    Vector<Type> sum(const Vector<Type1>&) const;
    template<TypeAdded<Type> Type1>
    Vector<Type>& operator +=(const Vector<Type1>&);
    template<TypeAdded<Type> Type1>
    Vector<Type>& sumEqual(const Vector<Type1>&);

    template<TypeSubtracted<Type> Type1>
    Vector<Type> operator -(const Vector<Type1>&) const;
    template<TypeSubtracted<Type> Type1>
    Vector<Type> sub(const Vector<Type1>&) const;
    template<TypeSubtracted<Type> Type1>
    Vector<Type>& operator -=(const Vector<Type1>&);
    template<TypeSubtracted<Type> Type1>
    Vector<Type>& subEqual(const Vector<Type1>&);

    template<TypeMultiplied<Type> Type1>
    Vector<Type> operator &(const Vector<Type1>& vec);
    template<TypeMultiplied<Type> Type1>
    Vector<Type>& operator &=(const Vector<Type1>& vec);
    template<TypeMultiplied<Type> Type1>
    Vector<Type> commutative (const Vector<Type1>& vec);

    template<TypeMultiplied<Type> Type1>
    Vector<Type> operator *(const Type1& mult) const;
    template<TypeMultiplied<Type> Type1>
    Vector<Type> mulNum(const Type1& mult) const;
    template<TypeMultiplied<Type> Type1>
    Vector<Type>& operator *=(const Type1& mult);
    template<TypeMultiplied<Type> Type1>
    Vector<Type>& mulNumEqual(const Type1& mult);

    template<TypeMultiplied<Type> Type1>
    Type operator *(const Vector<Type1>& vec) const;
    template<TypeMultiplied<Type> Type1>
    Type scalarMul(const Vector<Type1>& vec) const;

    template<TypeMultiplied<Type> Type1>
    Vector<Type> operator ^(const Vector<Type1>& vec) const;
    template<TypeMultiplied<Type> Type1>
    Vector<Type> mulElement(const Vector<Type1>& vec) const;
    template<TypeMultiplied<Type> Type1>
    Vector<Type>& operator ^=(const Vector<Type1>& vec);
    template<TypeMultiplied<Type> Type1>
    Vector<Type>& mulElementEqual(const Vector<Type1>& vec);

    template<TypeDivided<Type> Type1>
    Vector<Type> operator /(const Type1& div) const;
    template<TypeDivided<Type> Type1>
    Vector<Type> divNum(const Type1& div) const;
    template<TypeDivided<Type> Type1>
    Vector<Type>& operator /=(const Type1& div);
    template<TypeDivided<Type> Type1>
    Vector<Type>& divNumEqual(const Type1& div);

    Vector<Type> operator -();
    Vector<Type> neg();

    bool operator ==(const Vector<Type>&) const;
    bool operator !=(const Vector<Type>&) const;
    bool isEqual(const Vector<Type>&) const;
    bool isNotEqual(const Vector<Type>&) const;

    Type& operator [](size_t index);
    const Type& operator [](size_t index) const;
    Type& get_elem_Vector(size_t index);
    const Type& get_elem_Vector(size_t index) const;
    bool set_elem_Vector(size_t index, const Type& vec);

    bool is_zero() const;
    bool is_single() const;
    bool empty() const;
    size_t size() const;
    Type len() const;

    Vector<Type> get_single_vector() const;
    double angle_between_vectors(const Vector<Type>&) const;
    bool is_collinearity(const Vector<Type>&) const;
    bool is_orthogonality(const Vector<Type>&) const;

    iterator begin() noexcept;
    iterator end() noexcept;
    iterator begin() const noexcept;
    iterator end() const noexcept;
    iterator rbegin() noexcept;
    iterator rend() noexcept;
    const_iterator c_begin() const noexcept;
    const_iterator c_end() const noexcept;
    const_iterator cr_begin() const noexcept;
    const_iterator cr_end() const noexcept;
private:
    std::shared_ptr<Type[]> data_list;

protected:
    Type sum_all_elem();
    template<TypeAdded<Type> Type1>
    void sum_vectors(Vector<Type>& result, const Vector<Type>& vec1, const Vector<Type1>& vec2) const;
    template<TypeSubtracted<Type> Type1>
    void difference_vectors(Vector<Type>& result, const Vector<Type>& vec1, const Vector<Type1>& vec2) const;
    template<TypeMultiplied<Type> Type1>
    void mult_vectors(Vector<Type>& result, const Vector<Type>& vec1, const Vector<Type1>& vec2) const;
    void new_dyn_mem(size_t);
};
