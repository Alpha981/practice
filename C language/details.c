#include<stdio.h>
#include<string.h>
struct student
{ char name[15];
  int age;
  float marks[6];  
};
int main(){
    int i,n,j;
    printf("enetr number of students");
    scanf("%d",&n);
    getchar();
    struct student s[n];
    for(i=0;i<n;i++){
        printf("\nReading details of students %d\n",i+1);
        printf("enter name:");
        gets(s[i].name);
    
        printf("enter age\n");
        scanf("%d",&s[i].age);
        printf("enter marks of 6 subjects:");
        for(j=0;j<6;j++)
        scanf("%f",&s[i].marks[j]);
        getchar();
    }
    for(i=0;i<n;i++){
        printf("details of students::%d\n",i+1);
        printf("%s %d",s[i].name,s[i].age);
        for(j=0;j<6;j++)
        printf("%.2f\n",s[i].marks[j]);
        printf("\n");
    }
    return 0;
}