#include <stdio.h>

int main(){
// Days in a month
    int dayMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

// Birth Date
    int dayBday;
    int monthBday;
    int yearBday;

// Current Date
    int dayCurrent;
    int monthCurrent;
    int yearCurrent;

// Final Age
    int dayAge;
    int monthAge;
    int yearAge;

// Input
    printf("AGE EVALUATOR\n\n");

    // Birth Year
    do{
        printf("Enter Birth Year Here: ");
        scanf("%d", &yearBday);

        if (yearBday < 0){
            printf("\nINVALID INPUT!\n\n");
        }
        
    } while(yearBday < 0);

        // Leap Year
        if (yearBday % 4 == 0){
            dayMonth[1] = 29;
        }

        if (yearCurrent % 4 == 0){
            dayMonth[1] = 29;
        }

    // Birth Month
    do{
        printf("Enter Birth Month Here [1 - 12]: ");
        scanf("%d", &monthBday);

        if (monthBday < 1 || monthBday > 12){
            printf("\nINVALID INPUT!\n\n");
        }
    } while(monthBday < 1 || monthBday > 12);

    // Birth Day
    do{
        printf("Enter Birth Day Here: ");
        scanf("%d", &dayBday);

        if (dayBday < 1 || dayBday > dayMonth[monthBday - 1]){
            printf("\nINVALID INPUT!\n\n");
        }
        
    } while (dayBday < 1 || dayBday > dayMonth[monthBday - 1]);

    // Current Year
    do{
        printf("\nEnter Current Year Here: ");
        scanf("%d", &yearCurrent);

        if (yearCurrent < yearBday){
            printf("\nINVALID INPUT!\n\n");
        }
        
    } while(yearCurrent < yearBday);

    // Current Month
    do{
        printf("Enter Current Month Here [1 - 12]: ");
        scanf("%d", &monthCurrent);

        if (monthCurrent < 1 || monthCurrent > 12){
            printf("\nINVALID INPUT!\n\n");
        }
    } while(monthCurrent < 1 || monthCurrent > 12);

    // Current Day
    do{    
        printf("Enter Current Day Here: ");
        scanf("%d", &dayCurrent); 

        if (dayCurrent < 1 || dayCurrent > dayMonth[monthCurrent - 1]){
            printf("\nINVALID INPUT!\n\n");
        }
    } while(dayCurrent < 1 || dayCurrent > dayMonth[monthCurrent - 1]);
    
// Calculations
    if(monthBday > monthCurrent){
        yearCurrent -= 1;
        monthCurrent += 12;
    }

    if(dayBday > dayCurrent && monthBday == monthCurrent){
        dayCurrent += dayMonth[monthBday - 1];
    } else if(dayBday > dayCurrent){
        monthCurrent -= 1;
        dayCurrent += dayMonth[monthBday - 1];
    }
// Results
    yearAge = yearCurrent - yearBday;
    monthAge = monthCurrent - monthBday;
    dayAge = dayCurrent - dayBday;

// Output
    printf("\nYour age is %d Years, %d Months, %d Days old.\n\n", yearAge, monthAge, dayAge);

    return 0;
}