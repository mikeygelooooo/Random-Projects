#include <stdio.h>
#include <stdlib.h>

// Main Function
int main(){
// Variables
   int choice;
   int amountItem;
   float price;
   float orderAmount;
   float itemCharge;
   float totalCharge;
   float payment;
   float change;
// Title & Intro
   printf("-----------------------\n\n");
   printf("\tMALL MALL\n\n");
   printf("-----------------------\n\n");
   printf("Available items in store:\n");
   printf("1. Food - 50.00\n2. Drinks - 40.00\n3. Clothes - 70.00\n\n");
   printf("-----------------------\n\n");
// Amount of Orders
   do{
      printf("How many items will you purchase?\n");
      printf("Enter amount here: ");
      scanf("%d", &amountItem);

      if (amountItem < 1){
         printf("\nINVALID INPUT!\n");
      }
      
      printf("\n-----------------------\n");
   } while(amountItem < 1);
 // Main Machinery     
   for (int i = 0; i < amountItem; i++){
      printf("\nOrder # %d\n", i + 1);
      printf("What would you like to buy?\n");
      printf("Enter choice here: ");
      scanf("%d", &choice);
   // Invalid Input
      if (choice < 1  || choice > 3){
         printf("\nItem Not Available!\n");
         printf("\n-----------------------\n");
         i -= 1;
         continue;
      }
   // Choice # 1
      if(choice == 1){
         price = 50.00;

         do{
            printf("\nHow many orders of item # 1 would you like?\n");
            printf("Enter amount here: ");
            scanf("%f", &orderAmount);

            if (orderAmount < 1){
               printf("\nINVALID INPUT!\n");
            }
         } while (orderAmount < 1);
         
         printf("\n-----------------------\n");

         itemCharge = price * orderAmount;
         totalCharge += itemCharge;

         printf("\n%.0f orders of item # 1\n", orderAmount);
         printf("Item Charge is: %.2f\n", itemCharge);
         printf("Total charge is: %.2f\n", totalCharge);
         printf("\n-----------------------\n");
   // Choice # 2      
      } else if(choice == 2){
         price = 40.00;

         do{
            printf("\nHow many orders of item # 2 would you like?\n");
            printf("Enter amount here: ");
            scanf("%f", &orderAmount);

            if (orderAmount < 1){
               printf("\nINVALID INPUT!\n\n");
            }
         } while (orderAmount < 1);
         
         printf("\n-----------------------\n");

         itemCharge = price * orderAmount;
         totalCharge += itemCharge;

         printf("\n%.0f orders of item # 2\n", orderAmount);
         printf("Item Charge is: %.2f\n", itemCharge);
         printf("Total charge is: %.2f\n", totalCharge);
         printf("\n-----------------------\n");
   // Choise # 3
      } else if(choice == 3){
         price = 70.00;

         do{
            printf("\nHow many orders of item # 3 would you like?\n");
            printf("Enter amount here: ");
            scanf("%f", &orderAmount);

            if (orderAmount < 1){
               printf("\nINVALID INPUT!\n\n");
            }
         } while (orderAmount < 1);

         printf("\n-----------------------\n");
         
         itemCharge = price * orderAmount;
         totalCharge += itemCharge;

         printf("\n%.0f orders of item # 3\n", orderAmount);
         printf("Item Charge is: %.2f\n", itemCharge);
         printf("Total charge is: %.2f\n", totalCharge);
         printf("\n-----------------------\n");
      }
   }
// Final Charge
   do {
        printf("\nYour Final Charge is: %.2f\n\n", totalCharge);
        printf("Enter payment: ");
        scanf("%f", &payment);

        if(payment < totalCharge){
            printf("\nINSUFFICIENT BALANCE!\n");
        } else {
            change = payment - totalCharge;
            printf("\nAmount Paid: %.2f\n", payment);
            printf("Change: %.2f\n", change);
        }
        printf("\n-----------------------\n");
    } while(payment < totalCharge);
// Thank You
   printf("\nThank you for eating at MALL MALL!\nPlease come and shop here again!\n");
   printf("\n-----------------------\n\n");

   system("pause");
   return 0;
}