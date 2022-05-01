#include<stdio.h>
int main(){
    int i,j,n,t,pos;
    printf("enter size");
    scanf("%d",&n);
    int a[n];
    printf("enter elements are:\n");
    for(i=0;i<n;i++)
       scanf("%d",&a[i]);
    printf("elements are:\n");
    for(i=0;i<n-1;i++){
        printf("%d\t",a[i]);
    for(i=0;i<n;i++){
        pos=i;
        for(j=i+1;j<n;j++){
            if (a[pos]>a[j])
                 pos=j;
            }
            if(pos!=i){
                t=a[j];
                a[j]=a[pos];
                a[pos]=t;
            }
        }
    printf("after sorting, elements are:");
    for(i=0;i<n;i++)
       printf("%d\t",a[i]);
       return 0;

}