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
        //still dealing with non-array ints here, we convert soon but do initial roll before
        Die5 = rand()%6+1;
        Die4 = rand()%6+1;
        Die3 = rand()%6+1;
        Die2 = rand()%6+1;
        Die1 = rand()%6+1;
        Rolls = 1;
        fprintf(stdout, "Die1: %d Die2: %d Die3: %d Die4: %d Die5: %d\n", Die1, Die2, Die3, Die4, Die5);
        int innercounter = 0, outercounter = 0, mostcommon;
        
        int DieArray[4]; DieArray[0] = Die1; DieArray[1] = Die2; DieArray[2] = Die3; DieArray [3] = Die4; DieArray[4] = Die5;
        //Computer autoroll

        while(DieArray[4] != DieArray[3] || DieArray[4] != DieArray[2] || DieArray[4] != DieArray[1] || DieArray[4] != DieArray[0]){
            for(int j = 1; j <=6; j++){ //iterate through face values
                innercounter = 0; //reset the counter
                for(int k = 0; k <=4; k++){ //iterate die
                    if(DieArray[k] == j){innercounter++;}
                }
            
            if(innercounter > outercounter){outercounter = innercounter; mostcommon = j;} //if a more common value has been found assign that value
            }
            
            fprintf(stdout, "mostcommon # = %d\n", mostcommon);
            for(int i = 0; i <= 4; i++){ //Reroll die that do not have the common value
                if(DieArray[i] != mostcommon){DieArray[i] = rand()%6+1;}
            }
            Rolls += 1;
            
            fprintf(stdout, "Die1: %d Die2: %d Die3: %d Die4: %d Die5: %d\n", 
            DieArray[0], DieArray[1], DieArray[2], DieArray[3], DieArray[4]);
            //system("clear"); //looks a little nicer but with smart rolling finishes too quicklyh
        }
        fprintf(stdout, "\nYahtzee at %d computer rolls with the number %d", Rolls, DieArray[4]);
    }
    return 0;
}
