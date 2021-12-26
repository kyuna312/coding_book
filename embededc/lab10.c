#include <stdio.h>
#include <stdlib.h>

int main() {
    char sentence[1000];
    FILE *fptr;
    fptr = fopen("program.txt", "w");

    if (fptr == NULL) {
        printf("Error!");
        exit(1);
    }
    printf("oguulberee oruulana uu:\n");
    fgets(sentence, sizeof(sentence), stdin);
    fprintf(fptr, "%s", sentence);
    fclose(fptr);
    return 0;
}