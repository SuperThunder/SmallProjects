//String insertion function

//This current implementation will overwrite
//Relies on null terminated string
//Not sure what it returns yet
int strins(char str[], char ins[], int pos){
	int ind;
	for(ind = 0; ins[ind] != 0; ind++){
		str[pos+ind] = ins[ind];
	}
	str[ind] = 0;
		
	return 0;
}

int main(){
	
}
