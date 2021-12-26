#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <stdlib.h>

#define SIZE 1024
#define MODE ( S_IRUSR | S_IWUSR | \
               S_IRGRP | S_IROTH)

int main(int argc, char *argv[])
{
    int src, dst;
    int in_count, out_count;
    char buf[SIZE];
    int nread;

    if(argc != 3) {
        fprintf(errno, "Usage: cp f1 f2\n");
        exit(1);
    }

    if((src = open(argv[1], O_RDONLY)) == -1) {
        fprintf(errno, "Cant open %s\n", argv[1]);
        exit(2);
    }

    if((dst = creat(argv[2], MODE)) == -1) {
        fprintf(errno, "cant create %s\n", argv[2]);
        exit(3);
    }

    while((nread =read(src, buf, SIZE)) > 0) 
    {
        if(write(dst, buf, nread) == -1) {
            printf(stderr, "cant write\n");
            exit(4);
        }
    }
    exit(0);
}