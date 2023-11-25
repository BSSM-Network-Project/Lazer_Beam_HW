#include <DFRobot_TFmini.h>
#include <toneAC.h>
#define BUZZER_PIN 8  

SoftwareSerial mySerial(8, 7); 

DFRobot_TFmini  TFmini;
uint16_t distance, strength;

void setup() {
    Serial.begin(115200);
    TFmini.begin(mySerial);
}

void loop() {
    if (TFmini.measure()) {
        distance = TFmini.getDistance();
        strength = TFmini.getStrength();
        Serial.print("Distance = ");
        Serial.print(distance);
        Serial.println("mm");

        if (distance >= 100) { //100mm는 임시, 그리고 단위는 mm이니 10000 - 1meter
            playTone(1000000, 10);

        } 
        else {
            noToneAC();  // 일정거리 미만시 소리 끝
        }
    }
}

void playTone(int frequency, int duration) {
    toneAC(BUZZER_PIN, frequency, duration);
}
