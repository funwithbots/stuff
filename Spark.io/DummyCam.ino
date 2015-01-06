/*
Created to read either button 2 or a PIR sensor to trigger an alert mode on the SparkButton.

Copyright 2015, Bill Shaw. 
This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.

Rev 0.1 01/05/2015 BS Initial release
*/

#include "SparkButton/SparkButton.h"
#include "math.h"    

SparkButton b = SparkButton();
int ledPos = 0;
int PIR = D7;

void setup() {
    // Tell b to get everything ready to go
    b.begin();
    pinMode(PIR, INPUT);
}

void loop(){
    
    if (b.buttonOn(2) || digitalRead(PIR)) {  //alert mode on button press or PIR activation
//        for(int i=1; i<13; i++) {
//            b.ledOn(i, 127,0,0);
//            delay(10);
        b.allLedsOn(127,0,0);
//        }
//        for(int i=1; i<13; i++) {
//            b.ledOff(i);
//            delay(10);
//        }
        delay(80);
        b.allLedsOff();
        delay(80);
    }
    else { //standby mode
        ledPos += 1;
        ledPos %= 12;  //modulo
           b.ledOn(ledPos, 0, 20, 20); 
        // Now turn that LED on
        
        
        // Wait a mo'
        delay(160);
        
        // Turn the LEDs off so they don't all end up on
        b.ledOff(ledPos);
    
        
    }

}