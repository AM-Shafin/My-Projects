#include <LiquidCrystal.h>
byte slash[8] = {
  B0001,
  B0010,
  B0100,
  B1000,
  B0100,
  B0010,
  B0001,
  B0010,
};

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);
  lcd.createChar(7, slash);
}

void loop() {
  for(int i=0; i<=15; i++) {
    lcd.setCursor(i,0);
    lcd.write(7);
    delay(1000);
    lcd.clear();
  }
}
