#include <stdio.h>

void sayHello(char name[64], int lineage) {
   // comments are transfered accross
   char textToPrint[128] = "Hello";

   for (int i = 0; i < lineage; i = i + 1) {
      /* say hello to all the lineage of people */
      printf("%c %c the %cth!", textToPrint, name, i);
   }
}

int main() {
   // while loop demo
   int i = 0;

   while i < 5 {
      printf("C2Rust Converter Demo!");
      i = i + 1;
   }

   // get user input from the command line
   char name[64] = "";

   printf("What's your name?");
   gets(name);

   // call another function
   sayHello(name, 4);

   return 0;
}
