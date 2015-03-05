//Roll 5 random 6-sided dice until all 6 equal the same number

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	int DieArray[5], Rolls = 0;
	DieArray[5] = 0;

    srand(time(NULL));
    //loop while the dice are not all equal: hacky but it works and i'm tired
    while(DieArray[5] != DieArray[4] || DieArray[5] != DieArray[3] || DieArray[5] != DieArray[2] || DieArray[5] != DieArray[1] || DieArray[5] != DieArray[0]){
        for(int j = 0; j < 1; j++){
			Rolls += 1;
            //give int n of the array a rand val from 1-6...roll the dice
            for(unsigned int i = 0; i < 6; i++){
                DieArray[i] = rand()%6+1;
                //fprintf(stdout, "die %d rolled %d\n", i, DieArray[i]);    
            }
        }
		fprintf(stdout, "Die1: %d Die2: %d Die3: %d Die4: %d Die5: %d Die6: %d\n", DieArray[0], DieArray[1], DieArray[2], DieArray[3], DieArray[4], DieArray[5]);
        //system("clear"); //looks a little nicer but runs much more slowly
    }
    fprintf(stdout, "Yahtzee at %d rolls with the number %d", Rolls, DieArray[5]);
    return 0;
}
