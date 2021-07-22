#include <stdio.h>

void printHelloWorld() {
   // comments are transfered accross
   char textToPrint[128] = "Hello World!";

   printf(textToPrint);
}

int main() {
   // call another function
   printHelloWorld()

   return 0;
}