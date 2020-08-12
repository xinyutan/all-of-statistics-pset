#include <stdio.h>

#define BUFFER_SIZE 100
static char buf[BUFFER_SIZE];
static int bufp = 0;

int getch(void) {
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c) {
    if (bufp >= BUFFER_SIZE)
        printf("ungetch: too many characters\n");
    else
        buf[bufp++] = c;
}
