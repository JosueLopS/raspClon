#include <wiringPi.h>
int main (void)
{
  wiringPiSetup () ;
  pinMode (17, OUTPUT) ;
  for (;;)
  {
    digitalWrite (17, HIGH) ; delay (500) ;
    digitalWrite (17,  LOW) ; delay (500) ;
  }
  return 0 ;
}