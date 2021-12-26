#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdio.h>

#define LED_Directions DDRA			
#define LED_Direction DDRB			
#define LED_PORT1 PORTA				
#define LED_PORT2 PORTB				

char array[]={0,1,2,3,4,5,6,7,8,9};
int k,j,i,factor;
int brightvalue=0;


void set_brightness(){
	int brightness = brightvalue;
	while (0 < brightness)
	{
		_delay_us(1);
		--brightness;
	}
}

ISR(TIMER0_OVF_vect)
{
	LED_PORT2 = 0x01;
	LED_PORT1 = array[k];
	set_brightness();

	LED_PORT2 = 0x02;
	LED_PORT1 = array[j];
	set_brightness();
				
	LED_PORT2 = 0x04;
	LED_PORT1 = array[i];
	set_brightness();
}

void SevenSeg_SetNumber(int num)
{
	k=num%10;
	num = num/10;
		
	j=num%10;
	num = num/10;
				
	i=num%10;
	num = num/10;
}

void sevseg_refreshDisplay(char refvalue)
{
	TIMSK=(1<<TOIE0);		/* Enable Timer0 overflow interrupts */
	TCNT0 = refvalue;		/* load TCNT0, count for 10ms*/
	TCCR0 = (1<<CS02) | (1<<CS00);  /* start timer0 with /1024 prescaler*/
}



int main(void)
{
	sei();
	LED_Directions = 0xff;		
	LED_Direction = 0xff;		
	LED_PORT1 = 0xff;
	LED_PORT2 = 0xff;
	sevseg_refreshDisplay(0xC2);	/* (for 10ms set 0xC2) */
	brightvalue=1000;		
	
	while(1)
	{
		SevenSeg_SetNumber(456);
		_delay_ms(1000);	/* wait for 1 second */
		SevenSeg_SetNumber(789);
 		_delay_ms(1000);
	}
}