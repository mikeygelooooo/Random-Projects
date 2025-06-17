#include <stdio.h>
#include <string.h>
#include <stdlib.h>
// Main Function
int main() {
// Variables
    char username[20];
    char password[20];
    int flag = 0;
// Welcome & Intro
    printf("---------------------------------------------\n\n");
    printf("Welcome to Intel!\n\nPlease log-in below:\n\n");
    printf("---------------------------------------------\n\n");
// Username        
    do {    
        printf("Input your username here: ");
        gets(username);

        if (strcmp(username, "itdept") == 0) {
        // Password
            do {
                printf("\nInput your password here: ");
                gets(password);

                if ((strcmp(password, "it2022") == 0) || (strcmp(password, "IT2022") == 0)) {
                    flag = 1;
                    printf("\n---------------------------------------------\n");
                    printf("\nWelcome to your Intel account!\n");
                    printf("\n---------------------------------------------\n");
                } else {
                    printf("\nINCORRECT PASSWORD!!!\n");
                    printf("\n---------------------------------------------\n\n");
                }
            } while (flag == 0);
        } else {
            printf("\nUSER DOES NOT EXIST!!!\n");
            printf("\n------------------------------\n\n");
        }
    } while (!(strcmp(username, "itdept") == 0));

    system("pause");
    return 0;
}