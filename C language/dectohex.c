#include<stdio.h>
int main()
{
    int n,i,rem;
    char hex[10];
    printf("enter the decimal number:");
    scanf("%d",&n);
    for(i=0;i<n,n>0;i++){
        rem=n%16;
        switch(rem)  {
            case 10:
              hex[i]='A';
              break;
            case 11:
              hex[i]='B';
              break;
            case 12:
              hex[i]='C';
              break;
            case 13:
              hex[i]='D';
              break;
            case 14:
              hex[i]='E';
              break;
            case 15:
              hex[i]='F';
              break;
            default:
              hex[i]=rem+'0';
              break;
        }
       n=n/16;
    }
    hex[i]='\0';
    printf("hexa decimal number:");
    for(i=i-1;i>=0;i--)
    putchar(hex[i]);
}