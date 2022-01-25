#include "Student.h"
const int MAX_ITEMS = 20000;


class HashTable {
public:
	HashTable();
	int Hash(char* key) const;
	void RetrieveItem(Student& item, bool& found);
	void InsertItem(Student item);
private:
	Student info[MAX_ITEMS];
	Student emptyItem;
	int length;
};
int getIntFromString(char* key) {
	int sum = 0;
	int len = strlen(key);
	if (len % 2 == 1)len++;
	for (int j = 0; j < len; j += 2)sum = (sum + 100 * key[j] + key[j + 1]) % 19937;
	return sum;
}

int HashTable ::Hash(char* key)const {
	return (getIntFromString(key) % MAX_ITEMS);
}


HashTable::HashTable() {
	emptyItem.InitValue(0, (char*)"", 0);
	emptyItem.EmptyKey();
	for (int i = 0; i < MAX_ITEMS; i++)
	{
		info[i] = emptyItem;
	}

};
void HashTable::InsertItem(Student item) {
	int location;
	location = Hash(item.Key());
	while ((info[location] != emptyItem))
		location = (location + 1) % MAX_ITEMS;
	info[location] = item;
	length++;
}

void HashTable::RetrieveItem(Student& item, bool& found) {
	int location;
	int startLoc;
	bool moreToSearch = true;

	startLoc = Hash(item.Key());
	location = startLoc;
	do {
		if (info[location] == item || info[location] == emptyItem)moreToSearch = false;
		else location = (location+1)%MAX_ITEMS;
	} while (moreToSearch&&location!=startLoc);
	found = (info[location] == item);
	if (found)item=info[location];
}