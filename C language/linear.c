#include<stdio.h>
int main(){
    int i,j,n,key;
    printf("enter n value");
    scanf("%d",&n);
    int a[n];
    printf("enetr the elements:\n");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    printf("elements are \n");
    for(i=0;i<n;i++)
       printf("%d\t",a[i]);
    printf("\nenetr the key");
    scanf("%d",&key);
    for(i=0;i<n;i++){
        if(a[i]==key){
            printf("\n %d is found at %d",key,i+1);
            break;
        } 
    }
    if(i==n){
        printf(" nummber not found");
    }
    return 0;

}