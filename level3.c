#define STDIN_FILENO 1
#define STDOUT_FILENO 1
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


void vulnerable_function(){
     char buf[128];
     read(STDIN_FILENO,buf,256);
}
 
int main(int argc,char** argv){
      vulnerable_function();
      write(STDOUT_FILENO,"HELLO,WORLD\n",13);
      
}
      

