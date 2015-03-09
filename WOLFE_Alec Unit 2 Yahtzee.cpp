//Roll 5 random 6-sided dice until all 5 equal the same number

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	int Die1, Die2, Die3, Die4, Die5, Rolls, Reroll = 0;
    char Player;
    bool Yahtzee = false;

    srand(time(NULL));
    
    fprintf(stdout, "Would you like to play the game yourself (y) or have the computer play (c)? ");
    fscanf(stdin, "%c", &Player);
    
    if(Player == 'y'){
        //initial roll
            Die5 = rand()%6+1;
            Die4 = rand()%6+1;
            Die3 = rand()%6+1;
            Die2 = rand()%6+1;
            Die1 = rand()%6+1;
            Rolls = 1;
            
        while(Yahtzee == false){
            fprintf(stdout, "Die1: %d Die2: %d Die3: %d Die4: %d Die5: %d\n", Die1, Die2, Die3, Die4, Die5);
            fprintf(stdout, "Which number would you like to reroll for? (Die already having this value will not reroll) ");
            fscanf(stdin, "%d", &Reroll);
            if(Die1 != Reroll){Die1 = rand()%6+1;Rolls += 1;} //Roll dice again and add the roll to the total
            if(Die2 != Reroll){Die2 = rand()%6+1;Rolls += 1;}
            if(Die3 != Reroll){Die3 = rand()%6+1;Rolls += 1;}
            if(Die4 != Reroll){Die4 = rand()%6+1;Rolls += 1;}
            if(Die5 != Reroll){Die5 = rand()%6+1;Rolls += 1;}
            
            if(Die5 == Die4 && Die5 == Die3 && Die5 == Die2 && Die5 == Die1){Yahtzee = true;}
        }
        fprintf(stdout, "Yahtzee at %d rolls with the number %d", Rolls, Die5);
    
    
    }else{
        fprintf(stdout, "Entering computer control mode\n");
        //give int n of the not-array a rand val from 1-6: roll the dice
        Die5 = rand()%6+1;
        Die4 = rand()%6+1;
        Die3 = rand()%6+1;
        Die2 = rand()%6+1;
        Die1 = rand()%6+1;
        Rolls = 1;
        fprintf(stdout, "Die1: %d Die2: %d Die3: %d Die4: %d Die5: %d\n", Die1, Die2, Die3, Die4, Die5);
        int counter = 0, occurance = 0;
        
        int DieArray[4]; DieArray[0] = Die1; DieArray[1] = Die2; DieArray[2] = Die3; DieArray [3] = Die4; DieArray[4] = Die5;
        //Computer autoroll
        while(Die5 != Die4 || Die5 != Die3 || Die5 != Die2 || Die5 != Die1){
            //trying to do this with only variables is a disaster
            //either put in one billion if(){}s or do some only slightly less complicated array stuff
            //need to somehow find the most common value and reroll if the var/arr[n] does not have that value
            for(int i = 1; i >=5; i++){
                for(int j = 1; j >= 5; j++){
                    for(int k = 1; k >= 5; k++){
                        if(DieArray[k] == DieArray[i] && DieArray[k] == DieArray[j]){
                            for(int h = 1; h >= 5; h++){
                                if(DieArray[h] != i){
                                    DieArray[h] = rand()%6+1;
                                }
                            }
                        }
                    }
                }
            }
            
            fprintf(stdout, "Die1: %d Die2: %d Die3: %d Die4: %d Die5: %d\n", Die1, Die2, Die3, Die4, Die5);
            //system("clear"); //looks a little nicer but runs much more slowly
        }
        fprintf(stdout, "\nYahtzee at %d computer rolls with the number %d", Rolls, Die5);
    }
    return 0;
}
