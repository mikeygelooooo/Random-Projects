#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <conio.h>

// Main Function
int main(){
// Word Bank
  char wordBank[][50] = {"socialist", "subject", "belong", "banquet", "object", "deposit", "strategic", "regard", "modernize", "property", "applaud", "welfare", "transport", "anniversary", "conspiracy", "reflection", "discovery", "compact", "suspicion", "ambiguous"};
  char wordToGuess[50];
  char hiddenWord[50];
  char hiddenWordTemp[50];

// Random Word Generator
  int random;
  srand(time(0));
  random = rand() % sizeof(wordBank)/sizeof(wordBank[0]);

// Other Important Variables
  char guess;
  char choice;

// Word to Guess
  strcpy(wordToGuess, wordBank[random]);

// Hiding The Word
  strcpy(hiddenWord, wordToGuess);
  for (int h = 0; h < strlen(wordToGuess); h++){
    hiddenWord[h] = '*';
  }
  strcpy(hiddenWordTemp, hiddenWord);

// Title & Intro
  printf("\n------------------------------\n\n");
  printf("\tGUESS THE WORD\n\n");
  printf("------------------------------\n\n");
  printf("The Word Bank currently has %d words.\n\n", sizeof(wordBank)/sizeof(wordBank[0]));
  printf("------------------------------\n\n");
  printf("RULES\n");
  printf("1. Only use small letters\n2. Guess a letter wrong and you lose a try\n3. You have 10 tries only\n\n");
  printf("------------------------------\n\n");
  printf("Word To Guess: %s\n\n", hiddenWord);
  printf("------------------------------\n");

// Main Machinery
  for (int g = 10; g > 0; g--){
    printf("\nTRIES LEFT: %d\n\n", g);
    printf("Enter Guess Here: ");
    scanf(" %c", &guess);

  // Correct Guess
    for (int l = 0; l < strlen(wordToGuess); l++){
      if(guess == wordToGuess[l]){
        hiddenWordTemp[l] = guess;
      }
    }

  // Changes in Hidden Word
    if (!(strcmp(hiddenWordTemp, hiddenWord) == 0)){
      strcpy(hiddenWord, hiddenWordTemp);

      printf("\nYou Have Guessed Correctly!\n\n");
      printf("Word To Guess: %s\n\n", hiddenWord);
      printf("------------------------------\n");

      g += 1;
    } else {
      printf("\nIncorrect Guess!\n\n");
      printf("Word To Guess: %s\n\n", hiddenWord);
      printf("------------------------------\n");
    }
    
  // Word Completed
    if(strcmp(hiddenWord, wordToGuess) == 0){
        printf("\nCongratulations! You Have Guessed The Word!\n\n");
        printf("------------------------------\n\n");
        break;
    }
  }

  // Word Not Guessed
  if(!(strcmp(hiddenWord, wordToGuess) == 0)){
    printf("\nSorry! You are out of Tries!\n");
    printf("The Hidden Word is: %s\n\n", wordToGuess);
    printf("------------------------------\n\n");
  }

// Play Again
  do{
    printf("Would you like to try again?[Y = Yes, N = No]\n");
    printf("Enter choice here: ");
    scanf(" %c", &choice);

    if (choice == 'Y' || choice == 'y'){
      main();
    } else if (choice == 'N' || choice == 'n'){
      printf("\n------------------------------\n\n");
      printf("Thank you for playing 'GUESS THE WORD'!\n\n");
      printf("------------------------------\n\n");

      system("pause");
    } else {
      printf("\nINVALID INPUT!\n\n");
      printf("------------------------------\n\n");
    }
  } while (!(choice == 'Y' || choice == 'y' || choice == 'N' || choice == 'n'));
  
  return 0;
}

