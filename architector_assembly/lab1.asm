.text
main:
li $t1, 0
loop:
addi $t1,$t1,1
add $t0,$t0,$t1
bne $t1,9,loop
la $a0,label
li $v0,4
syscall 
move $a0,$t0
li $v0,1
syscall

.data
label: .asciiz "1-ees 9 hurteleh toonii niilber="