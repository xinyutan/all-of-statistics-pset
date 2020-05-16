/* 1-19
 * Write a function reverse(s) that reverses the character string s.
 * Use it to write a program that reverses its input a line at a time
 */

#include <stdio.h>

#define MAX 10 // maximum length of a line allowed

int get_line(char line[], int lim);
void reverse_in_place(char s[], int len);

int main() {
    char line[MAX];
    int len;

    while ((len = get_line(line, MAX)) > 0){
        reverse_in_place(line, len);
        printf("Reversed: %s\n", line);
    }
}

int get_line(char line[], int lim) {
    int i, c;
    for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
        line[i] = c;

    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;
}

void reverse_in_place(char s[], int len) {
    int i, c;
    for (i = 0; i < len / 2; ++i) {
        c = s[i];
        s[i] = s[len - 1 - i];
        s[len - 1 - i] = c;
    }
}

