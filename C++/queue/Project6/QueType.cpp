#include "QueType.h"
#include<iostream>

QueType::QueType(int max)
// Parameterized class constructor
// Post: maxQue, front, and rear have been initialized.
//       The array to hold the queue elements has been dynamically
//       allocated.
{
  maxQue = max + 1;
  front = maxQue - 1;
  rear = maxQue - 1;
  items = new ItemType[maxQue];
  minimum_pos = 0;
}
QueType::QueType()          // Default class constructor
// Post: maxQue, front, and rear have been initialized.
//       The array to hold the queue elements has been dynamically
//       allocated.
{
  maxQue = 501;
  front = maxQue - 1;
  rear = maxQue - 1;
  items = new ItemType[maxQue];
}
QueType::~QueType()         // Class destructor
{
  delete [] items;
}

void QueType::MakeEmpty()
// Post: front and rear have been reset to the empty state.
{
  front = maxQue - 1;
  rear = maxQue - 1;
}

bool QueType::IsEmpty() const
// Returns true if the queue is empty; false otherwise.
{
  return (rear == front);
}

bool QueType::IsFull() const
// Returns true if the queue is full; false otherwise.
{
  return ((rear + 1) % maxQue == front);
}

void QueType::Enqueue(ItemType newItem)
// Post: If (queue is not full) newItem is at the rear of the queue;
//       otherwise a FullQueue exception is thrown.  
{

    bool flag = false;
    int index;
    int length = (maxQue - (front - rear)) % maxQue;
    for (int i = length - 1; i > 0; i--) {
        if ((items[i] < items[minimum_pos]) && items[i] != -1)minimum_pos = i;
        if (items[minimum_pos] == -1)minimum_pos++;
    }
  if (IsFull())
    throw FullQueue();
 
  else {
      for (int i = length-1; i >= 0; i--) {
            //큐 내부에 -1이 있으면...
          if (items[i] == -1) {
              flag = true; index = i; break;
          }
      }
      if (flag == true)items[index] = newItem;
      else {
        rear = (rear + 1) % maxQue;
        items[rear] = newItem;
      }
    }
}
  

void QueType::Dequeue(ItemType& item)
// Post: If (queue is not empty) the front of the queue has been 
//       removed and a copy returned in item; 
//       othersiwe a EmptyQueue exception has been thrown.
{
  if (IsEmpty())
    throw EmptyQueue();
  else
  {
    front = (front + 1) % maxQue;
    item = items[front];
  }
}
int QueType::MinDequeue() {
    int length = (maxQue - (front - rear)) % maxQue;
    for (int i = length - 1; i > 0; i--) {
        if ((items[i] < items[minimum_pos]) && items[i] != -1)minimum_pos = i;
        if(items[minimum_pos]==-1)minimum_pos++;
    }
    int elem = items[minimum_pos];
    items[minimum_pos] = -1;
    return elem;
}
