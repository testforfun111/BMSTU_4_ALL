PUBLIC input_number
PUBLIC number
PUBLIC len
PUBLIC real_numb
PUBLIC rev_numb
PUBLIC bin_len
PUBLIC bin_str
PUBLIC hex_len
PUBLIC hex_str

EXTRN print_newline: near
EXTRN convert_to_dec: near
EXTRN to_reverse_code: near
EXTRN convert_to_bin: near
EXTRN convert_to_hex: near

SEGDATA SEGMENT PARA PUBLIC 'DATA'
    max_size   db 8         ;максимальные символы можно в буфер
    len        db 0         ;количество символов из последнего ввода, которые можно вызвать
    number     db 8 DUP ("$")       ;строка цифр в восьмеричной системе счисления

    bin_len    db 0
    bin_str    db 16 DUP ("0")
               db "$" 
    
    hex_len    db 0
    hex_str    db 6 DUP ("$")
               db "$"

    real_numb  dw 0
    rev_numb   dw 0

    MSG  db "Enter number (octal with sign (-/+)): $"
SEGDATA ENDS

SEGCODE SEGMENT PARA PUBLIC 'CODE'
    ASSUME CS:SEGCODE, DS:SEGDATA
input_number proc near
    call init_num         ;инициализация 
    call print_newline

    mov ah, 9
    mov dx, offset MSG
    int 21h

    mov ah, 0AH
    mov dx, offset max_size
    int 21h

    call convert_to_dec       ;перевод из символов в число без знака в десятичную систему счисления
    call to_reverse_code    ;перевод в число с знаком -
    call convert_to_bin             ;перевод числа в двоичную систему счисления
    call convert_to_hex             ;перевод числа в шестнадцатеричную систему счисления
    call print_newline

    ret

input_number endp

init_num proc near
    mov len, 0
    mov bin_len, 0
    mov hex_len, 0
    mov real_numb, 0 
    mov rev_numb, 0

    mov ax, seg number
    mov es, ax                  ; es:di 
    mov di, offset number       
    mov al, "$"                 ;копирует регистр AL в память по адресу ES:DI 
    mov cx, 8                   ;длина 8
    rep stosb                   ;повторяет запись по байт

    mov ax, seg bin_str
    mov es, ax
    mov di, offset bin_str
    mov al, "0"
    mov cx, 16
    rep stosb

    mov ax, seg hex_str
    mov es, ax
    mov di, offset hex_str
    mov al, "0"
    mov cx, 6
    rep stosb 

    ret

init_num endp

SEGCODE ENDS
END
