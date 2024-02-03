#pragma once

#include <exception>
#include <string>
#include <string.h>
#include <concepts>
class BaseError : public std::exception
{
protected:
    char msg[1024];
public:
    BaseError(char* filename, char* classname, int line, const char* info) noexcept
    {
        strcat(msg, "\nFile name: ");
        strcat(msg, filename);
        strcat(msg, "\nClass: ");
        strcat(msg, classname);
        strcat(msg, "\nLine: ");
        strcat(msg, std::to_string(line).c_str());
        strcat(msg, "Info: ");
        strcat(msg, info);
    }
    ~BaseError() = default;

    virtual const char* what() const noexcept override;
};