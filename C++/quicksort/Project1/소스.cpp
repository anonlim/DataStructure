#include <iostream>
#include "QuickSort.h"
#include "Student.h"
using namespace std;

int main()
{
    Student stud[100];
    stud[0].InitValue(2001000003, (char*)"�̿���", 3.0);
    stud[1].InitValue(2001000007, (char*)"�ǿ���", 3.2);
    stud[2].InitValue(2001000008, (char*)"������", 2.7);

    QuickSort(stud, 0, 2);

    
    Print(cout, stud, 3);
}