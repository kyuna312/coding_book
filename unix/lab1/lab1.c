#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <stdio.h>

int main(){
    int fd;
    fd = open("khatnaa", O_WRONLY | O_CREAT ,0644);
    write(fd, "Unix programchlal", 27);
    close(fd);
}