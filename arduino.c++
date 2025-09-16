#include <DHT.h>
#include <Servo.h>

#define DHTPIN 4      
#define DHTTYPE DHT11
const int buzzer = 7;

Servo motor;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println("Início do sistema!");

  pinMode(buzzer, OUTPUT);
  dht.begin();
  motor.attach(8);
}

void loop() {
  delay(2000);

  float temperatura = dht.readTemperature();

  if (isnan(temperatura)) {
    Serial.println("Falha na leitura do sensor!");
    return;
  }

  if (temperatura > 26) {
    digitalWrite(buzzer, HIGH);
    motor.write(180);
  } else {
    digitalWrite(buzzer, LOW);
    motor.write(0);
  }

  Serial.println("Nova leitura");
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C\n");
}
