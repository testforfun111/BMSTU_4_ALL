# include <iostream>

using namespace std;

int main()
{
	int i = 0;
	int&& rv1 = i + 0;
	int&& rv2 = move(i);
	int&& rv3 = (int)i;

	++i;

	int&& rv4 = 5;
	++rv4;

	cout << "rv1 = " << rv1 << "; rv2 = " << rv2 << "; rv3 = " << rv3 << endl;
	cout << "rv4 = " << rv4 << endl;
    ++rv2;

    cout << "rv2 = " <<  rv2 <<endl;
    cout << "i = " << i << endl;
}
