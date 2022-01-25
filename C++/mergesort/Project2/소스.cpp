#include <iostream>
#include "MergeSort.h"
#include "Student.h"
using namespace std;

int main()
{
    Student stud[100];
    stud[0].InitValue(2001000003, (char*)"이용재", 3.0);
    stud[1].InitValue(2001000007, (char*)"권오준", 3.2);
    stud[2].InitValue(2001000008, (char*)"김진일", 2.7);

    MergeSort(stud, 0, 2);

    
    Print(cout, stud, 3);
}