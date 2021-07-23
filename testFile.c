#include <stdio.h>

void sayHello(char name[64], char prefix[16]) {
   // comments are transfered accross
   char textToPrint[128] = "Hello";

   printf("%c %c %c!", textToPrint, prefix, name);
}

int main() {
   char name[64] = "";

   printf("What's your name?");
   gets(name);

   // call another function
   sayHello(name, "Mx");

   return 0;
}