#include <SPI.h>
#include <Wire.h>
#include <RTClib.h>
#include <RF24.h>
#include <SD.h>
#include <StandardCplusplus.h>
#include <vector>

byte command[8];
RF24 radio(4, 5);
char address = 114;
byte addresses[][6] = { "1Node","2Node" };
RTC_DS1307 RTC;
bool dateCommand[7] = {1,1,1,1,1,1,1};
int timeout = 0;
File logFile;
int dataPin = 47;
int latchPin = 46;
int clockPin = 45;


union byCo {
	byte by[4];
	long lo;
	float fl;
};

String RTCParser(DateTime now, bool parts[7]) {

	String ParsedTime = "";

	if (parts[1] == true) {
		ParsedTime += String(now.year(), DEC);
	}

	if (parts[0] == true) {
		ParsedTime += "/";
	}

	if (parts[2] == true) {
		if (now.month() < 10) {
			ParsedTime += "0";
			ParsedTime += String(now.month(), DEC);
		}
		else {
			ParsedTime += String(now.month(), DEC);
		}
	}

	if (parts[0] == true) {
		ParsedTime += "/";
	}

	if (parts[3] == true) {
		if (now.day() < 10) {
			ParsedTime += "0";
			ParsedTime += String(now.day(), DEC);
		}
		else {
			ParsedTime += String(now.day(), DEC);
		}
	}

	if (parts[0] == true) {
		ParsedTime += "-";
	}

	if (parts[4] == true) {
		if (now.hour() < 10) {
			ParsedTime += "0";
			ParsedTime += String(now.hour(), DEC);
		}
		else {
			ParsedTime += String(now.hour(), DEC);
		}
	}

	if (parts[0] == true) {
		ParsedTime += ":";
	}

	if (parts[5] == true) {
		if (now.minute() < 10) {
			ParsedTime += "0";
			ParsedTime += String(now.minute(), DEC);
		}
		else {
			ParsedTime += String(now.minute(), DEC);
		}
	}

	if (parts[0] == true) {
		ParsedTime += ":";
	}

	if (parts[6] == true) {
		if (now.second() < 10) {
			ParsedTime += "0";
			ParsedTime += String(now.second(), DEC);
		}
		else {
			ParsedTime += String(now.second(), DEC);
		}
	}

	return ParsedTime;
}


void execInterCommand(DateTime now) {
	byCo send;
	if (command[3] == 97) {
		digitalWrite(latchPin, LOW);
		shiftOut(dataPin, clockPin, MSBFIRST, command[4]);
		digitalWrite(latchPin, HIGH);
	}
	else if (command[3] == 98) {
		;
	}
	else if (command[3] == 99) {
		;
	}
}


void transferCommand(DateTime now) {

	if (command[2] == 97) {         //0x61 a
		radio.stopListening();
		radio.write(&command, sizeof(command));
		radio.startListening();
	}

	else if (command[2] == 98) {    //0x62 b
		Serial.write(command, 8);
	}

	else if (command[2] == 99) {    //0x63 c
		Serial1.write(command, 8);
	}

	else if (command[2] == 100) {   //0x64 d
		Serial2.write(command, 8);
	}

	else if (command[2] == 101) {   //0x65 e
		Serial3.write(command, 8);
	}

	else if (command[2] == 102) {   //0x66 f
		Serial.write(command, 8);
		Serial1.write(command, 8);
	}
	else if (command[2] == 103) {   //0x67 g
		Serial.write(command, 8);
		Serial2.write(command, 8);
	}
	else if (command[2] == 104) {   //0x68 h
		Serial.write(command, 8);
		Serial3.write(command, 8);
	}
	else if (command[2] == 105) {   //0x69 i
		Serial1.write(command, 8);
		Serial2.write(command, 8);
	}
	else if (command[2] == 106) {   //0x6A j
		Serial1.write(command, 8);
		Serial3.write(command, 8);
	}
	else if (command[2] == 107) {   //0x6B k
		Serial2.write(command, 8);
		Serial3.write(command, 8);
	}
	else if (command[2] == 108) {   //0x6C l
		Serial.write(command, 8);
		Serial1.write(command, 8);
		Serial2.write(command, 8);
	}
	else if (command[2] == 109) {   //0x6D m
		Serial1.write(command, 8);
		Serial2.write(command, 8);
		Serial3.write(command, 8);
	}
	else if (command[2] == 110) {   //0x6E n
		Serial.write(command, 8);
		Serial2.write(command, 8);
		Serial3.write(command, 8);
	}
	else if (command[2] == 111) {   //0x6F o
		Serial.write(command, 8);
		Serial1.write(command, 8);
		Serial3.write(command, 8);
	}
	else if (command[2] == 112) {   //0x70 p
		Serial.write(command, 8);
		Serial1.write(command, 8);
		Serial2.write(command, 8);
		Serial3.write(command, 8);
	}
	else if (command[2] == 113) {   //0x71 q
		;
	}
	else if (command[2] == 114) {   //0x72 r
		execInterCommand(now);
	}
}

void internalListen(DateTime now) {
	if (Serial.available()) {
		Serial.readBytes(command, 8);
		String  com = "";
		for (int i = 0; i < 8; i++) {
			com += String(command[i], HEX);
			com += " ";
		}
		logFile = SD.open("LOG.txt", FILE_WRITE);
		logFile.println(com);
		logFile.close();
		transferCommand(now);
	}

	if (Serial1.available()) {
		Serial1.readBytes(command, 8);
		String  com = "";
		for (int i = 0; i < 8; i++) {
			com += String(command[i], HEX);
			com += " ";
		}
		logFile = SD.open("LOG.txt", FILE_WRITE);
		logFile.println(com);
		logFile.close();
		transferCommand(now);
	}

	if (Serial2.available()) {
		Serial2.readBytes(command, 8);
		String  com = "";
		for (int i = 0; i < 8; i++) {
			com += String(command[i], HEX);
			com += " ";
		}
		logFile = SD.open("LOG.txt", FILE_WRITE);
		logFile.println(com);
		logFile.close();
		transferCommand(now);
	}

	if (Serial3.available()) {
		Serial3.readBytes(command, 8);
		String  com = "";
		for (int i = 0; i < 8; i++) {
			com += String(command[i], HEX);
			com += " ";
		}
		logFile = SD.open("LOG.txt", FILE_WRITE);
		logFile.println(com);
		logFile.close();
		transferCommand(now);
	}
}

void externalListen(DateTime now) {
	if (radio.available()) {
		radio.read(&command, sizeof(command));
		String  com = "";
		for (int i = 0; i < 8; i++) {
			com += String(command[i], HEX);
			com += " ";
		}
		logFile = SD.open("LOG.txt", FILE_WRITE);
		logFile.println(com);
		logFile.close();
		transferCommand(now);
	}
}

void setup() {
	SD.begin(10, 11, 12, 13);

	pinMode(latchPin, OUTPUT);
	pinMode(clockPin, OUTPUT);
	pinMode(dataPin, OUTPUT);
	digitalWrite(latchPin, LOW);
	shiftOut(dataPin, clockPin, LSBFIRST, B11111111);
	digitalWrite(latchPin, HIGH);


	Serial1.begin(115200);
	Serial2.begin(115200);
	Wire.begin(); //initialize RTC auxilery library
	RTC.begin(); //initialize RTC

	radio.begin();
	radio.setPALevel(RF24_PA_MAX);
	radio.setDataRate(RF24_250KBPS);
	radio.setRetries(15, 15);
	radio.setPayloadSize(8);
	radio.openWritingPipe(addresses[1]);
	radio.openReadingPipe(1, addresses[0]);
	radio.startListening();

	logFile = SD.open("LOG.txt", FILE_WRITE);
	DateTime now = RTC.now();
	logFile.println(" CART STARTED"); //writes completed task
	logFile.close();
}

void loop() {
	DateTime now = RTC.now();
	externalListen(now);
	internalListen(now);
}
