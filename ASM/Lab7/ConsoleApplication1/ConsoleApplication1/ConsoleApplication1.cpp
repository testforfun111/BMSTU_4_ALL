#include <iostream>
#include <cstring>

using namespace std;

extern "C"
{
	void my_strcpy(char* dst, const char* src, int len);
}

int my_strlen(const char* str)
{
	int len = 0;
	__asm 
	{
		push ecx;
		push edi;
		mov al, '\0'
		mov ecx, -1;   //установка счетчик
		mov edi, str;  //сравнить es:edi
		repne scasb;   //пока на равно, до первого отличного
		not ecx;
		mov len, ecx;
		pop edi;
		pop ecx;
	}

	return len - 1;
}

int main()
{
	cout << "Test strlen\n";
	char str[100] = "First test";
	cout << "String: " << str << endl;
	int len = my_strlen(str);
	cout << "my_strlen: " << len << endl;
	len = strlen(str);
	cout << "strlen: " << len << endl;

	cout << "Test strcpy\n";
	char src[100] = "Second test";
	char dst[100] = "flkjsdlkfjslkdfj";
	cout << "Source string: " << src << endl;
	len = my_strlen(src);
	my_strcpy(dst, src, len);
	cout << "Copy string from my_strcpy: " << dst << endl;
	memcpy(dst, src, len);
	cout << "Copy string from memcpy: " << dst << endl;
	len = 3;
	cout << "Test overlap\n";
	my_strcpy(src + 2, src, len);
	cout << "Copy string from my_strcpy: " << src << endl;
	char* temp = src + 3;
	my_strcpy(src, temp, len);
	cout << "Copy string from my_strcpy: " << src << endl;
	return 0;
}