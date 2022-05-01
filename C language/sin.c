#include<stdio.h>
#include<math.h>
float sine(float, int);
int fact(int);
int main(){
    int n;
    float x,val;
    printf("enter value of x in degrees:");
    scanf("%f",&x);
    printf("enter the value of n:");
    scanf("%d",&n);
    val=x*3.14/180;
    printf("sin value of %f is %f",x,sine(val,n));
    return 0;
}
float sine(float rad,int n){
    float i,t,sum=rad;
    for(i=1;i<=n;i++){
        t= (pow(-1,i)*pow(rad,2*i+1))/fact(2*i+1);
        sum+= t;
    }
    return sum;
}
int fact(int n){
    int i,f=1;
    for(i=1;i<=n;i++){
        f*=i;
    }
    return f;
}
