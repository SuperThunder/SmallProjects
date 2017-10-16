using namespace std;
#include <iostream>
#include <fstream>
struct infile{
	char filename[255];
	char* line[]; //pointer to memory that will be allocated for file lines
	int lc; //line count	
};

//returns a status code, infile filled by reference
int fillFile(char filename[], infile dest){
	ifstream fin;
	const int STRLEN = 255;
	int line = 0;
	fin.open(filename);
	
	if(fin.fail()){
		cerr << "Error: Invalid filename" << endl;
		return -1;
	}
	
	while(!fin.eof()){	
		fin.getline(dest.line[line], STRLEN-2, '\n');
		line++;
	}
	
}
