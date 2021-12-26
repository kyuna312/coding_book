#include <stdio.h>
#include<stdlib.h>
#include<sys/stat.h>
#include<sys/types.h>
#include <unistd.h>

int main ( int argc, char *argv[]){
    printf("1 dir uusgeh \n 2 dir ustgah \n 3 dir holboh\n 4 dir holbolt salgah" );
    int ret, rem;
    char dirname[10000];
    int expression;
    scanf("%d", &expression);
    switch (expression)
    {
    case 1:
        scanf("%s", & dirname);
        ret = mkdir(dirname , S_IRUSR | S_IRGRP | S_IROTH | S_IXUSR | S_IXGRP | S_IXOTH);
        break;
    case 2: 
        scanf("%s", & dirname);
        ret = rmdir(dirname);
        break;
    case 3:
        scanf("%s", & dirname);
        ret = symlink(dirname, "alooga"); 
        break;
    case 4:
        scanf("%s", & dirname);
        ret  = unlink(dirname);
        break;
    default:
        break;
    }
    
    
    return 0;
}