#pragma once
#include "stddef.h"
#include<string>
struct LineType {
	char info[80];
	LineType* back;
	LineType* next;
};

class TextEditor {
public:
	TextEditor() ;
	void GoToTop();
	void GoToBottom();
	void InsertLine(char newline[]);
private:
	int length;
	LineType* currentLine;
	LineType* listData;
};
TextEditor::TextEditor() {
	LineType* Header=new LineType;
	strcpy_s(Header->info,"Top of File");
	LineType* Trailer=new LineType;
	strcpy_s(Trailer->info, "Bottom of File");
	Header->back = NULL;
	Header->next = Trailer;
	Trailer->next = NULL;
	currentLine = Header;
	listData = Header;
}
void TextEditor::GoToTop() {
	while (currentLine->back != NULL) {
		currentLine = currentLine->back;
	}
	currentLine = currentLine->next;
}
void TextEditor::GoToBottom() {
	while (currentLine->next != NULL) {
		currentLine = currentLine->next;
	}
	currentLine = currentLine->back;
}

void TextEditor::InsertLine(char newline[]) {
	LineType* line = new LineType;
	strcpy_s(line->info, newline);
	line->back = currentLine;
	line->next = currentLine->next;
	currentLine->next=line;
	currentLine->next->back = line;
	length++;
}