#include <AccelStepper.h>

char command[8];
bool runMotor = false;
AccelStepper leftMotor(AccelStepper::DRIVER, 4, 5); //Driver,Pulse, Dir

union byCo {
	byte by[4];
	float fl;
	long lo;
};

void execCommand()
{
	byCo conv;

	for (int i = 0; i < 4; i++)
	{
		conv.by[i] = command[i + 2];
	}
	if (command[1] == 97)
	{
		runMotor = true;
		Serial.println("Motors are good to go");
	}
	else if (command[1] == 98)
	{
		runMotor = false;
		leftMotor.stop();
	}
	else if (command[1] == 99)
	{
		leftMotor.setSpeed(conv.lo);
		Serial.print("I set the Speed: ");
		Serial.println(conv.lo);
	}
	else if (command[1] == 100)
	{
		leftMotor.setMaxSpeed(conv.lo);
		Serial.print("I set the max Speed to: ");
		Serial.println(conv.lo);
	}
	else if (command[1] == 101)
	{
		leftMotor.setAcceleration(conv.lo);
		Serial.print("I set the Acceleration to: ");
		Serial.println(conv.lo);
	}
	else if (command[1] == 102)
	{
		leftMotor.setPinsInverted(true, true);
	}
	Serial.println("exiting exec stage");
}

void setup()
{
	Serial.begin(115200);
}

void loop()
{
	if (Serial.available() > 0)
	{
		Serial.readBytes(command, 8);
		Serial.println("Command:");
		for (int i = 0; i < 8; i++)
		{
			Serial.println(command[i], DEC);
		}
		execCommand();
	}
	if (runMotor == true && Serial.available() <= 0)
	{
		leftMotor.move(200);
		leftMotor.runSpeed();
	}

}
