/*
 * 1-10 Write a program to copy its input to its output, replacing each tab by \t,
 * each backspace by \b, and each backslash by \\.
 * Note: I can't get \b to work. The reason is stated here:
 * https://stackoverflow.com/a/4363345
*/
#include <stdio.h>

int main() {
    int c;
    while ((c = getchar()) != EOF) {
        if (c == '\t')
            printf("\\t");
        else if (c == '\b' || c == 8 || c == 127)
            printf("\\b");
        else if (c == '\\')
            printf("\\\\");
        else
            putchar(c);
    }
}
