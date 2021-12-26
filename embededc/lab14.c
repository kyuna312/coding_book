

#include <avr/io.h>
#include <util/delay.h>

 

int main(void) {

DDRD = DDRD | ( 1<<4) ;
DDRC = DDRC & ~(1<<5) ; 

while (1) {

if(PINC & (1<<5) ) {
    PORTD = PORTD | ( 1<<4) ; 
}
else{
    PORTD = PORTD &  ~( 1<<4) ; 
}

} 

