#include <iostream>
using namespace std;

bool signchar(char in){
	const int SIGN_CHAR_NUM = 2;
	const char validchars[SIGN_CHAR_NUM] = {'+', '-'};
	
	for(int i = 0; i < SIGN_CHAR_NUM; i++){
		if(in == validchars[i]){
			return true;
		}
	}
	
	return false;
}

bool whitechar(char in){
	const int WHITE_CHAR_NUM = 3;
	const char validchars[WHITE_CHAR_NUM] = {' ', '\t', '\n'};
	
	for(int i = 0; i < WHITE_CHAR_NUM; i++){
		if(in == validchars[i]){
			return true;
		}
	}
	//WILL default to false
	//cerr << "Non whitespace character" << endl;
	return false;
}

bool numchar(char in){
	const int NUM_CHAR_NUM = 10;
	const char validchars[NUM_CHAR_NUM] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
	//bool valid = false;
	
	for(int i = 0; i < NUM_CHAR_NUM; i++){
		if(in == validchars[i]){
			return true;
		}
	}
	//If not a numeric character WILL return false
	//cerr << "Non numeric character" << endl;
	return false;
}

// Check that number chars aren't too big for int
// Returns true for good size, false for too big
bool intsize(char number[]){
	int i = 0;
	const int numlen = 10;
	int posadj = 0; //use this if sign char makes number 1 longer
	char maxint[10] = {'2', '1', '4', '7', '4', '8', '3', '6', '4', '7'};
	bool bigger = true;
	
	// Adjust size of number str depending on if signchar is present
	if(signchar(number[0])){	posadj=1;	}

	for(i=0; i < numlen; i++){
		if(number[i+posadj] > maxint[i]){
			bigger = true;
		}else if(number[i+posadj] == maxint[i]){
			continue;
		}else{
			//if any one of the chars starting from left is less then we're fine
			return true;
		}
	}
	if(bigger){
		return false;
	}
}

//Returns status code
//Error: negative index of error
//Converted int is set by reference
int arrtoint(char* src, int* dest){
	char number[12]; //possible sign, 10 digits in 2^32 int, null terminator
	char curchar;
	int srcind = 0, destind = 0;
	
	//for every char in the passed char number
	while(src[srcind] != '\0'){
		curchar = src[srcind];
		// For any char, check for period since it needs special error
		if(curchar == '.'){
			cerr << "Error: Invalid input. Not an integer." << endl;
			return -srcind;
		}
		// Check if number input is too long for int
		// Different lengths if sign char is there or not
		if(destind == 11 && signchar(number[0]) && !intsize(number)){
			cerr << "Error: Input number too long for int." << endl;
			return -srcind;
		//no sign char therefore can only be 10 digits long
		}
		else if(destind == 10 && !signchar(number[0]) && !intsize(number)){
			cerr << "Error: Input number too long for int." << endl;
			return -srcind;
		}
		else if(destind > 11){
			cerr << "Error: Input number too long for int." << endl;
			return -srcind;
		}
		
		// Special checks for just the first character of number
		if(srcind == 0){
			// Check for a sign char
			if(signchar(curchar)){
				number[destind] = curchar;
				destind++;
				srcind++;
			// Check for a whitespace char, only incr. ind skips wpspace
			}
			else if(whitechar(curchar)){
				srcind++;
			//Check for a digit char
			}
			else if(numchar(curchar)){
				number[destind] = curchar;
				destind++;
				srcind++;
			}
			else{
				cerr << "Error: Invalid input. Not a number." << endl;
				return -srcind;
			}
		}else{
			if(numchar(curchar)){
				number[destind] = curchar;
				destind++;
				srcind++;
			}else{
				cerr << "Error: Invalid input. Not a number." << endl;
				return -srcind;
			}
		}
	}
	//Since the while loop terminates on '\0' of input, 
	//it means we have all the number chars for that num
	number[destind] = '\0'; //terminate the number word
	if(destind > 10 || !intsize(number)){
		cerr << "Error: Invalid int size: " << number << endl;
		return -srcind;
	}
		
	return 0;
}
