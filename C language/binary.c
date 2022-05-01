#include <stdio.h>
int main(){
    int i, j, n, key;
    printf("enter the n size");
    scanf("%d", &n);
    int a[n], first = 0, last = n - 1, mid;
    printf("enetr the numbers");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    printf("elements are:");
    for (i = 0; i < n; i++)\
     printf("%d\t", a[i]);
    printf("enetr key");
    scanf("%d", &key);
    while (first <= last)
    {
        mid = (first = last) / 2;
        if (key > a[mid])
         first = mid + 1;
        else if (key < a[mid])
            last = mid - 1;
        else
           { printf("%d is found at %d\n", key, mid + 1);
        break;  }
    }
    if (first > last)
        printf("elment not found");
    return 0;
         }