
//Finds the instances of any string in another as delineated by multiple tokens
//Returns number of instances found
//Set by reference is those indexes, in an int array
int tokfind(char src[], char tok, int inds[]){
	return 0;
}

using namespace std;
#include <iostream> //for use of copy(): remove when native function made

//Similar behaviour to tokfind, but takes a left bound token and right bound token
//Fills by reference a str of the token
//Returns the immediate post index of the token found
//Returns -1 on no token found
//-2 on invalid tokenizing (ex: left token, and then left token again)
//This version relies on NUL as EOS
int tokfind(char src[], const char ltok, const char rtok, char token[], int ind){
	int indl, indr; //left and right index
	enum states{NOTOK, LTOK, RTOK};
	states s = NOTOK;
	
	cout << "Called with: " << src << " " << ltok << rtok << " " << ind << endl;
	
	for(int i = 0; src[i] != 0; i++){
		cout << src[i] << " i: " << i << endl;
		//possibly reimplementation: set ltok/rtok to const char and use switch
		if(src[i] == ltok){
				cout << "Found ltok" << endl;
				//Found left token again: string is improperly tokenized
				//Trying to validly handle this would be arbitrary and bug prone
				if(s==LTOK){
					return -2;
				}
				else{
					s = LTOK;
					indl = i;
				}
		}
		else if(src[i] == rtok){
				cout << "Found rtok" << endl;
				//Found right token without left token
				if(s==NOTOK){
					return -2;
				}
				else{
					s = RTOK;
					indr = i;
					/*BEGIN NON NATIVE*/
					//To implement: own strcpy function
					using namespace std;
					copy(src+indl+1, src+indr, token);
					token[indr+1] = '\0';
					return indr;
					/*END NON NATIVE*/
				}
		}
		else if(src[i] == 0){
			//Not sure if this can ever be reached: to test
		}
	}
	
	//Should occur on no token found
	return -1;
}

//returns right index when done
int toksfind(char src[], char toks, int numtoks, char word[], int ind){
	int indl, indr; //left and right index
	enum states{NOTOK, LTOK, RTOK};
	states s = NOTOK;
	
	//starting from an index, go until non token is found
	//once non token is found, record word chars into word
	//once token char is then found, return the index
	for(int i = ind; src[i] != 0; i++){
		
	}
	
	//Should occur on no token found
	return -1;
}

int main(){
	char token[255];
	char ex[] = "A string [about] tokens as a [token] test to test a token finder";
	int tokind;
	
	//Run tokfind on ex with [] tokens to fill token starting at ind 0
	tokind = tokfind(ex, '[', ']', token, 0);
	if(tokind < 0){
		//error occured
	}
	else{
		cout << token << endl;
	}
	
	
}
