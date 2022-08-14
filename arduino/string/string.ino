#include<LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

String greetings[] = {
  "World!",
  "Motherfucker",
  "Piece of shit",
  "Jerk",
  "Fucking idiot",
  "Pussy",
  "Cunt",
  "Bastard",
  "Fuckface",
  "Bitch",
  "Dickhead",
  "Rubbish",
  "Twat",
  "Split ass",
};

void setup() {
  lcd.begin(16, 2);
}

void loop() {
   for(int j=0; j<=13; j++){  
      lcd.setCursor(4, 0);
      lcd.print("  Hello!!");
      lcd.setCursor(0, 1);
      lcd.print(greetings[j]);
      delay(1000);
      lcd.clear();
   }
}
