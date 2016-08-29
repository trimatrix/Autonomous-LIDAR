#include <utility.h>
#include <unwind-cxx.h>
#include <system_configuration.h>
#include <StandardCplusplus.h>
#include <SPI.h>
#include "RF24.h"
#include <algorithm>
#include <iterator>

RF24 radio(4, 5);
byte command[8];
int timeout = 0;
byte addresses[][6] = { "1Node","2Node" };
long randNum;

void recieve() {
	radio.read(&command, sizeof(command));
	Serial.write(command, sizeof(command));
}

void transmit() {
	Serial.readBytes(command, 8);
	radio.stopListening();
	radio.write(&command, sizeof(command));
	radio.startListening();
}

void setup() {
	Serial.begin(115200);

	radio.begin();
	radio.setPALevel(RF24_PA_MAX);
	radio.setDataRate(RF24_250KBPS);
	radio.setRetries(15, 15);
	radio.setPayloadSize(8);
	radio.openWritingPipe(addresses[0]);
	radio.openReadingPipe(1, addresses[1]);
	radio.startListening();

	randomSeed(analogRead(0));
}

void loop() {
	if (Serial.available() > 0) {
		transmit();
	}
	if (radio.available()) {
		recieve();
	}
}
