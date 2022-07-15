; este codigo contiene la informacion en asm

    global GS_
    section .text
GS_:
    ; [rdi] es color
    ; [rsi] es salida
    ; rcx es el limite

    xorpd xmm0, xmm0; color[0]
    xorpd xmm1, xmm1; color[1]
    xorpd xmm2, xmm2; color[2]
    xorpd xmm3, xmm3; salida[]

    mov r8,rdx  ; rdx va a poner el contador a r8
    cmp rdx, 0
    je done

constantes:
    xorpd xmm4, xmm4
    xorpd xmm5, xmm5
    xorpd xmm6, xmm6
    xorpd xmm7, xmm7

    mov r10, 2125 
    mov r11, 10000
    cvtsi2ss xmm4, r10
    cvtsi2ss xmm5, r11
    divss xmm4, xmm5

    mov r10, 7174
    mov r11, 10000
    cvtsi2ss xmm6, r10
    cvtsi2ss xmm5, r11
    divss xmm6, xmm5

    mov r10, 721
    mov r11, 10000
    cvtsi2ss xmm7, r10
    cvtsi2ss xmm5, r11
    divss xmm7, xmm5
    
    

loop1: 
    ;el valor de rdi va a almacenarse en cada xmmX cada 3 veces
    ;con un incremento de 12 variables
    ; 0.2125
    ; color[0]
    movss xmm0, [rdi] 
    mulss xmm0, xmm4
    add rdi, 4
    ; 0.7174
    ; color[1] 
    movss xmm1, [rdi] 
    mulss xmm1, xmm6
    add rdi, 4
    ; 0.0721
    ; color[2]
    movsd xmm2, [rdi] 
    mulss xmm2, xmm7
    add rdi, 4
    
    addss xmm3,xmm0
    addss xmm3,xmm1
    addss xmm3,xmm2

    movss [rsi], xmm3
    add rsi, 4
    
    xorpd xmm3, xmm3;
    ;xorpd xmm0, xmm0;
    ;xorpd xmm1, xmm1;
    ;xorpd xmm2, xmm2;

    sub r8,1      ; decrement
    cmp r8,0
    jne loop1   ; Loop while less or equal
done:
    ret
