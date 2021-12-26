#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/mman.h>
void write_mmap_sample_data();

int main() {
   struct stat mmapstat;
   char *data;
   int minbyteindex , maxbyteindex , offset , fd , unmapstatus;

   write_mmap_sample_data();

   if (stat("MMAP_DATA.txt", &mmapstat) == -1) {
      perror("stat aldaa");
      return 1;
   }
   
   if ((fd = open("MMAP_DATA.txt", O_RDONLY)) == -1) {
      perror("open aldaa");
      return 1;
   }
   data = mmap((caddr_t)0, mmapstat.st_size, PROT_READ, MAP_SHARED, fd, 0);
   
   if (data == (caddr_t)(-1)) {
      perror("mmap aldaa");
      return 1;
   }

   minbyteindex = 0;
   maxbyteindex = mmapstat.st_size - 1;
   
   do {
      printf("-1 deer darj garah");
      printf("endees  %d ene hurtleh toog oruulan uu %d: ", minbyteindex, maxbyteindex);
      scanf("%d",&offset);
      if ( (offset >= 0) && (offset <= maxbyteindex) )
      printf("hURJ IRSEN  %d utga %c\n", offset, data[offset]);
      else if (offset != -1)
      printf("tohirohgui utgaa damjuulagdsan bn %d\n", offset);
   } while (offset != -1);
   unmapstatus = munmap(data, mmapstat.st_size);
   
   if (unmapstatus == -1) {
      perror("munmap aldaa");
      return 1;
   }
   close(fd);
   system("rm -f MMAP_DATA.txt");
   return 0;
}

void write_mmap_sample_data() {
   int fd;
   char ch;
   struct stat textfilestat;
   fd = open("MMAP_DATA.txt", O_CREAT|O_TRUNC|O_WRONLY, 0666);
   if (fd == -1) {
      perror("File open aldaa ");
      return;
   }
   // Write A to Z
   ch = 'A';
   
   while (ch <= 'Z') {
      write(fd, &ch, sizeof(ch));
      ch++;
   }
   // Write 0 to 9
   ch = '0';
   
   while (ch <= '9') {
      write(fd, &ch, sizeof(ch));
      ch++;
   }
   // Write a to z
   ch = 'a';
   
   while (ch <= 'z') {
      write(fd, &ch, sizeof(ch));
      ch++;
   }
   close(fd);
   return;
}