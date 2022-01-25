#include <iostream>
#include "Hash.h"
#include "Student.h"
using namespace std;

int main()
{
    Student stu[100];
    stu[0].InitValue(200000000, (char*)"i", 3.0);
    stu[1].InitValue(200000000, (char*)"j", 3.0);
    stu[2].InitValue(200000000, (char*)"b", 3.0);
    stu[3].InitValue(200000000, (char*)"d", 3.0);
    stu[4].InitValue(200000000, (char*)"a", 3.0);
    stu[5].InitValue(200000000, (char*)"e", 3.0);
    stu[6].InitValue(200000000, (char*)"c", 3.0);
    stu[7].InitValue(200000000, (char*)"h", 3.0);
    stu[8].InitValue(200000000, (char*)"f", 3.0);
    stu[9].InitValue(200000000, (char*)"g", 3.0);

    HashTable ht;
    for (int i = 0; i < 10; i++)
        ht.InsertItem(stu[i]);
    

    cout << "Input name" << endl;

    char searchname[30];
    cin >> searchname;

    Student temp;
    temp.InitValue(0, searchname, 0);
    bool found;
    ht.RetrieveItem(temp, found);
    if (found)
        cout << "Found! Name:" << temp.getName() << endl;
}