PUBLIC convert_to_dec
PUBLIC to_reverse_code
PUBLIC convert_to_bin

EXTRN rev_numb: word
EXTRN real_numb: word
EXTRN len: byte
EXTRN number: byte
EXTRN bin_len: byte
EXTRN bin_str: byte
EXTRN hex_len: byte
EXTRN hex_str: byte
EXTRN print_newline:near

SEGCODE SEGMENT PARA PUBLIC 'CODE'
    ASSUME CS:SEGCODE

convert_to_dec proc near
    mov cx, 0
    mov cl, len
    dec cx
    mov si, cx  ;начал процесс из младшего бита
    mov bx, 1

    cmp len, 1  ;только 1 цифра без знак
    je continue

    loop_dec:
        mov ax, 0
        mov al, number[si]
        sub ax, "0"
        mul bx
        add real_numb, ax 

        mov ax, bx ;увеличить значение bx на 8 раз
        mov bx, 8
        mul bx
        mov bx, ax
        dec si

        loop loop_dec
    
    cmp number[0], "-"
    jne check_sign
    ret
    
    check_sign:
        cmp number[0], "+"
        jne continue
        ret
    continue:
        mov ax, 0
        mov al, number[si]
        sub ax, "0"
        mul bx 
        add real_numb, ax 
        ret 
convert_to_dec endp

to_reverse_code proc near
    mov ax, real_numb
    mov rev_numb, ax
    neg rev_numb
    ret
to_reverse_code endp
    
convert_to_bin proc near
    cmp number[0], "-"
    je rev_to_ax
    mov ax, real_numb

    back:
    mov si, 15
    mov dx, 0
    mov bx, 2

    loop_bin:
        div bx
        mov bin_str[si], dl
        add bin_str[si], "0"
        mov dx, 0
        inc bin_len

        dec si
        cmp ax, 0
        jne loop_bin

    ret
    rev_to_ax:
        mov ax, rev_numb
        jmp back
convert_to_bin endp

convert_to_hex proc near
    mov dx, 0
    mov cx, 0

    mov bx, 16
    mov si, 5
    mov ax, real_numb

    loop_hex:
        div bx
        mov hex_str[si], dl

        cmp dl, 9 
        jg hex_char
        add hex_str[si], "0"

        back:
        mov dx, 0
        inc hex_len

        dec si
        cmp ax, 0
        jne loop_hex

    cmp number[0], "-"
    je add_sign
    cmp number[0], "+"
    je add_sign
    ret

    hex_char:
        add hex_str[si], 55
        jmp back
    add_sign:
        mov bx, 0
        mov bl, 5
        sub bl, hex_len
        mov dh, number
        mov hex_str[bx], dh
        ret

convert_to_hex endp

SEGCODE ENDS
END
