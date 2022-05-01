#include<stdio.h>
#include<stdlib.h>
#include<time.h>
// return 0 for draw,1 for win, -1 for lose
int snake(char u,char c){
    if(u==c){
        return 0;
    }
    if((u=='s' && c=='g') || (u=='w' && c=='s') || (u=='g' && c=='w')){ 
        return -1;
    }
    else if((u=='g' && c=='s') || (u=='s' && c=='g') || (u=='w' && c=='g')){ 
        return 1;
    }
}
 
int main(){
    char u,c;
    srand(time(NULL));
    int number =rand()%100 +1;

    if(number<33){
        c='s';
    }
    else if(number>33 && number<66){
        c='w';
    }
    else{
        c='g';
    }

    printf("enter 's' for snake, 'w' for water, 'g' for gun\n");
    scanf("%c",&u);
    int result=snake(u,c);
     if(result==0){
        printf("match draw\n");
    }
    else if(result== 1){
        printf("match win\n");
   }
    else if(result== -1){
        printf("match lose\n");
    }
    printf("you choose %c and computer choose %c",u,c);
    return 0;
}