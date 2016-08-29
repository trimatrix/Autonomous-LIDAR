#include <Arduino.h>
char command[8];
int address = 101;

int dataPin = 4;
int latchPin = 5;
int clockPin = 6;
int LED[4] = { 7, 8, 9, 10 };


long lMoto[6];
long rMoto[6];
unsigned long relays;
volatile long distance;

union byCo {
	byte by[4];
	float fl;
	long lo;
};

void lMotoChange() {
	byCo conv;

	for (int i = 4; i < 8; i++) {
		conv.by[i - 4] = command[i];
	}
	if (command[3] == 97) {       
		lMoto[0] = 1;
	}
	else if (command[3] == 98) {   
		lMoto[0] = 0;
	}
	else if (command[3] == 99) {   
		lMoto[1] = conv.lo;
	}
	else if (command[3] == 100) {  
		lMoto[2] = conv.lo;
	}
	else if (command[3] == 101) {  
		lMoto[3] = conv.lo;
	}
	else if (command[3] == 102) {  
		lMoto[4] = 0;
	}
	else if (command[3] == 103) {  
		lMoto[5] = 0;
	}
}

void rMotoChange() {
	byCo conv;

	for (int i = 4; i < 8; i++) {
		conv.by[i - 4] = command[i];
	}
	if (command[3] == 97) {        
		rMoto[0] = 1;
	}
	else if (command[3] == 98) {   
		rMoto[0] = 0;
	}
	else if (command[3] == 99) {   
		rMoto[1] = conv.lo;
	}
	else if (command[3] == 100) {  
		rMoto[2] = conv.lo;
	}
	else if (command[3] == 101) {  
		rMoto[3] = conv.lo;
	}
	else if (command[3] == 102) {
		rMoto[4] = 0;
	}
	else if (command[3] == 103) { 
		rMoto[4] = 0;
	}
}

void execCommand() {
	byCo send;
	if (command[3] == 97) {
		digitalWrite(latchPin, LOW);
		shiftOut(dataPin, clockPin, MSBFIRST, command[4]);
		digitalWrite(latchPin, HIGH);
	}
	else if (command[3] == 98) {
		send.lo = distance;
		byte reBack[8] = {
			0, address, command[1], 0,
			send.by[0], send.by[1], send.by[2], send.by[3] };
		reBack[0] = random(0, 255);
		Serial.write(reBack, 8);
	}
	else if (command[3] == 99) { 
		send.lo = relays;
		byte reBack[8] = {
 			0, address, command[1], 0,
			send.by[0], send.by[1], send.by[2], send.by[3] };
		reBack[0] = random(0, 255);
		Serial.write(reBack, 8);
	}
	else if (command[3] == 100) {
		send.lo = distance;
		byte reBack[8] = {
			0, address, command[1], 0,
			send.by[0], send.by[1], send.by[2], send.by[3] };
		reBack[0] = random(0, 255);
		Serial.write(reBack, 8);
	}
}

void execUpdate() {
	if (command[2] == 0x6A) {
		lMotoChange();
	}
	else if (command[2] == 0x6B) {
		rMotoChange();
	}
	else if (command[2] == 0x6D) {
		lMotoChange();
		rMotoChange();
	}
	else if (command[1] == 0x63) {
		lMotoChange();
	}
	else if (command[1] == 0x64) {
		rMotoChange();
	}
	else if (command[1] == 0x69) {
		lMotoChange();
		rMotoChange();
	}
}
void posUpdate() {
	if (lMoto[4]) {
		distance -= 1;
	}
	else {
		distance += 1;
	}
}
void setup() {
	pinMode(latchPin, OUTPUT);
	pinMode(clockPin, OUTPUT);
	pinMode(dataPin, OUTPUT);
	for (int i = 0; i < sizeof(LED); i++) {
		pinMode(LED[i], OUTPUT);
	}
	digitalWrite(latchPin, LOW);
	shiftOut(dataPin, clockPin, LSBFIRST, B11111111);
	digitalWrite(latchPin, HIGH);
	Serial.begin(115200);
	attachInterrupt(digitalPinToInterrupt(2), posUpdate, RISING);

}

void loop() {
	if (Serial.available() > 0) {
		Serial.readBytes(command, sizeof(command));
		if (command[2] == 101) {
			execCommand();
		}

		else {
			execUpdate();
		}
	}
}