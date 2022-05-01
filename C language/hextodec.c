#include<stdio.h>
#include<math.h>
#include<string.h>
int main() {
    char hex[10];
    int len,i=0,dec=0;
    printf("enetr the hexadecimal number");
    scanf("%s",hex);
    len=strlen(hex);
    len--;
    for(i=0;hex[i]!='0';i++,len--){
        if(hex[i]>='0' && hex[i]<='9') {
            dec = dec + (hex[i]-48)*pow(16,len);
        }
        else if(hex[i]>='A' && hex[i]<='F') {
            dec = dec + (hex[i]-55)*pow(16,len);
        }
        else if(hex[i]>='a' && hex[i]<='f') {
            dec = dec + (hex[i]-87)*pow(16,len);
         
        }
    }
    printf("decimal number is %d",dec);
    return 0;
}