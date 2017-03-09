int photoTran = A2;
int reading = 0;
int led = 2;


void setup(){
  pinMode(photoTran,INPUT);
  pinMode(led,OUTPUT);
  digitalWrite(led,HIGH);
  Serial.begin(9600);
}

void loop(){
  reading = analogRead(photoTran);
  Serial.println(reading);
  delay(100);
}
