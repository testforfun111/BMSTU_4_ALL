SSTACK SEGMENT PARA STACK 'stack'
    DB 100 DUP (?)
SSTACK ENDS 

SDATA SEGMENT PARA 'data'
    number1 DB 1 
    number2 DB 1 
SDATA ENDS 

SCODE SEGMENT PARA 'code'
    ASSUME CS:SCODE, DS:SDATA, SS:SSTACK 
input_c proc 
    mov AH, 01h
    int 21h
    ret 
input_c endp
start:
    mov AX, SDATA
    mov DS, AX 

    call input_c
    mov number1, AL 

    call input_c
    mov number2, AL 

    mov AH, 02h
    mov DL, 32
    int 21h 

    mov AL, number1
    add AL, number2
    sub AL, 30h 
    mov DL, AL 
    mov AH, 02h 
    int 21h  

    mov AH, 4CH 
    int 21h 
    SCODE ENDS
END start