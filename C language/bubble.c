#include<stdio.h>
int main(){
    int i,j,n,t;
    printf("enter size:\n");
    scanf("%d",&n);
    int a[n];
    printf("enetr %d elements:\n",n);
    for ( i = 0; i <n; i++)
    {
        scanf("%d",&a[i]);
    }
    printf("elements are:");
    for(i=0;i<n;i++)
       printf("%d\t",a[i]);
    for(i=0;i<n-1;i++){
        for(j=0;j<n-i-1;j++){
            if(a[j]>a[j+1]){
                t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
            }
        }
    }   
    printf("after sorting, elements are:\n");
    for(i=0;i<n;i++){
        printf("%d\t",a[i]);
    } 
    return 0;   
}