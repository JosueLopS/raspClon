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
    ldr r1,=db_dest
    MOV R5,#0x5A 
copy:
    LDR R2,[R0] 
    STR R2,[R1] 
    ADD R0,#4 
    ADD R1,#4 
    subs r5,#1 
    bne copy 
    bx lr
    