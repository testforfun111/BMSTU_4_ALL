.686
.model flat, c
.stack
.code

public my_strcpy

my_strcpy proc
    mov esi, ecx 
    mov edi, edx
    mov ecx, eax

    cmp edi, esi
    je exit
	jl copy

	mov eax, edi
	sub eax, esi

	cmp eax, ecx
	jge copy

complicated_copy : 
	add edi, ecx
	add esi, ecx
	sub esi, 1
	sub edi, 1
	std

copy:
    rep movsb
    cld
exit:
    ret
my_strcpy endp

end