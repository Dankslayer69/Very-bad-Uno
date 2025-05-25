#include <iostream>
#include <string>
#include <time.h>
#include <random>
#define NUMPLAYERS 4
#define DECKSIZE 40
using namespace std;

//comment to see if git works

struct card{
    int num;
    string color;
};

int rollnumber(){
    return (rand() % 9) + 1 ;
}

string rollcolor(){
    int i = rand() % 4;

    switch(i){
        case 0:
            return "blue";
            break;
        case 1:
            return "red";
            break;
        case 2:
            return "yellow";
            break;
        case 3:
            return "green";
            break;
    };
}


class player{
public:
    string name;
    int numplayer;



};


int main(void){
    srand(time(NULL));

bool gamerunning = true;

card deck[40];


for(int i = 0;i < DECKSIZE; i++){
    deck[i].num = rollnumber();
    deck[i].color = rollcolor();
}

for(int i = 0;i < DECKSIZE; i++){
    cout << deck[i].num << deck[i].color << endl;
}



    
    return 0;
}
