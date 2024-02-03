#ifndef class_Vector_h
#define class_Vector_h

#include <stdarg.h>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <memory>
#include <stdexcept>
#include <string.h>
#include <concepts>
#define EPS 1e-5

template <typename Type>
concept arithmetic = std::is_arithmetic_v<Type>;

template <typename Type, typename Type1>
concept is_convertable = requires(Type a, Type1 b)
{
    a = b;
    convertible_to<Type1, Type>;
};

template <typename Type>
concept is_container = requires(Type t)
{
    typename Type::value_type;
    typename Type::size_type;
    typename Type::iterator;
    typename Type::const_iterator;

    { t.begin() } noexcept -> same_as<typename Type::iterator>;
    { t.end() } noexcept -> same_as<typename Type::iterator>;

    { t.empty() } noexcept -> same_as<bool>;
    { t.size() } noexcept -> same_as<typename Type::size_type>;
};

template<typename Type>
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

    //????????????
    Vector();
    explicit Vector(size_t num_elements);
    explicit Vector(const Vector<Type>& vec);
    Vector(size_t num_elements, Type* vec);
    Vector(size_t num_elements, Type first, ...);
    Vector(std::initializer_list<Type> args);
    Vector(Vector<Type>&& vec) noexcept;

    template <is_container Type1>
    Vector(const Type1& container);

    template <is_convertable<Type> Type1>
    explicit Vector(const Vector<Type1>& vec);

    //??????????
    ~Vector();

    //????????? ????????????
    Vector<Type>& operator =(const Vector<Type>& vec);
    Vector<Type>& operator =(Vector<Type>&& vec) noexcept;
    Vector<Type>& operator =(std::initializer_list<Type> args);
    template <is_container Type1>
    Vector<Type>& operation = (const Type1 & container);
    template <is_convertable<Type> Type1>
    Vector<Type>& operator = (const Vector<Type1>& vec);


    //????????? ????????
    Vector<Type> operator +(const Vector<Type>&) const;
    Vector<Type> sum(const Vector<Type>&) const;
    Vector<Type>& operator +=(const Vector<Type>&);
    Vector<Type>& sumEqual(const Vector<Type>&);

    //????????? ?????????
    Vector<Type> operator -(const Vector<Type>&) const;
    Vector<Type> sub(const Vector<Type>&) const;
    Vector<Type>& operator -=(const Vector<Type>&);
    Vector<Type>& subEqual(const Vector<Type>&);

    //???????? ????????? ?? ?????
    Vector<Type> operator *(const Type& mult) const;
    Vector<Type> mulNum(const Type& mult) const;
    Vector<Type>& operator *=(const Type& mult);
    Vector<Type>& mulNumEqual(const Type& mult);
    template<arithmetic Type1>
    decltype(auto) operator * (const Type1& number) const;

    //???????? ??????? ?? ?????
    Vector<Type> operator /(const Type& div) const;
    Vector<Type> divNum(const Type& div) const;
    Vector<Type>& operator /=(const Type& div);
    Vector<Type>& divNumEqual(const Type& div);
    template<arithmetic Type1>
    decltype(auto) operator / (const Type1& number) const;

    //???????? ?????????? ????????????
    Vector<Type> operator &(const Vector<Type>& vec);
    Vector<Type> vectorMul(const Vector<Type>& vec);
    Vector<Type>& operator &=(const Vector<Type>& vec);
    Vector<Type>& vectorMulEqual(const Vector<Type>& vec);

    //???????? ?????????? ????????????
    value_type operator *(const Vector<Type>& vec) const;
    value_type scalarMul(const Vector<Type>& vec) const;

    //???????? ???????????? ?? ????????
    Vector<Type> operator ^(const Vector<Type>& vec) const;
    Vector<Type> mulElement(const Vector<Type>& vec) const;
    Vector<Type>& operator ^=(const Vector<Type>& vec);
    Vector<Type>& mulElementEqual(const Vector<Type>& vec);

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
    value_type len() const;

    Vector<Type> get_single_vector() const;
    double angle_between_vectors(const Vector<Type>&) const;
    bool is_collinearity(const Vector<Type>&) const;
    bool is_orthogonality(const Vector<Type>&) const;

    iterator begin() noexcept;
    iterator end() noexcept;
    iterator begin() const noexcept;
    iterator end() const noexcept;
    const_iterator constBegin() const noexcept;
    const_iterator constEnd() const noexcept;

private:
    std::shared_ptr<Type[]> data_list;

protected:
    Type sum_all_elem();
    void sum_vectors(Vector<Type>& result, const Vector<Type>& vec1, const Vector<Type>& vec2) const;
    void difference_vectors(Vector<Type>& result, const Vector<Type>& vec1, const Vector<Type>& vec2) const;
    void mult_vectors(Vector<Type>& result, const Vector<Type>& vec1, const Vector<Type>& vec2) const;
    void new_dyn_mem(size_t);
};

#endif
