#include <stdio.h> 
  
int main() 
{ 
 
    int Var = 10; 
  

    int *ptr = &Var; 

    printf("Value = %d\n", *ptr); 

    printf("Address  = %p\n", ptr); 
  

    *ptr = 20; 
 
    printf(" *ptr = 20, *ptr is %d\n", *ptr); 
  
    return 0; 
} 