#include "StackType.h"
#include <iostream>
using namespace std;



int main() {
	StackType stack;
	stack.Push(8);
	stack.Push(3);
	stack.Push(9);
	stack.Push(8);
	stack.Push(3);
	stack.Push(7);
	stack.Push(5);
	stack.Push(3);

	stack.ReplaceItem( 3, 5);
	
	cout << stack.Top() << endl;
	stack.Pop();
	cout << stack.Top() << endl;
	stack.Pop();
	cout << stack.Top() << endl;
	stack.Pop();
	cout << stack.Top() << endl;
	stack.Pop();
	cout << stack.Top() << endl;
	stack.Pop();
	cout << stack.Top() << endl;
	stack.Pop();
	cout << stack.Top() << endl;
	stack.Pop();
	cout << stack.Top() << endl;
	stack.Pop();
}

