#include<stdio.h>
struct topper 
{   char name[20];
    int score;
};
int main(){
    struct topper t[20],temp;
    int i,j,n;
    printf("enetr number of students::");
    scanf("%d",&n);
    printf("enter name and score::");
    for(i=0;i<n;i++){
        scanf("%s ",t[i].name);
        scanf("%d",&t[i].score);
    }
    for(i=0;i<n;i++){
       for(j=i+1;j<n;j++){
           if(t[i].score<t[j].score){
               temp=t[i];
               t[i]=t[j];
               t[j]=temp;
           }
       }
    }
    for(i=0;i<n;i++){
        printf("%s \t%d\n",t[i].name,t[i].score);
    }
    return 0;
}
