  //=======SETUP=======//
// LIBRARIES
#include <Keypad.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h> 
#include <Adafruit_SSD1306.h>

// STEPPER MOTORS
const int   gearRatio = 4;  // Gear Ratio
const int   maxSpeed = 5000; // Spinning Speed (Max 75 - Stable 5000)
const float stepsPerRevInc = 200; // Step/Rev = 200
const int   stepsInc = 16; // 1/16 Degree Per Step           
const float stepperSpeed = maxSpeed/stepsInc; // Spinning Speed in Degree
const float stepsPerRev = stepsPerRevInc * stepsInc; // Spinning Speed Overal

// BOTTOM STEEPER MOTORS 
const int DIR = A2;  // Directio Pin Motor 1
const int STEP = A3; // Stepper  Pin Motor 1 

// TOP 2 STEPPER MOTORS
const int DIR1 = A0; // Directio Pin Motor 2    
const int STEP1 = A1;// Stepper  Pin Motor 2

const float angleCardOut = 2040; // #Steps for Shooting 1 Card

// Define LED pins
const int RED = 10;
const int GREEN = 11;
const int BLUE = 12;
const int GND = 13;

// SCREEN
Adafruit_SSD1306 display(128, 64, &Wire, -1); // Define OLED Screen
const unsigned char minions [] PROGMEM = 
{
  0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe0, 0x07, 0xf0, 0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x80, 0x01, 0xe0, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x00, 0x00, 0x00, 0x00, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xf8, 0x00, 0x19, 0xc0, 0x00, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x01, 0xff, 0xff, 0xe0, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xe0, 0x07, 0xff, 0xff, 0xf8, 0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 0x1f, 0xff, 0xff, 0xfc, 0x01, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 0xff, 0xff, 0xff, 0xff, 0xc0, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xc7, 0xff, 0xff, 0xfe, 0x0f, 0xf0, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0x8e, 0x00, 0x7f, 0xe0, 0x00, 0xf8, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0x18, 0x00, 0x1f, 0xc0, 0x00, 0x7c, 0x7f, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0x30, 0x7e, 0x07, 0x0f, 0x0c, 0x1e, 0x7f, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xfe, 0x62, 0x00, 0xc2, 0x30, 0x01, 0x0f, 0x3f, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xfe, 0x44, 0x00, 0x30, 0x60, 0x00, 0x87, 0x3f, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xfc, 0x88, 0x00, 0x18, 0xc0, 0x00, 0x47, 0x9f, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xfc, 0x90, 0x7f, 0x0f, 0x87, 0xf8, 0x23, 0x9f, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xfc, 0x20, 0x3f, 0xc7, 0x81, 0xfe, 0x11, 0x9f, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xf9, 0x60, 0x1f, 0xe7, 0x00, 0xff, 0x10, 0x9f, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xf8, 0x40, 0x0f, 0xf3, 0x00, 0x7f, 0x88, 0x07, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xf0, 0x41, 0x0f, 0xf2, 0x08, 0x7f, 0x88, 0x07, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xf0, 0x40, 0x0f, 0xf2, 0x00, 0x7f, 0xc0, 0x07, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xf0, 0x40, 0x1f, 0xf2, 0x00, 0xff, 0xc0, 0x07, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xf0, 0x48, 0x3f, 0xf2, 0x41, 0xff, 0xc8, 0x07, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xf0, 0x4e, 0xff, 0xf3, 0x3f, 0xff, 0x88, 0x07, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xf0, 0x47, 0xff, 0xf3, 0x3f, 0xff, 0x90, 0x07, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xf0, 0x67, 0xff, 0xe7, 0x9f, 0xff, 0x10, 0x07, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0x03, 0xf0, 0x21, 0xff, 0xc7, 0x8f, 0xfc, 0x21, 0xcf, 0xc0, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xf0, 0x01, 0xf9, 0x10, 0x7e, 0x08, 0xc0, 0x00, 0x23, 0xcf, 0x80, 0x0f, 0xff, 0xff, 
  0xff, 0xff, 0xe0, 0x00, 0xf9, 0x98, 0x00, 0x10, 0x60, 0x00, 0x47, 0xcf, 0x80, 0x07, 0xff, 0xff, 
  0xff, 0xff, 0xe0, 0x00, 0xf9, 0xc4, 0x00, 0x20, 0x30, 0x01, 0x8f, 0xcf, 0x00, 0x07, 0xff, 0xff, 
  0xff, 0xff, 0xe0, 0x30, 0xf9, 0xc3, 0x00, 0xc3, 0x0c, 0x06, 0x1f, 0xcf, 0x0c, 0x03, 0xff, 0xff, 
  0xff, 0xff, 0xc3, 0xf0, 0x19, 0xe0, 0xfe, 0x07, 0x81, 0xf0, 0x3f, 0xc8, 0x0f, 0xc3, 0xff, 0xff, 
  0xff, 0xff, 0xc3, 0xf0, 0x09, 0xf8, 0x00, 0x1f, 0xe0, 0x00, 0x7f, 0xc0, 0x0f, 0xc3, 0xff, 0xff, 
  0xff, 0xff, 0xc3, 0x00, 0x01, 0xfc, 0x00, 0x7f, 0xf0, 0x03, 0xff, 0xc0, 0x00, 0xc3, 0xff, 0xff, 
  0xff, 0xff, 0xc0, 0x00, 0x01, 0xff, 0xe3, 0xff, 0xff, 0xff, 0xff, 0xc0, 0x00, 0x03, 0xff, 0xff, 
  0xff, 0xff, 0xc0, 0x00, 0x00, 0xff, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xff, 0xff, 
  0xff, 0xff, 0xc0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xff, 0xff, 
  0xff, 0xff, 0xe0, 0x00, 0x0c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x07, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }; // Define Minion Pixel

// Define KEYPAD 
const byte ROWS = 4; 
const byte COLS = 4; 
char hexaKeys[ROWS][COLS] = 
{
  {'1', '2', '3', 'A'}, // 49 50 51 65
  {'4', '5', '6', 'B'}, // 52 53 54 66 
  {'7', '8', '9', 'C'}, // 55 56 57 67 
  {'*', '0', '#', 'D'}  // 42 48 35 68
};
//byte rowPins[ROWS] = {6, 7, 8, 9}; 
//byte colPins[COLS] = {2, 3, 4, 5};

byte rowPins[ROWS] = {5, 4, 3, 2}; 
byte colPins[COLS] = {9, 8, 7, 6}; 
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

//----------------------------------//----------------------------------
//----------------------------------//----------------------------------

//========RUN ONCE========
void setup() 
{

    // Define Pins Status 
    // SERIAL
    Serial.begin(9600); 
    
     // SCREEN
    display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
    
    //  BOTTOM MOTORS
     pinMode(STEP, OUTPUT);
     pinMode(DIR, OUTPUT);
    
    // TOP MOTORS
     pinMode(STEP1, OUTPUT);
     pinMode(DIR1, OUTPUT);

     // LEDs
     pinMode(RED, OUTPUT);
     pinMode(GREEN, OUTPUT);
     pinMode(BLUE, OUTPUT);
     pinMode(GND, OUTPUT);
     digitalWrite(GND,LOW);
}

void loop() 
{ 
  analogWrite(GREEN, 20);
  // MINION ANIMATION
  minion();
  char start = getChar();
  while(start != '#')
  {
    start = getChar();
  }
  display.clearDisplay();
  
  // HOME (OPTIONS) 
  option();
  char opt = getChar();
  
  // OPTIONS MODIFIED
  int player = 0;
  int card = 0;
  if (opt == 'A') 
  {
    askPlayers();
    player = getNumber();
    askCads();  
    card = getNumbrer();
  }
  else if (opt == 'B')
  {
    askPlayers();
    player = getNumber();  
    card = 2;
  }
  else if (opt == 'C')
  {
    askPlayers();
    player = getNumber();  
    card = 3;
  }
  else if (opt == 'D')
  {
    askPlayers();
    player = getNumber();  
    card = 13;
  }
  
  // GAME START SCREEN
  gameStart(player, card, opt);
  delay(500);
  
  // SPIN AROUND
  stepperRound(player, card);
  if (opt == 'B')
  {
    BlackJack(player);  
  }
  
  // ASK FOR PLAYING AGAIN
  askAgain();
  char playAgain = getChar();
  while (playAgain == '*')
  {
    gameStart(player, card, opt);
    delay(1000);
    stepperRound(player, card);
    if (opt == 'B')
    {
      BlackJack(player);  
    }
     askAgain();
     playAgain = getChar();
  }
  digitalWrite(BLUE,LOW); 
}

//=======FUNCTION======

//----------------------------------//----------------------------------
// KEYPAD - getNumber() - getChar()
//----------------------------------//----------------------------------

int getNumber()
{
  int number = 0;
  bool numbDone = false;
  while (!numbDone)
  {
    int numbIn = int(customKeypad.waitForKey()) - 48;
    if (numbIn == -13)
    {
      numbDone = true;
    }
    else if (numbIn ==  -6)
    {
      number = 0;
      blinkLED(RED,1);
    }
    else
    {
      number = number*10 + numbIn;
    }
  }
  blinkLED(GREEN,1);
  Serial.println(number);
  return number;
}
//----------------------------------
char getChar()
{
  char ch;
  bool charDone = false;
  while(!charDone)
  {
    ch = customKeypad.waitForKey();
    char charIn = customKeypad.waitForKey();
    if( charIn == '#')
    {
      charDone = true;
    }
    else if (charIn == '*')
    {
      ch = ' ';
      blinkLED(RED,1);
    }
  }
  blinkLED(GREEN,1);
  return ch;
}

//----------------------------------//----------------------------------
// LED - blinkLED(color, times)
void blinkLED(int color, int times)
{
  analogWrite(GREEN, 0);
  for (int i = 1; i <= times; i++)
  {
    analogWrite(color, 50);
    delay(50);
    analogWrite(color, 0);
    delay(50);
  }
    analogWrite(GREEN, 50);
}

//----------------------------------//----------------------------------
// SCREEN - minion()  - option() - askPlayers() - askCards() - askAgain()-askWithdraw() - gameStart(player, cards, opt)
//----------------------------------//----------------------------------
void minion()
{
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(BLACK, WHITE);  
  display.setCursor(0,0);
  display.println(" BELLO !!! ");
  display.display();
  display.drawBitmap(0, 16, minions, 128, 48, WHITE); 
  // display.drawBitmap(x position, y position, bitmap data, bitmap width, bitmap height, color)
  display.display();
  display.startscrollright(0x00, 0x01);
}
//----------------------------------
void option()
{
  display.clearDisplay();
  display.stopscroll();
  display.setTextSize(2);
  display.setCursor(0,0);
  display.setTextColor(WHITE);
  display.println("*OPTIONS:");
  display.setTextSize(1);
  display.println("(A) - CUSTOM");
  display.println("(B) - XI DACH");
  display.println("(C) - BAI CAO");
  display.println("(D) - TIEN LEN");
  display.println("(#) - CONFIRM");
  display.display();
}
//----------------------------------
void askPlayers()
{
  display.clearDisplay();
  display.setCursor(0,0);
  display.setTextSize(2);
  display.println("#Players");
  display.setTextSize(2);
  display.println("(#)Confirm(*)Cancel ");
  display.display();
}
//----------------------------------
void askCards()
{
  display.clearDisplay();
  display.setCursor(0,0);
  display.setTextSize(2);
  display.println("#Cards");
  display.println("(#)Confirm(*)Cancel ");
  display.display();
}
//----------------------------------
void askAgain()
{
  display.clearDisplay();
  display.setCursor(0,0);
  display.setTextSize(2);
  display.println("PLAY AGAIN");
  display.println("(*) + (#)");
  display.display();
}
//----------------------------------
void askWithdraw()
{
      display.clearDisplay();
      display.setCursor(0,0);
      display.setTextSize(2);
      display.println("Withdraw?");
      display.println("#Cards+(#)");
      display.display();
}
//----------------------------------
void gameStart(int players, int cards, char opt)
{
  display.clearDisplay();
  display.setCursor(0,0);
  display.setTextSize(2);
  display.println("GAME START");
  display.print("Players:");
  display.println(players);
  display.print("Cards:  ");
  display.println(cards);
  display.display();
}

//----------------------------------//----------------------------------
// STEPPER MOTORS - stepperSpin(stepsAngle, STEP) - cardOut() - stepperRound(player, card) - BlackJack(player)
//----------------------------------//----------------------------------
void stepperSpin(int stepsAngle, int STEP, int stepperSpeed)
{
  for(int i = 1; i <= stepsAngle; i++)
  {
    digitalWrite(STEP, HIGH);
    delayMicroseconds(stepperSpeed);
    digitalWrite(STEP, LOW); 
  }
}
//----------------------------------.
void cardOut()
{
  stepperSpin(angleCardOut,STEP1,70);
}
//----------------------------------
void stepperRound(int player, int card)
{ 
  int stepAngle = gearRatio * (3200/player);
  for( int i = 1; i <= card; i++)
  {
    Serial.println(stepAngle);
    digitalWrite(DIR, LOW);
    display.clearDisplay();
    display.setCursor(0,0);
    display.setTextSize(4);
    display.println("CARD OUT!");
    display.display();
    for (int i = 1; i <= player; i++)
    {
      cardOut();
      stepperSpin(stepAngle, STEP, stepperSpeed);
    }
    display.clearDisplay();
  }
}
//----------------------------------

void BlackJack(int player)
{
    int stepAngle = gearRatio*((stepsPerRev)/(player));
    stepperSpin(stepAngle, STEP, stepperSpeed);
    for (int i = 1; i <= player; i++)
    {
      askWithdraw();
      int cardDrawn = getNumber();
      while (cardDrawn != 0)
      {
        display.clearDisplay();
        display.setCursor(0,0);
        display.setTextSize(4);
        display.println("CARD OUT!");
        display.display();
        for (int i = 1; i <= cardDrawn; i++)
        {
          cardOut();
        }
        askWithdraw();
        cardDrawn = getNumber();
      }
        display.clearDisplay();
        display.setCursor(0,0);
        display.setTextSize(4);
        display.println("PASS");
        display.display();
        delay(1000);
      if(i!=player)
      {
        stepperSpin(stepAngle, STEP, stepperSpeed);
      }
    }   
}
