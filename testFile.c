#include <stdio.h>

void sayHello() {
   // comments are transfered accross
   char name[64] = "";
   char textToPrint[128] = "Hello ";

   gets(name);
   printf("%c %c!", textToPrint, name);
}

int main() {
   // call another function
   sayHello();

   return 0;
}