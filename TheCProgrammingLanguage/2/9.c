/* 2-9
 * In a two's complement number system, x &= (x-1)
 * deletes the rightmost 1-bit in x. Explain why.
 * Use this observation to write a faster version of
 * bitcount
 */

#include <stdio.h>

unsigned bitcount(unsigned x);

int main() {

    printf("====Testing bitcount====\n");
    printf("bitcount(15) = %d (expect 4)\n", bitcount(15));
    printf("bitcount(40) = %d (expect 2)\n", bitcount(40));
    printf("bitcount(70) = %d (expect 3)\n", bitcount(70));

}

unsigned bitcount(unsigned x) {
    unsigned cnt = 0;
    while (x != 0) {
        x &= (x-1);
        ++cnt;
    }
    return cnt;
}
