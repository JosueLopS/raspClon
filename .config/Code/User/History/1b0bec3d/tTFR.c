#include <wiringPi.h>
int main (void)
{
  wiringPiSetup () ;
  pinMode (15, OUTPUT) ;
  for (;;)
  {
    digitalWrite (21, HIGH) ; delay (500) ;
    digitalWrite (21,  LOW) ; delay (500) ;
  }
  return 0 ;
}