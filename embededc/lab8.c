  
#include<stdio.h>
int main(){

	FILE* input = fopen("input.txt", "r");
	int a;

	fscanf(input, "%d", &a);

	fclose(input);
	printf("%d", a);
	FILE* output = fopen("output.txt", "w");

	fprintf(output, "%d", a);
	fclose(output);
	return 0;
}