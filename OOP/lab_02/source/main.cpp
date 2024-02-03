#include <iostream>
#include <cstdlib>
#include <stdexcept>
#include <exception>

#include "../header/my_errors.h"
#include "../header/Vector.hpp"

int main()
{
    try
    {
        Vector<double> initializing = {5, 2, 15};
        const Vector<int> constVect = {0, 1, 2, 3, 4};
        Vector<float> lenExample(3);
        Vector<double> lenFillExample(3, 6.66, 7.5, 8.6);
        Vector<double> emptyVector(0);

        cout << "---------------Vectors Construction-------------" << endl;
        cout<< "  Vector with initialization: "<< initializing<< endl;
        cout<< "  Vector with a given length "<< lenExample<< endl;
        cout<< "  Vector of a given length with initialization: "<< lenFillExample<< endl;
        cout<< "Empty vector: "<< emptyVector<< endl;

        Vector<double> operVecF = {4, 2, 4};
        Vector<double> operVecS = {3, 1, 5};

        cout << "---------------Vectors checks-------------" << endl;
        cout<< "   Normalization of the vector: "<< operVecS << "=>" << operVecS.get_single_vector() << endl;
        cout<< "   Size vector: " << initializing << " => " << initializing.size()<< endl;
        cout<< "   Vector length: "<< initializing << " => " <<initializing.len()<< endl;
        cout<< "   Is the vector zero: "<< initializing << " => " <<initializing.is_zero()<< endl;
        cout<< "   Is a single vector: "<< initializing << " => " << initializing.is_single()<< endl;
        cout<< "   Angle between vectors: "<< lenFillExample << " and " <<  initializing << " => " <<lenFillExample.angle_between_vectors(initializing)<< endl;

        cout << "---------------Vectors gets and sets-------------" << endl;
        cout<< "   Setting the second element to 10: "<<initializing.set_elem_Vector(1, 10)<< endl;
        cout<< "   The second element of the vector: "<<initializing.get_elem_Vector(1)<< endl;
        cout<< "   The second element of the constant vector: "<< constVect.get_elem_Vector(1)<< endl;

        cout << "---------------Vectors operation-------------" << endl;
        cout << "1. Sum Vectors:" << endl;
        cout << "   Vectors +: "<< operVecF << " + " <<  operVecS << " = " << operVecF + operVecS << endl;
        cout << "   Vectors +: "<< operVecF << ".sum(" <<  operVecS << ") = " << operVecF.sum(operVecS) << endl;
        cout << "   Vectors +=: "<< operVecF << " += " <<  operVecS << " => " << (operVecF += operVecS) << endl;

        operVecF = {4, 2, 4};

        cout << "2. Sub Vectors:" << endl;
        cout << "   Vectors -: "<< operVecF << " - " <<  operVecS << " = " << operVecF - operVecS << endl;
        cout << "   Vectors -: "<< operVecF << ".sub(" <<  operVecS << ") = " << operVecF.sub(operVecS) << endl;
        cout << "   Vectors -=: "<< operVecF << " -= " <<  operVecS << " => " << (operVecF -= operVecS) << endl;

        operVecF = {4, 2, 4};

        cout << "3. Scalar Multy:" << endl;
        cout << "   Vectors * : "<< operVecF << " * " <<  operVecS << " = " << operVecF * operVecS << endl;
        cout << "   Vectors * : "<< operVecF << ".scalarMul(" <<  operVecS << ") = " << operVecF.scalarMul(operVecS) << endl;
//        cout << "   Vectors *=: " << operVecF << " *= " << operVecS  << " => " << (operVecF *= operVecS) << endl;

        operVecF = {4, 2, 4};

        cout << "4. Multy vector and number:" << endl;
        int multyNumber = 2;
        cout << "   Vectors *: "<< operVecF << " * " <<  multyNumber << " = " << operVecF * multyNumber << endl;
        cout << "   Vectors *: "<< operVecF << ".mulNum(" <<  multyNumber << ") = " << operVecF.mulNum(multyNumber) << endl;
        cout << "   Vectors *=: "<< operVecF << " *= " <<  multyNumber << " => " << (operVecF *= multyNumber) << endl;

        operVecF = {4, 2, 4};

        cout << "5. Vector Multy:" << endl;
        cout << "   Vectors &: "<< operVecF << " & " <<  operVecS << " = " << (operVecF & operVecS) << endl;
        cout << "   Vectors &: "<< operVecF << ".vectorMul(" <<  operVecS << ") = " << operVecF.vectorMul(operVecS) << endl;
        cout << "   Vectors &=: "<< operVecF << " &= " <<  operVecS << " => " << (operVecF &= operVecS) << endl;

        operVecF = {4, 2, 4};

        cout << "6. Div vector and number:" << endl;
        int divNum = 2;
        cout << "   Vectors /: "<< operVecF << " / " <<  divNum << " = " << operVecF / divNum << endl;
        cout << "   Vectors /: "<< operVecF << ".divNum(" <<  divNum << ") = " << operVecF.divNum(divNum) << endl;
        cout << "   Vectors /=: "<< operVecF << " /= " <<  divNum << " => " << (operVecF /= divNum) << endl;

        cout << "---------------Vectors checks-------------" << endl;
        Vector<float> orthVecF = {1, 0, 0};
        Vector<float> orthVecS = {0, 1, 0};
        Vector<float> nonOrthVec = {1, 2, 3};

        cout<< "  Orthogonality: "<< orthVecF.is_orthogonality(orthVecS)<< endl;
        cout<< "  Not orthogonality: "<<orthVecF.is_orthogonality(nonOrthVec)<< endl;
        cout<< "  Negative " << nonOrthVec << ": " << -nonOrthVec << endl;
        cout<< "  Negative " << nonOrthVec << " with neg(): " << nonOrthVec.neg() << endl;

        Vector<int> colVecF = {1, 1, 0};
        Vector<int> colVecS = {1, 1, 0};

        cout<< "  Collinearity: "<< colVecF.is_collinearity(colVecS)<< endl;
        colVecF = {5, 2, 0};
        cout<< "  Not collinearity: "<< colVecF.is_collinearity(colVecS)<< endl;

    }
    catch (baseError& err)
    {
        std::cout << err.what() << std::endl;
    }
    return 0;
}
