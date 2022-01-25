#include "QueType.h"
#include<iostream>

using namespace std;


int main() {
	QueType Que1;


	for (int i = 6; i < 10; i++) {
		Que1.Enqueue(i);
	}
	for (int i = 1; i < 6; i++) {
		Que1.Enqueue(i);
	}
	Que1.Enqueue(6);
	cout<<Que1.MinDequeue();
	cout << endl;
	Que1.Enqueue(6);
	Que1.printQue();
	cout << Que1.MinDequeue();
	cout << Que1.MinDequeue();
	cout << Que1.MinDequeue();
	cout << endl;
}

