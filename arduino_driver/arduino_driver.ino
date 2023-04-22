;;;; ;;;;      ;;;;
;  ; ;         ;
;;;; ;    ;;;; ;
;    ;    ;    ;
;    ;;;; ;    ;;;; // by malisipi

#include "SevSeg.h"
#include <IRremote.hpp>

//#define DEBUG_MODE 1
#define VOL_UP 0xE718FF00
#define VOL_DOWN 0xAD52FF00
#define TRACK_PLAY_PAUSE 0xE31CFF00
#define TRACK_PREV 0xF708FF00
#define TRACK_NEXT 0xA55AFF00
#define COMMAND_01 0xBA45FF00
#define COMMAND_02 0xB946FF00
#define COMMAND_03 0xB847FF00
#define COMMAND_04 0xBB44FF00
#define COMMAND_05 0xBF40FF00
#define COMMAND_06 0xBC43FF00
#define COMMAND_07 0xF807FF00
#define COMMAND_08 0xEA15FF00
#define COMMAND_09 0xF609FF00
#define COMMAND_10 0xE619FF00
#define COMMAND_11 0xE916FF00
#define COMMAND_12 0xF20DFF00
#define RESPONSE_WAIT_MS 1000
#define DISPLAY_WAIT_MS 1000

#ifdef DEBUG_MODE
#define LED_FEEDBACK ENABLE_LED_FEEDBACK
#else
#define LED_FEEDBACK DISABLE_LED_FEEDBACK
#endif

SevSeg sevseg;
char time[5] = "----";
const byte numDigits = 4;
const byte digitPins[] = { 2, 3, 4, 5 };
const byte segmentPins[] = { 6, 7, 8, 9, 10, 11, 12, 13 };
const bool resistorsOnSegments = 0;

void setup() {
  sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins, resistorsOnSegments);
  sevseg.setBrightness(90);

  Serial.begin(9600);
  IrReceiver.begin(A0, LED_FEEDBACK);
  delay_with_display(2500, "PCrC");
}

void display(char* text){
  sevseg.setChars(text);
  sevseg.refreshDisplay();
}

void delay_with_display(int dt, char* text){
  for(int i=0; i<dt; i++){
    display(text);
    delay(1);
  }
}

void send_command(char* command){
  Serial.println(command);
  char resp[5] = "FAIL";
  for(int i=0; i<=RESPONSE_WAIT_MS; i++){
    delay(1);
    if(Serial.available()){
      i = RESPONSE_WAIT_MS+1;
      Serial.readStringUntil('\n').toCharArray(resp, 5);
    }
  }
  delay_with_display(DISPLAY_WAIT_MS, resp);
}

void loop() {
  if(Serial.available()){
    Serial.readStringUntil('\n').toCharArray(time, 5);
  }
  display(time);
  if (IrReceiver.decode()) {
    switch(IrReceiver.decodedIRData.decodedRawData){
      case VOL_UP:
        send_command("#VUP");
        break;
      case VOL_DOWN:
        send_command("#VDN");
        break;
      case TRACK_PLAY_PAUSE:
        send_command("#PLY");
        break;
      case TRACK_PREV:
        send_command("#PRV");
        break;
      case TRACK_NEXT:
        send_command("#NXT");
        break;
      case COMMAND_01:
        send_command("#C01");
        break;
      case COMMAND_02:
        send_command("#C02");
        break;
      case COMMAND_03:
        send_command("#C03");
        break;
      case COMMAND_04:
        send_command("#C04");
        break;
      case COMMAND_05:
        send_command("#C05");
        break;
      case COMMAND_06:
        send_command("#C06");
        break;
      case COMMAND_07:
        send_command("#C07");
        break;
      case COMMAND_08:
        send_command("#C08");
        break;
      case COMMAND_09:
        send_command("#C09");
        break;
      case COMMAND_10:
        send_command("#C10");
        break;
      case COMMAND_11:
        send_command("#C11");
        break;
      case COMMAND_12:
        send_command("#C12");
        break;
      default:
        break;
    }
    IrReceiver.resume();
  }
}