#include <iostream>
#include "StackType.h"
using namespace std;

int main() {
	StackType<int> stack(5);
	stack.Push(1);
	stack.Push(3);
	stack.Push(5);
	stack.Push(2);
	stack.Push(4);

	stack.Print();

	for (int i = 0; i < 5; i++) {
		int item;
		stack.Pop(item);
		cout << item << endl;
	}

	return 0;
}