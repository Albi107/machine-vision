#include <cvzone.h>

/*SerialData serialData(1, 1); //(numOfValsRec,digitsPerValRec)
int valsRec[1]; // array of int with size numOfValsRec 

//0 or 1 = 1 digit
//0 to 99 = 2 digits
//0 to 999 = 3 digits

void setup() {
  serialData.begin();
  pinMode(13, OUTPUT);
 
  
}

void loop() {

  serialData.Get(valsRec);
  digitalWrite(13, valsRec[0]);
 
}
//send $1 to turn on led or $0 to turn off led */

SerialData serialData(2, 1); //(numOfValsRec,digitsPerValRec)
int valsRec[2]; // array of int with size numOfValsRec
int red = 8;
int blue = 9;
int green = 10;

void setup()
{serialData.begin(); 
  pinMode(red,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(green,OUTPUT);
}


void loop()
{
  serialData.Get(valsRec);
  digitalWrite(red,valsRec[0]); 
  digitalWrite(green,valsRec[1]);
  
}
