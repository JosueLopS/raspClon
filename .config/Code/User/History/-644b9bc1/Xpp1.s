/* Example.s Author: Description: */
/* -- Data section */ .data
Version:
Date:
/* Ensure variable is 4-byte aligned */
.balign 4
db_sour:@ 1 2 3 4 5 6 7 8 9 0
.ascii "LULU","LUCY","GEOO","LEON","AGUS","MAXI","MAJO","ALEX","TINA","ANDY"
.ascii "GINA","LUPE","LINA","PATY","TONY","TONI","LISA","LOLA","LALO","ANIS" 
.ascii "ARON","EDDY","GUSS","IVAN","JAIR","ZACK","MAGY","RAFA","RAUL","RICO" 
.ascii "SAMY","FAVY","ISIS","VIKY","JUAN","MARY","CECI","GABY","LILI","DANI" 
.ascii "NICO","CUCA","VERO","BERE","RENE","ROSA","SARA","SAUL","LUZZ","TEOO" 
.ascii "FLOR","PAME","LUIS","SUSY","TERE","JOSE","RAFA","POLO","PAZZ","PACO" 
.ascii "YOLA","ALMA","ROSY","ROSA","FANY","ELIA","ELII","BLAS","ANAA","SONY" 
.ascii "JENY","ERIC","ARES","EROS","ZEUS","IRIS","PEPE","KINO","BONI","ALDO" 
.ascii "LISA","DOLY","NORA","DORA","CRIS","CARO","REYY","IVON","BENI","ARAA" 
/* Ensure variable is 4-byte aligned */
.balign 4
db_dest: @ 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 
.word 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 
.word 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 
.word 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
/* -- Code section */ 
.text

/* 4 byte aligned */ 

.balign 4
.global main 
main:
    /*Programa para COPIAR datos en memoria FLASH a RAM (2000 0000H)*/ 
    ldr r0,=db_sour
    ldr r2,[r0]
    rev r2,r2 //Menor
    MOV R5, #0x5A-1
copy:
    add r0,#4
    ldr r3,[r0]
    rev r3,r3
    cmp r2,r3
    bmi menor
    mov r2,r3
menor:
    subs r5,#1
    bne copy   
        push {lr}
        rev r2,r2
        str r2,[r0]
        bl printf
        pop {lr}
    bx lr444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
