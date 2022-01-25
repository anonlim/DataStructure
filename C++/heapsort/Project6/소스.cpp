#include <iostream>
#include "HeapSort.h"
using namespace std;

int main()
{
	Student stu[100];
	stu[0].InitValue(2003200111, (char*)"25", 3.0);
	stu[1].InitValue(2004200121, (char*)"17", 3.2);
	stu[2].InitValue(2005200131, (char*)"36", 2.7);
	stu[3].InitValue(2005200131, (char*)"2", 2.7);
	stu[4].InitValue(2005200131, (char*)"3", 2.7);
	stu[5].InitValue(2005200131, (char*)"100", 2.7);
	stu[6].InitValue(2005200131, (char*)"1", 2.7);
	stu[7].InitValue(2005200131, (char*)"19", 2.7);
	stu[8].InitValue(2005200131, (char*)"7", 2.7);
	stu[9].InitValue(2005200131, (char*)"12", 2.7);
	stu[10].InitValue(2005200131, (char*)"13", 2.7);
	//HeapSort(stu, 9);
	//Print(cout, stu, 9);


	GetHeightSum(stu, 11);

	
	return 0;

}