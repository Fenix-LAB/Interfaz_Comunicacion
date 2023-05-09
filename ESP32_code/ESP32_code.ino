#define A0 13 
int lectura;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600,SERIAL_8N1, 3, 1);
  pinMode(A0, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  lectura = analogRead(A0);
  Serial.println(lectura);
  delay(100);
  
}
