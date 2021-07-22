#include <stdio.h>

void printHelloWorld() {
   // comments are transfered accross
   char name[128] = "Hello World!";

   printf(name);
}

int main() {
   // call another function
   printHelloWorld()

   return 0;
}