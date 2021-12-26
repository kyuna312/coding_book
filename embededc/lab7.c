#include <stdio.h>
#include <string.h>

int main(void) {

    char dest[5];
    char src[5]="hello"; 

    dest[sizeof(dest)-1]='\0'; 
    (void) strncpy(dest, src, sizeof(dest));
    if (dest[sizeof(dest)-1]!='\0'); 
    dest[sizeof(dest)-1]='\0'; 

    int required = snprintf(dest, sizeof(dest), "%s", src);
    if (required >= sizeof(dest));
}