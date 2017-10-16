//String insertion function

//This current implementation will overwrite
//Relies on null terminated string
//Not sure what it returns yet
int strins(char str[], char ins[], int pos){
	int ind;
	for(ind = 0; ins[ind] != 0; ind++){
		str[pos+ind] = ins[ind];
	}
	str[pos+ind] = 0;
		
	return 0;
}

/*
#include <iostream>
using namespace std;
int main(){
	char t[] = "A string that is going to be inserted into";
	cout << t << endl;
	strins(t, ".txt", 42);
	cout << t;
}
*/
