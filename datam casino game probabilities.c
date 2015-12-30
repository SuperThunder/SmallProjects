#include <stdio.h>
#include <stdlib.h>
int fact(int number); //factorial function
int combin(int num, int sel); //nCk function
int playerprob(int numplaying);
int addvalcsv(float val);

/*
What we need is the the total probabilities for
    2 to 8 cards drawn for player, 4 to 8 for dealer
        number of cards * expected points

And then the probabilities when there is more than one player
*/
FILE *csv;
float eppc = 1.384615385; //expected points per card
int main(){

    csv = fopen("probabilities.csv", "w");//make and open a .csv file to store the data in
    fprintf(csv, "Alec Wolfe/Lucas Stack Data Management Summative Probabilities");
    fprintf(csv, ",Generated using a C program");

	int i, k, j;
	float dealertotalp = 0, playertotalp = 0;
	int dealertotalwins = 0, totalgames = 0, tiecount = 0;

	//set up column headers
	fprintf(csv, "\n\nDealer Cards, Player Cards,Dealer Expected Points, Player Expected Points, Dealer Won");

	for(i = 5; i <= 8; i++){
		for(k = 3; k <= 8; k++){
			fprintf(csv, "\n%d,%d,%f,%f", i, k, i*eppc, k*eppc);
			if(i*eppc>k*eppc){ //dealer points > player points (dealer won)
				fprintf(csv, ",Yes");
				dealertotalwins += 1;
			}else if(i*eppc==k*eppc){
				fprintf(csv, ",Tie");
				tiecount += 1;
			}else{
                fprintf(csv, ",No");
			}
			dealertotalp += i*eppc;
			playertotalp += k*eppc;
			totalgames += 1;
		}
	}
	fprintf(csv, "\n,,%f (total),%f (total),%d (total) of %d with %d ties", dealertotalp, playertotalp, dealertotalwins, totalgames, tiecount);
	printf("Done!");

	return 0;
}

int fact(int number) {
    int result = 1, i;
    for(i = 1; i <= number; i++){
        result = result * i;
    }

    return result;
}

int combin(int num, int sel){
	int result;
	result = fact(num) / (fact(num-sel)*fact(sel));
	return result;
}

//non-functional recursive code
/*
int playerprob(int numplaying){
    int i, k;
    float numb;

    fprintf(csv, "\n");
    for(k = 0; k < numplaying; k++){
        for(i = 3; i <= 8; i++){ //player's possible numbers of cards
            //ftoa(i*eppc, numb, 10);
            numb = i*eppc;
            addvalcsv(numb);
        }
    }
}

int addvalcsv(float val){
    fprintf(csv, ",%f", val);
}
*/
