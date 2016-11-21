#include <iostream>
using namespace std;

//Find the existence of a str inside another str
//Returns number of instances of existence
//Takes NUL terminated sec and full
int instr(char sec, char full){
	int lsec = slen(sec);
	int lfull = slen(full);
	int end = slen(full)-slen(sec);

	//Only want to iterate as far as there are enough chars in source str
	//That it would be possible for substr to be present
	for(int i = 0; i < end; i++){
		//for each char in substr, check if they match
		for(int k = 0; k < lsec; k++){
			if(sec[k] != full[i+k]){
				break;
			}
			else{

			}
		}
	}

}

//Returns len of str from start to NUL
//Max is value you should set for a reasonable upper limit that the str would never be above
int slen(char s, int max){
	int c = 0; //count

	for(int i = 0; i < max; i++){
		if(s[i] == 0){
			return c;
		}
		else{
			c++;
		}
	}

}
