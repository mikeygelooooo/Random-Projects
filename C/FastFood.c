#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// Main Function
int main(){
// Variables
    int item;
    float noOfOrders;
    float itemCharge;
    float itemCharge2;
    float totalCharge = 0;
    int answer;
    float payment;
    float change;
// Title & Intro
    printf("-----------------------\n\n");
    printf(" WELCOME TO WCDOMALDS\n\n");
    printf("-----------------------\n\n");
    getch();
    printf("Kaibigan kong gutom, pinakain ko ng alam mo na...\n\n");
    printf("-----------------------\n\n");
    getch();
// Menu
    printf("MENU:\n");
    printf("1. Appetizer - 30.00\n2. First Course - 40.00\n3. Main Course - 50.00\n4. Dessert - 40.00\n\n");
    printf("-----------------------\n\n");
// Main Machinery
    do {
    // Choice of Menu Item
        do{
            printf("Which menu item would you like?\n");
            printf("Enter choice here: ");
            scanf("%d", &item);

            if(item < 1 || item > 4){
                printf("\nItem is not on Menu!\n");
            }
            printf("\n-----------------------\n\n");
        } while(item < 1 || item > 4);
    // Item Charge
        if(item == 1){
            itemCharge = 30.00;
        } else if(item == 2){
            itemCharge = 40.00;
        } else if(item == 3){
            itemCharge = 50.00;
        } else if(item == 4){
            itemCharge = 40.00;
        }
    // Number of Items
        do{
            printf("How many orders of item # %d would you like?\n", item);
            printf("Enter amount here: ");
            scanf("%f", &noOfOrders);

            if(noOfOrders < 1){
                printf("\nINVALID INPUT!\n");
            }
            printf("\n-----------------------\n\n");
        } while(noOfOrders < 1);
    // Total Charge
        itemCharge2 = itemCharge * noOfOrders;
        totalCharge += itemCharge2;
        printf("%.0f orders of item # %d\n", noOfOrders, item);
        printf("Item Charge is: %.2f\n", itemCharge2);
        printf("Total charge is: %.2f\n", totalCharge);
        printf("\n-----------------------\n\n");
    // Order Again
        do{
            printf("Would you like to order another item? [1 = Yes, 0 = No]\n");
            printf("Answer here: ");
            scanf("%d", &answer);

            if(answer < 0 || answer > 1){
                printf("\nINVALID INPUT!\n");
            }
            printf("\n-----------------------\n\n");
        } while(answer < 0 || answer > 1);
    //Main Machinery Loop Condition
    } while (answer == 1);
// Final Charge
    do {
        printf("Your Final Charge is: %.2f\n\n", totalCharge);
        printf("Enter payment: ");
        scanf("%f", &payment);

        if(payment < totalCharge){
            printf("\nINSUFFICIENT BALANCE!\n");
        } else {
            change = payment - totalCharge;
            printf("\nAmount Paid: %.2f\n", payment);
            printf("Change: %.2f\n", change);
        }
        printf("\n-----------------------\n\n");
    } while(payment < totalCharge);
// Thank You
    printf("Thank you for eating at WCDOMALDS\nEnjoy your meal\nPlease come and dine here again!\n");
    printf("\n-----------------------\n\n");

    system("pause");

    return 0;
}