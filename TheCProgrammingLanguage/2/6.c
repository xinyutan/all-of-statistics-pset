/* 2-6
 * Write a function setbits(x, p, n, y) that returns x with the n
 * bits at the position p set to the rightmost n bits of y, leaving
 * the other bits unchanged.
 */

#include <stdio.h>

unsigned setbits(unsigned x, int p, int n, unsigned y);
unsigned get_last_bits(unsigned x, int n);

int main() {
    printf("get_last_bits(37, 3) = %d\n", get_last_bits(37, 3));
    printf("get_last_bits(37, 2) = %d\n", get_last_bits(37, 2));
    printf("get_last_bits(37, 1) = %d\n", get_last_bits(37, 1));
    printf("get_last_bits(3, 2) = %d\n", get_last_bits(3, 2));

    printf("\nTesting setbits:\n");
    printf("setbits(5, 2, 2, 3) = %d (expect 7)\n", setbits(5, 2, 2, 3));
    printf("setbits(11, 2, 2, 6) = %d (expect 13)\n", setbits(11, 2, 2, 6));
    printf("setbits(3, 0, 1, 6) = %d (expect 2)\n", setbits(3, 0, 1, 6));
    printf("setbits(11, 3, 0, 29) = %d (expect 11)\n", setbits(11, 3, 0, 29));
}

// assume p, n are reasonable inputs
unsigned setbits(unsigned x, int p, int n, unsigned y) {
    unsigned xn, yn;
    xn = get_last_bits(x, p - n + 1);
    yn = get_last_bits(y, n);
    return ((((x >> (p - n + 1)) & (~0 << n)) | yn ) << (p - n + 1)) | xn;
}

// return last n bits of x
unsigned get_last_bits(unsigned x, int n) {
    return x & ~(~0 << n);
}

