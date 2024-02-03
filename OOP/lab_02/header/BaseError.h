#ifndef BASE_ERROR_H
#define BASE_ERROR_H

#include <exception>
#include <string>
#include <string.h>

class BaseError : public std::exception
{
protected:
    char msg[1024];
public:
    BaseError(std::string file_name, char *classname, int line, std::string info) noexcept
    {
        strcat(msg, "\nFile name: ");
        strcat(msg, filename);
        strcat(msg, "\nClass: ");
        strcat(msg, classname);
        strcat(msg, "\nLine: ");
        strcat(msg, line);
        strcat(msg, "Info: ");
        strcat(msg, info);
    }
    ~BaseError() = default;

    virtual const char* what() const noexcept override;
};

#endif // BASE_ERROR_H
