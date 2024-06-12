#include <wiringPi.h>
int main (void)
{
  wiringPiSetup () ;
  pinMode (12, OUTPUT) ;
  for (;;)
  {
    digitalWrite (12, HIGH) ; delay (500) ;
    digitalWrite (12,  LOW) ; delay (500) ;
  }
  return 0 ;
}