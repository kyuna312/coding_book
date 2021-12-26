#include<stdio.h>
#include<conio.h>

int main()
{
    int a[20],n,i,max=0; 
    clrscr();

    printf("\n array: ");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        printf("\n Enter element [%d] : ",i+1);
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        if(max<a[i])
            max=a[i];
    }

    printf(" %d",max);

    getch();

    return 0;
}