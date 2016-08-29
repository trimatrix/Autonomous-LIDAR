#include <AccelStepper.h>
#include <Arduino.h>
char command[8];

AccelStepper motor(AccelStepper::DRIVER, 4, 5); //Driver,Pulse, Dir

long movePos = 200;
long acceleration;
long speed;
long maxSpeed;
char address = 99;
bool runMotor = false;
bool invert;
char sideLR = 'L';

union byCo {
	byte by[4];
	float fl;
	long lo;
};

void execCommand() {
	byCo conv;
	byCo send;

	for (int i = 4; i < 8; i++) {
		conv.by[i - 4] = command[i];
	}

	if (command[3] == 97) {        //0x61
		runMotor = true;
	}
	else if (command[3] == 98) {   //0x62
		runMotor = false;
	}
	else if (command[3] == 99) {   //0x63
		speed = conv.lo;
		motor.setSpeed(speed);
	}
	else if (command[3] == 100) {  //0x64
		maxSpeed = conv.lo;
		motor.setMaxSpeed(maxSpeed);
	}
	else if (command[3] == 101) {  //0x65
		acceleration = conv.lo;
		motor.setAcceleration(acceleration);
	}
	else if (command[3] == 102) {  //0x66
		invert = true;
		if (sideLR == 'L') {
			motor.setPinsInverted(invert, invert);
		}
		else if (sideLR == 'R') {
			motor.setPinsInverted(!invert, !invert);
		}
	}

	else if (command[3] == 103) {  //0x67
		invert = false;
		if (sideLR == 'L') {
			motor.setPinsInverted(invert, invert);
		}
		else if (sideLR == 'R') {
			motor.setPinsInverted(!invert, !invert);
		}
	}

	else if (command[3] == 104) {  //0x68
		movePos = conv.lo;
	}
	else if (command[3] == 105) {  //0x69
		send.lo = speed;
		byte reBack[8] = {
			0, address, command[1], 0,
			send.by[0], send.by[1], send.by[2], send.by[3] };
		reBack[0] = random(0, 255);
		Serial.write(reBack, 8);
	}
	else if (command[3] == 106) {  //0x70
		send.lo = maxSpeed;
		byte reBack[8] = {
			0, address, command[1], 0,
			send.by[0], send.by[1], send.by[2], send.by[3] };
		reBack[0] = random(0, 255);
		Serial.write(reBack, 8);

	}
	else if (command[3] == 107) {  //0x71
		send.lo = acceleration;
		byte reBack[8] = {
			0, address, command[1], 0,
			send.by[0], send.by[1], send.by[2], send.by[3] };
		reBack[0] = random(0, 255);
		Serial.write(reBack, 8);
	}
	else if (command[3] == 108) {  //0x71
		byte reBack[8] = {
			0, address, command[1], 0,
			invert, 0, 0, 0 };
		reBack[0] = random(0, 255);
		Serial.write(reBack, 8);
	}
}

void setup()
{
	Serial.begin(115200);
	if (sideLR == 'R') {
		motor.setPinsInverted(true, true);
	}
	randomSeed(analogRead(0));
}

void loop()
{
	if (Serial.available() > 0)
	{
		Serial.readBytes(command, 8);
		execCommand();
	}
	if (runMotor == true) {
		motor.move(movePos);
		motor.runSpeed();
	}

}