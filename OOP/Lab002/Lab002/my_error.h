#pragma once

#include "BaseError.h"

class memError : public BaseError
{
public:
    explicit memError(
        char* filename,
        char* classname,
        int line,
        const char* info = "Can't allocate memory!\n") noexcept :
        BaseError(filename, classname, line, info) {};

    virtual const char* what() const noexcept
    {
        return msg;
    }
};

class emptyError : public BaseError
{
public:
    explicit emptyError(
        char* filename,
        char* classname,
        int line,
        const char* info = "Size must be > 0!\n") noexcept :
        BaseError(filename, classname, line, info) {};

    virtual const char* what() const noexcept
    {
        return msg;
    }
};

class indexError : public BaseError
{
public:
    explicit indexError(
        char* filename,
        char* classname,
        int line,
        const char* info = "Index out of range> 0!\n") noexcept :
        BaseError(filename, classname, line, info) {};

    virtual const char* what() const noexcept
    {
        return msg;
    }
};

class zero_divError : public BaseError
{
public:
    explicit zero_divError(
        char* filename,
        char* classname,
        int line,
        const char* info = "Divide on zero!\n") noexcept :
        BaseError(filename, classname, line, info) {};

    virtual const char* what() const noexcept
    {
        return msg;
    }
};

class deletedObj : public BaseError
{
public:
    explicit deletedObj(
        char* filename,
        char* classname,
        int line,
        const char* info = "Work with deleted object error!\n") noexcept :
        BaseError(filename, classname, line, info) {};

    virtual const char* what() const noexcept
    {
        return msg;
    }
};


