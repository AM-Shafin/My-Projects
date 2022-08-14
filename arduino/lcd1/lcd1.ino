
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup()
{
  lcd.begin(16, 2);
}

void loop() {
  lcd.print("Arduino");
  delay(3000);

  lcd.setCursor(2, 1);
  lcd.print("LCD Testing");
  delay(3000);
  lcd.clear();

  lcd.blink();
  delay(4000);

  lcd.setCursor(7, 1);
  delay(3000);
  lcd.noBlink();

  lcd.cursor();
  delay(4000);

  lcd.noCursor();

  lcd.clear();
}
