PUBLIC print_bin
PUBLIC print_hex
PUBLIC print_newline

EXTRN real_numb: word
EXTRN number: byte
EXTRN bin_len: byte
EXTRN bin_str: byte
EXTRN hex_str: byte
EXTRN hex_len: byte

SEGDATA SEGMENT PARA PUBLIC 'DATA'
    bin_msg    db "Unsigned binary:"
               db 10
               db 13
               db "$"

    hex_msg    db "Signed hexadecimal:"
               db 10
               db 13
               db "$"
SEGDATA ENDS

SEGCODE SEGMENT PARA PUBLIC 'CODE'
    ASSUME CS:SEGCODE, DS:SEGDATA
print_bin proc near
    call print_newline

    mov ah, 9
    mov dx, offset bin_msg
    int 21h

    mov dx, offset bin_str
    int 21h

    call print_newline
    ret

print_bin endp

print_hex proc near
    call print_newline
    
    mov ah, 9
    mov dx, offset hex_msg
    int 21h

    mov dx, offset hex_str
    add dx, 5
    mov al, hex_len
    sub dl, al
    int 21h

    call print_newline
    ret
print_hex endp

print_newline proc near
    mov ah, 2
    mov dl, 10
    int 21h
    mov dl, 13
    int 21h

    ret
print_newline endp

SEGCODE ENDS
END
