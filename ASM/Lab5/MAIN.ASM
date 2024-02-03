EXTRN print_bin: near
EXTRN print_hex: near
EXTRN input_number: near
EXTRN print_newline: near

STK SEGMENT PARA STACK 'STACK'
    db 200 dup (?)
STK ENDS

SEGDATA SEGMENT PARA PUBLIC 'DATA'
    string_menu db "1. Enter number"
              db 10
              db 13
              db "2. Convert to unsigned binary and print it"
              db 10
              db 13
              db "3. Convert to signed hexadecimal and print it"
              db 10
              db 13
              db "4. Exit" 
              db 10
              db 13
              db "Enter action: $"

    arr_ptr     dw input_number, print_bin, print_hex, exit
SEGDATA ENDS

SEGCODE SEGMENT PARA PUBLIC 'CODE'
    ASSUME CS:SEGCODE, DS:SEGDATA, SS:STK
main:
    mov ax, SEGDATA
    mov ds, ax

    menu:
        mov ah, 9
        mov dx, OFFSET string_menu
        int 21h

        mov ah, 1
        int 21h
        mov ah, 0
        sub al, "1"
        mov bx, 2
        mul bx
        ;shl 
        mov bx, ax

        call print_newline
        call arr_ptr[bx]
        call print_newline
    jmp menu

exit proc near
    mov ah, 4ch
    int 21h
exit endp

SEGCODE ENDS
END MAIN
