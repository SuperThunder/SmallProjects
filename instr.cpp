#include <iostream>
using namespace std;

//Returns len of str from start to NUL
//Max is value you should set for a reasonable upper limit that the str would never be above
int slen(char s[], int max){
	int c = 0; //count

	for(int i = 0; i < max; i++){
		if(s[i] == 0){
			return c;
		}
		else{
			c++;
		}
	}
	
	return -1;
}

//Find the existence of a str inside another str
//Returns number of instances of existence
//Takes NUL terminated sec and full
int instr(char sec[], char full[]){
	int lsec = slen(sec, 255);
	int lfull = slen(full, 20000);
	cout << "Selection length: " << lsec << endl;
	cout << "Full length: " << lfull << endl;
	int end = lfull-lsec;
	int count = 0;
	bool same = false;

	//Only want to iterate as far as there are enough chars in source str
	//That it would be possible for substr to be present
	for(int i = 0; i < end; i++){
		//for each char in substr, check if they match
		for(int k = 0; k < lsec; k++){
			if(sec[k] != full[i+k]){
				same = false;
				break;
			}
			else{
				same = true;
			}
		}
		//if the substr matched to all chars, count it as an instance
		if(same){
			count++;
		}
	}
	
	//should be 0 if no instances
	return count;
}

/* Function seems to work well
int main(){
	char* t = "Or, if the poet everywhere appears and never conceals himself, then again the imitation is dropped, and his poetry becomes simple narration. However, in order that I may make my meaning quite clear, and that you may no more say, I don't understand,' I will show how the change might be effected. If Homer had said, 'The priest came, having his daughter's ransom in his hands, supplicating the Achaeans, and above all the kings;' and then if, instead of speaking in the person of Chryses, he had continued in his own person, the words would have been, not imitation, but simple narration. The passage would have run as follows (I am no poet, and therefore I drop the metre), 'The priest came and prayed the gods on behalf of the Greeks that they might capture Troy and return safely home, but begged that they would give him back his daughter, and take the ransom which he brought, and respect the God. Thus he spoke, and the other Greeks revered the priest and assented. But Agamemnon was wroth, and bade him depart and not come again, lest the staff and chaplets of the God should be of no avail to him --the daughter of Chryses should not be released, he said --she should grow old with him in Argos. And then he told him to go away and not to provoke him, if he intended to get home unscathed. And the old man went away in fear and silence, and, when he had left the camp, he called upon Apollo by his many names, reminding him of everything which he had done pleasing to him, whether in building his temples, or in offering sacrifice, and praying that his good deeds might be returned to him, and that the Achaeans might expiate his tears by the arrows of the god,' --and so on. In this way the whole becomes simple narrative. ";
	cout << instr("and", t);
	
	return 0;
}
*/
