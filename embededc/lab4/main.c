#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long converterD2B(int n);
int converterB2D(long n);
int decimalToBinery();
int bineryToDecimal();

int main()
{
    int option, k = 1;

    while (k > 0)
    {
        rintf("\n*********Menu*********\n\n(1)Decimal into Binary\n(2)Binary into Decimal\n\n - Enter 0 to exit -");
        printf("\n\nEnter your Option: ");
        scanf("%d", &option);

        //when option = 0. Program will terminate
        if(option == 0)
        {
            exit(0);
            break;
        }
        if (option == 1)
        {
            decimalToBinery();
        }
        if (option == 2)
        {
            bineryToDecimal();
        }
        if (option<1 || option >2)
        {
            printf("\nooops! aldaa.\n");
        }

        k++;
    }

}

int decimalToBinery()
{
    long x;

    printf("\n\ntoogoo oruulana uu: ");
    scanf("%d", &x);

    printf("\n\n%d  >>>>  %ld \n\n", x, converterD2B(x));

    return 0;
}

int bineryToDecimal()
{
    long y;
    printf("\nbinary gaa oruulana uu: ");
    scanf("%lld", &y);
    printf("\n\n%d  >>>>  %ld \n\n", y, converterB2D(y));
    return 0;
}

long converterD2B(int n)
{
    long binery = 0;
    int y, i = 1;

    while (n != 0)
    {
        y = n%2;
        n /= 2;

        binery += y*i;
        i *= 10;

    }
    return binery;
}

int converterB2D(long n)
{
    int decimalNumber = 0, i = 0, remainder;
    while (n!=0)
    {
        remainder = n%10;
        n /= 10;
        decimalNumber += remainder*pow(2,i);
        ++i;
    }
    return decimalNumber;
}
