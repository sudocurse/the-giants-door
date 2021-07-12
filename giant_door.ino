// ---------------------------------------------------------------------------
// Example NewPing library sketch that does a ping about 20 times per second.
// ---------------------------------------------------------------------------

#include <NewPing.h>

#define TRIGGER_PIN  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     11  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

void setup() {
  Serial.begin(115200); // Open serial monitor at 115200 baud to see ping results.
}

void loop() {
  delay(1);                     // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  //Serial.print("Ping: ");
  Serial.print(sonar.ping_cm()); // Send ping, get distance in cm and print result (0 = outside set distance range)
  //Serial.println("cm");
  Serial.println();
}

void calibrate()
{
  Serial.print(sonar.ping_cm());
}

/// make this code reachable eventually

bool check_knock(){
  return false;
}

bool ultrasonic_1pc(){
  // lol fix this logic. this is where we'd put the smoothing or debounce or whatever
  if (sonar.ping_cm() < MAX_DISTANCE) {
    return true;
  }
}

bool check_letterbox(){

  return false;
}

bool knock_play() { 
    int MAX_RECORDING_TIME = 15; // seconds
  
    // 1. give instructions, and a beep
    // TODO once we have a speaker
    // 2. record for MAX_RECORDING_TIME 
    // TODO once we have a mic
    
    // TODO if there's an error or flatline, return false so it doesnt print a receipt
    
    return true;
}

bool letter_play(){
    
    return false;
}

bool print_receipt(){
    return false;
}

void event_main(){
    bool KEEP_GOING = true;
    while(KEEP_GOING){
        if (check_knock() == true) {

            // if a knock has been detected, the voice recording routine triggers
            
            if (knock_play() == true){
              print_receipt();
            } // lol what about error conditions
            
            continue;
        } else if (check_letterbox() == true) { 

            // if a letter's dropped, 

            if (letter_play() == true){
              // if a letter is received, print a receipt and thank them
              print_receipt();
              // Thank you, please take a receipt!
              // play_thank_you();
              
            } // lol what about error conditions
            
            continue;
        }
    }
}

