#pragma once
#include <iostream>
#include <memory>

class BaseIter
{
public:
    BaseIter() = default;
    virtual ~BaseIter() = 0;

protected:
    size_t index = 0;
    size_t num_elem = 0;
};