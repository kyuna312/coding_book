#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>             
#include "geometry.h"        
 
 
int main()
{
double displayVolume[2][20] = {};
int choice;
int a, b;
char answer=' ';
char name[30] = " ";
char calcResults[128];
 

printf("Please, enter your first and last names separated by a space: ");
fgets(name, 30, stdin);
strupr(name);
printf("\nHello %s\nWelcome to My Geometric Calculator.\n", name);
 

printf("\nEnter .txt file name to save future calculations: ");
scanf("%123s", calcResults);
strcat(calcResults, ".txt");
FILE *inputf;
inputf = fopen(calcResults, "w");
    if (inputf == NULL)
    {
    printf("Error opening file!\n");
    return 1;
    }
 
do
{
    choice = selectedOption();
 
    switch(choice)
    {
        case 1:
            printf("\nEnter data to calculate area of Parallelogram.");
            printf("\n\nBase: ");
            scanf("%f", &base);
            printf("\nHeight: ");
            scanf("%f", &height);
            printf("\nThe Area of the Parallelogram is %.2f\n", parallelogramArea(base, height));
            fprintf(inputf, "\nThe Area of the Parallelogram is %.2f\n", parallelogramArea(base, height));
        break;
 
        case 2:
            printf("\nEnter data to calculate area of a triangle.");
            printf("\n\nBase: ");
            scanf("%f", &base);
            printf("\nHeight: ");
            scanf("%f", &height);
            printf("\nThe Area of the Triangle is %.2f\n", triangleArea(base, height));
            fprintf(inputf, "\nThe Area of the Triangle is %.2f\n", triangleArea(base, height));
        break;
 
        case 3:
            printf("\nEnter data to calculate area of a trapezoid.");
            printf("\n\nBase: ");
            scanf("%f", &base);
            printf("\nBase Two: ");
            scanf("%f", &baseTwo);
            printf("\nHeight: ");
            scanf("%f", &height);
            printf("\nThe Area of the Trapezoid is %.2f\n", trapezoidArea(base, baseTwo, height));
            fprintf(inputf, "\nThe Area of the Trapezoid is %.2f\n", trapezoidArea(base, baseTwo, height));
        break;
 
        case 4:
            printf("\nEnter data to calculate area of a circle. \n\nRadius: ");
            scanf("%f", &radius);
            printf("\nThe Area of the Circle is %.2f\n", circleArea(radius));
            fprintf(inputf, "\nThe Area of the Circle is %.2f\n", circleArea(radius));
        break;
 
        case 5:
            printf("\nEnter data to calculate area of a regular polygon.");
            printf("\n\nLength: ");
            scanf("%f", &length);
            printf("\nWidth: ");
            scanf("%f", &width);
            printf("\nThe Area of the Regular Polygon is %.2f\n", regPolygonArea(length, width));
            fprintf(inputf, "\nThe Area of the Regular Polygon is %.2f\n", regPolygonArea(length, width));
        break;
 
        case 6:
            printf("\nEnter data to calculate volume of a rectangular prism.");
            printf("\n\nLength: ");
            scanf("%f", &length);
            printf("\nWidth: ");
            scanf("%f", &width);
            printf("\nHeight: ");
            scanf("%f", &height);
            displayVolume[0][1] = length * width;
            displayVolume[1][1] = height;
            printf("\nThe Volume of the Rectangular Prism is %.2f\n", rectPrismVolume(length, width, height));
            fprintf(inputf, "\nThe Volume of the Rectangular Prism is %.2f\n", rectPrismVolume(length, width, height));
        break;
 
        case 7:
            printf("\nEnter data to calculate volume of a right circular cylinder.");
            printf("\n\nRadius: ");
            scanf("%f", &radius);
            printf("\nHeight: ");
            scanf("%f", &height);
            printf("\nThe Volume of the Right Circular Cylinder is %.2f\n", rightCircCylinderVolume(radius, height));
            fprintf(inputf, "\nThe Volume of the Right Circular Cylinder is %.2f\n", rightCircCylinderVolume(radius, height));
        break;
 
        case 8:
            printf("\nEnter data to calculate volume of a right square pyramid.");
            printf("\n\nBase Edge: ");
            scanf("%f", &baseEdge);
            printf("\nHeight: ");
            scanf("%f", &height);
            printf("\nThe Volume of the Right Square Pyramid is %.2f\n", rightSqrPyramidVolume(baseEdge, height));
            fprintf(inputf, "\nThe Volume of the Right Square Pyramid is %.2f\n", rightSqrPyramidVolume(baseEdge, height));
        break;
 
        case 9:
            printf("\nEnter data to calculate volume of a right circular cone.");
            printf("\n\nRadius: ");
            scanf("%f", &radius);
            printf("\nHeight: ");
            scanf("%f", &height);
            printf("\nThe Volume of the Right Circular Cone is %.2f\n", rightCircConeVolume(radius, height));
            fprintf(inputf, "\nThe Volume of the Right Circular Cone is %.2f\n", rightCircConeVolume(radius, height));
        break;
        default: puts("You did not enter a valid number.");
    }

printf("\nTry again?\n");
printf("\nEnter Y or y for yes or any other value to exit:\n");
scanf("%s", &answer);
}while(answer == 'Y' || answer == 'y');
 
    for(a = 0; a <= 1; a++)
    {
        for(b = 0; b <= 19; b++)
        {
    printf("You calculated the volume of  Rectangular Prisms: \n");
    printf("Area of Base: %.2f", a, displayVolume[a][1]);
    printf("\tHeight: %.2f", b, displayVolume[1][b]);
    printf("\tVolume: %.2f\n", rectPrismVolume(length, width, height));
        }
    }
 
fclose(inputf);
return 0;
}
 
int menuArea()
{
    int figure;
    printf("\nSelect figure: \n");
    //Printf with figures for area
    printf("\t1- Parallelogram\n\t2- Triangle\n\t3- Trapezoid\n\t4- Circle\n\t5- Regular Polygon\n");
    printf("\n\nEnter your option: ");
    scanf("%d", &figure);
 
    return figure;
}
 
int menuVolume()
{
    int option;
    printf("\nSelect figure: \n");

    printf("\t1- Rectangular prism\n\t2- Right circular cylinder\n\t3- Right square pyramid\n\t4- Right circular cone\n");
    printf("\n\nEnter your option: ");
    scanf("%d", &option);
 
    return option+5;
}
 
int selectedOption()
{
    int choice;
 
    printf("\nSelect one of the following options: ");
    printf("\n\t1- Calculate area\n\t2- Calculate volume\n");
    printf("\nEnter your option: ");
    scanf("%d", &choice);
    switch(choice)
    {
        case 1: choice = menuArea();
        break;
        case 2: choice = menuVolume();
        break;
    }
    return(choice);
}