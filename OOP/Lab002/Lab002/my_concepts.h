#pragma once
#include <concepts>
#include <iostream>
template <typename Type>
concept arithmetic = std::is_arithmetic_v<Type>;

template <typename Type>
concept VectorType = std::semiregular<Type>;

template <typename Type, typename Type1>
concept Convertable = requires(Type a, Type1 b)
{
    a = b;
    std::convertible_to<Type1, Type>;
};

template <typename Type>
concept container = requires(Type t)
{
    typename Type::value_type;
    typename Type::size_type;
    typename Type::iterator;
    typename Type::const_iterator;

    { t.begin() } noexcept -> std::same_as<typename Type::iterator>;
    { t.end() } noexcept -> std::same_as<typename Type::iterator>;

    { t.empty() } noexcept -> std::same_as<bool>;
    { t.size() } noexcept -> std::same_as<typename Type::size_type>;
};

template <typename Type>
concept iteratorc = requires(Type a)
{
    typename Type::iterator_category;
    typename Type::value_type;
    typename Type::difference_type;
    typename Type::pointer;
    typename Type::reference;
};

template <typename Type, typename Type1>
concept ConvertableIterator = std::is_convertible<Type, typename Type1::value_type>::value() && iteratorc<Type1>;

template <typename Type, typename Type1>
concept ConvertableContainer = std::is_convertible<Type, typename Type1::value_type>::value() && container<Type1>;

template <typename Type, typename Type1>
concept TypeAdded = requires(Type a, Type1 b)
{
    Convertable<Type, Type1>;
    {a + b}->std::convertible_to<Type>;
};

template <typename Type, typename Type1>
concept TypeSubtracted = requires(Type a, Type1 b)
{
    Convertable<Type, Type1>;
    {a - b}->std::convertible_to<Type>;
};

template <typename Type, typename Type1>
concept TypeMultiplied = requires(Type a, Type1 b)
{
    Convertable<Type, Type1>;
    {a* b}->std::convertible_to<Type>;
};

template <typename Type, typename Type1>
concept TypeDivided = requires(Type a, Type1 b)
{
    Convertable<Type, Type1>;
    {a / b}->std::convertible_to<Type>;
};

template <typename Type, typename Type1>
concept ArithmeticConvertable = std::is_arithmetic_v<Type1> && std::convertible_to<Type, Type1>;
