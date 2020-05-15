/* Write a program to print a histogram of the lengths
 * of words in its input. It's easy to draw the histogram
 * with the bars horizontal; a vertical orientation is more challenging.
 */

#include <stdio.h>

#define IN  1
#define OUT 0
#define UPPER 20

int main() {
    int c, state, len;
    state = OUT;
    len = 0;
    int freq[UPPER]; // freq[i] means the frequency of (i+1) length words
    int i, j;

    // initialize array
    for (i = 0; i < UPPER; ++i)
        freq[i] = 0;

    while((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            if (state == IN && len <= UPPER && len > 0)
                ++freq[len-1];
            state = OUT;
            len = 0;
        }
        else {
            if (state == OUT)
                state = IN;
            ++len;
        }
    }

    // print the histogram vertically
    int max_freq = 0;
    for (i = 0; i < UPPER; ++i)
        if (freq[i] > max_freq)
            max_freq = freq[i];

    printf("============================\n");
    printf("The Word Frequency Histogram\n");
    printf("============================\n\n");
    for(i = max_freq; i >= 0; --i) {
        for ( j = 0; j < UPPER; ++j) {
            if (freq[j] >= i)
                printf("--- ");
            else
                printf("    ");
        }
        printf("\n");
    }
    for (j = 1; j < UPPER + 1; ++j)
        printf("%3d ", j);
    printf("\n");
}

