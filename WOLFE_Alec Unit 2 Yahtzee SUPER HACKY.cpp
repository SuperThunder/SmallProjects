//Roll 5 random 6-sided dice until all 5 equal the same number

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	int Die1, Die2, Die3, Die4, Die5, Rolls = 0;
    char player;

    srand(time(NULL));
    
    fprintf(stdout, "Would you like to play the game yourself (y) or have the computer play (c)");
    fscanf(stdin, "%c", player);
    
        //Computer autoroll
        while(Die5 != Die4 || Die5 != Die2 || Die5 != Die2 || Die5 != Die1){
            Rolls += 1;
            //give int n of the array a rand val from 1-6: roll the dice
            Die5 = rand()%6+1;
            Die4 = rand()%6+1;
            Die3 = rand()%6+1;
            Die2 = rand()%6+1;
            Die1 = rand()%6+1;
            
            fprintf(stdout, "Die1: %d Die2: %d Die3: %d Die4: %d Die5: %d\n", Die1, Die2, Die3, Die4, Die5);
            //system("clear"); //looks a little nicer but runs much more slowly
        }
        fprintf(stdout, "Yahtzee at %d rolls with the number %d", Rolls, Die5);


    return 0;
}
