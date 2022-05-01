#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main(){
    int num,guess,nguesses=1;
    srand(time(NULL));
    num = rand()%100 ;  // number b/w 0 to 100
   // printf("%d\n",num);
    do{
        printf("Guess the number between 0 to 100\n");
        scanf("%d",&guess);
        if(guess>num){
            printf("lower number please\n");
        }
        else if(guess<num){
            printf("higher number please\n");
        }
        else{
            printf("you guessed it in %d attempts\n",nguesses);
        }
        nguesses++;
    }while (guess!=num);
     return 0;
}