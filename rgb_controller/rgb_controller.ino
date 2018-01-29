int p3 = 3;
int p5 = 5;
int p6 = 6;
int val;

void setup() {
  //pinMode(p3, OUTPUT);
}

void loop() {
  val = analogRead(A4);
  analogWrite(p6, val/4);
  /*delay(1000);
  analogWrite(p3, val/4);
  delay(1000);
  analogWrite(p5, val/4);
  delay(1000);
  analogWrite(p3, 0);
  delay(1000);
  analogWrite(p6, 0);
  delay(1000);
  analogWrite(p5, 0);
  delay(1000);*/
}  
