#include <stdio.h>

void sayHello(char name[64]) {
   // comments are transfered accross
   char textToPrint[128] = "Hello ";

   printf("%c %c!", textToPrint, name);
}

int main() {
   char name[64] = "";
   gets(name);

   // call another function
   sayHello(name);

   return 0;
}