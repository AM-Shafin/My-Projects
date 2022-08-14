#include<LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

String message[] = {
  "Shafin!",
  "Bushra!",
  "Friends!!",
  "Sir!",
  "Madam!"
};

void setup() {
  lcd.begin(16, 2);
}

void loop() {
  for(int i=0; i<5; i++) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Hello");
    lcd.setCursor(6,1);
    lcd.print(message[i]);
    delay(3000);
  }
}
