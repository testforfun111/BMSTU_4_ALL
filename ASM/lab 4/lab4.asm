SSTACK SEGMENT STACK 'stack'
    DB 100h DUP (?)
SSTACK ENDS

SDATA SEGMENT PARA PUBLIC 'data'
    Enter_size DB "Input size: ", '$'
    Enter_matrix DB "Input matrix: ", 13, 10, "$"
    Result DB "Result: ", 13, 10, "$"
    n DB 1 
    m DB 1 
    m_max DB 9
    matrix DB 81 DUP ('0')
    limit_lower DB 'a'
    limit_upper DB 'm'
SDATA ENDS

SCODE SEGMENT PARA 'code'
    ASSUME CS:SCODE, DS:SDATA, SS:SSTACK

input_size:
    call input_c 
    sub al, 30h
    mov n, al 
    int 21h

    call input_c
    sub al, 30h 
    mov m, al
    int 21h
    ret 

input_c:  
    mov ah, 1 
    int 21h 
    ret 

input_matrix:
    mov bx, 0
    mov al, n
    mul m
    mov cl, al    ; установка счетчик равно m * n 
input_loop:
    mov ax, 0    ; ax = 0
    mov al, bh   ; bh = index   
    div n       
    mov dl, ah   ; j = dl 
    mul m_max    ; index = i * column 
    add al, dl   ; index = i * column + j 
    mov ah, 0    
    xchg si, ax  ; обмен(si, ax) si = index 
    call input_c 
    mov matrix[si], al
    int 21h 
    inc bh
    loop input_loop
    ret 

print_c:
    mov ah, 2
    int 21h
    ret 

print_space:
    mov ah, 2
    mov dl, ' '
    int 21h 
    jmp continue

print_newline:
    mov ah, 2 
    mov dl, 10 
    int 21h
    jmp continue

print_matrix:
    mov bx, 0
    mov al, n 
    mul m 
    mov cl, al 
print_loop:
    mov ax, 0
    mov al, bl 
    div n   
    mov dl, ah 
    mul m_max 
    add al, dl 
    mov ah, 0
    xchg si, ax
    mov dl, matrix[si]
    call print_c 
    inc bl
    mov ax, bx 
    div m 
    cmp ah, 0
    JE print_newline 
    JNE print_space
continue:
    loop print_loop
    ret

check_limit_upper:
    cmp limit_upper, dl 
    JAE change_to_upper
    jmp continue_process 
change_to_upper:
    sub matrix[si], 32 
    jmp continue_process

process:
    mov ax, 0
    mov bx, 0
    mov al, n 
    mul m 
    mov cl, al 
process_loop:
    mov ax, 0
    mov al, bl 
    div n   
    mov dl, ah 
    mul m_max 
    add al, dl 
    mov ah, 0
    xchg si, ax
    mov dl, matrix[si]
    cmp dl, limit_lower 
    JAE check_limit_upper
continue_process:
    inc bl 
    loop process_loop
    ret

print_string:
    mov ah, 09 
    int 21h
    ret
main:
    mov ax, SDATA 
    mov ds, ax 

    mov dx, OFFSET Enter_size
    call print_string
    call input_size

    mov dx, OFFSET Enter_matrix
    call print_string
    call input_matrix

    call process

    mov dx, OFFSET Result
    call print_string
    call print_matrix

    mov ah, 4ch 
    int 21h
SCODE ENDS
END main