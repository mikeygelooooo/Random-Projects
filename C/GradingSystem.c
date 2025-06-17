#include <stdio.h>
#include <stdlib.h>

// Main Function
int main(){
// Variables
   int noOfStudents;

// Intro
   printf("----------------------------------------\n");
   printf("----------------------------------------\n\n");
   printf("GRADES INPUT & CALCULATION SYSTEM\n\n");
   printf("----------------------------------------\n");
   printf("----------------------------------------\n");

// No. of Students
   do{
      printf("\nHow many students are in the class?\n");
      printf("Enter amount here: ");
      scanf("%d", &noOfStudents);

      if (noOfStudents < 1){
         printf("\nINVALID INPUT\n");
      }
   } while (noOfStudents < 1);

   printf("\n----------------------------------------\n");

// Important Arrays
   float gradesStudents[noOfStudents][4];
   char nameStudent[noOfStudents][50];
   float sumGrades[noOfStudents];
   float aveGrades[noOfStudents];

// Main Input Machinery
   for (int s = 0; s < noOfStudents; s++){
      printf("\nINPUT # %d\n", s + 1);
      printf("\nEnter Name of Student here: ");
      scanf("%s", nameStudent[s]);

      for (int g = 0; g < 4; g++){
         printf("Quarter # %d Grades here: ", g + 1);
         scanf("%f", &gradesStudents[s][g]);

         if (gradesStudents[s][g] < 1.0 || gradesStudents[s][g] > 100.0){
            g -= 1;
            
            printf("\nINVALID INPUT\n\n");
            
            continue;
         }
         
      }
      
      printf("\n----------------------------------------\n");
   }

// Main Calculation Machinery
   for (int ac = 0; ac < noOfStudents; ac++){
      for (int sc = 0; sc < 4; sc++){
         sumGrades[ac] += gradesStudents[ac][sc];
      }

      aveGrades[ac] = sumGrades[ac] * 0.25;
   }

// Final Output
   printf("----------------------------------------\n");
   printf("\nLIST OF STUDENTS & GRADES\n");
   printf("\n----------------------------------------\n");
   printf("----------------------------------------\n");

   for (int fs = 0; fs < noOfStudents; fs++){
      printf("\nSTUDENT # %d\n", fs + 1);
      printf("\nName: %s\n\n", nameStudent[fs]);

      for (int fg = 0; fg < 4; fg++){
         printf("Quarter # %d Grade: %.2f\n", fg + 1, gradesStudents[fs][fg]);
      }
      
      printf("\nGeneral Average: %.2f\n", aveGrades[fs]);
      
      if(aveGrades[fs] > 74.99){
         printf("\nRemarks: PASSED!\n");
      } else {
         printf("\nRemarks: FAILED!\n");
      }
      
      printf("\n----------------------------------------\n");  
   }

   system("pause");

   return 0;
}