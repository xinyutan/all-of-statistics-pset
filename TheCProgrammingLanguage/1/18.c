/* 1-18
 * Write a program to remove trailing blanks and tabs from each line of input,
 * and to delete entirely blank lines.
 */

#include <stdio.h>

#define MAXIMUM 1000
#define IN 1
#define OUT 0

int get_line(char line[], int lim);

int main() {
    char line[MAXIMUM];
    int c; // the last char in the line

    while ((c = get_line(line, MAXIMUM)) != EOF) {
        printf("%s", line);
        line[0] = '\0';
    }
}

int get_line(char line[], int lim) {
    int c, i, j, b, l, state;
    char blank[MAXIMUM];

    b = 0;
    l = 0;
    state = OUT;
    for (i = 0; i < lim && (c = getchar())!= EOF && c != '\n'; ++i) {
        if (c == ' ' || c == '\t') {
            if (state == IN)
                b = 0;
            blank[b] = c;
            ++b;
            state = OUT;
        }
        else {
            if (state == OUT && b > 0) {
                // copy previous blanks to current line
                for (j = 0; j < b; ++j, ++l)
                    line[l] = blank[j];
            }
            line[l] = c;
            ++l;
            state = IN;
        }

    }
    return c;
}
