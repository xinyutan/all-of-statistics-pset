/* 2-7
 * Write a function invert(x, p, n) that returns x with the n
 * bits that begins at p inverted, leaving the others unchanged.
 */

#include <stdio.h>

unsigned invert(unsigned x, int p, int n);

int main() {
    printf("====Testing invert====\n");
    printf("invert(5, 1, 1) = %d (expect 7)\n", invert(5, 1, 1));
    printf("invert(25, 3, 2) = %d (expect 21)\n", invert(25, 3, 2));
    printf("invert(25, 4, 1) = %d (expect 9)\n", invert(25, 4, 1));
    printf("invert(25, 4, 2) = %d (expect 1)\n", invert(25, 4, 2));
}

unsigned invert(unsigned x, int p, int n) {
   return (((x >> (p - n + 1)) ^ ~(~0 << n)) << (p - n + 1))
       | (x & ~(~0 << (p -n + 1)));
}
