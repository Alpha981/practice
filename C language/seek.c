#include<stdio.h>
int main(){
    FILE *fp;
    int len;
    fp =fopen("file.txt","w");
    fprintf(fp,"hello");
    fseek(fp,-2,SEEK_SET);
    len=ftell(fp);
    fclose(fp);
    printf("%d",len);
    return(0);
}