/* 3-1 Our binary search makes two tests inside the loop,
 * when one would suffice. Write a version with only one tests inside
 * the loop and measure the difference in run-time.
 *
 * ANS: when the array contains mostly unique elements, two methods
 * are similar in speed. But when the array contains mostly the same
 * elements, and we are looking for a repeated element, one test is slower.
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>

#define MAX 10000
#define REPEAT 1000

int binarysearch_1(int x, int v[], int n);
int binarysearch_2(int x, int v[], int n);
double perf_experment(int v[], int n, int xs[], int nx,
        int (*search) (int, int *, int));
void compare_result(int v[], int n, int xs[], int nx,
        int (*search1) (int, int *, int),
        int (*search2) (int, int *, int));

int main() {
    int i;
    int v[MAX];

    printf("====Experiment 1: array elements are unique====\n");
    for(i = 0; i < MAX; ++i)
        v[i] = 2*i + 1;

    int xs[5] = {-1, 3000, 10001, 15001, 30000};

    compare_result(v, MAX, xs, 5, binarysearch_1, binarysearch_2);
    printf("binarysearch with two tests = %f ms\n",
            perf_experment(v, MAX, xs, 5, binarysearch_1));

    printf("binarysearch with one test = %f ms\n",
            perf_experment(v, MAX, xs, 5, binarysearch_2));


    printf("\n====Experment 2: array elements are the same====\n");
    for (i = 0; i < MAX; ++i)
        v[i] = 5;
    xs[0] = 0;
    xs[1] = 5;
    xs[2] = 10;

    compare_result(v, MAX, xs, 3, binarysearch_1, binarysearch_2);
    printf("binarysearch with two tests = %f ms\n",
            perf_experment(v, MAX, xs, 3, binarysearch_1));

    printf("binarysearch with one test = %f ms\n",
            perf_experment(v, MAX, xs, 3, binarysearch_2));



}

void compare_result(int v[], int n, int xs[], int nx,
        int (*search1) (int, int *, int),
        int (*search2) (int, int *, int)) {
    int ix, res1, res2;
    for (ix = 0; ix < nx; ++ix) {
        res1 = search1(xs[ix], v, n);
        res2 = search2(xs[ix], v, n);
        assert((res1==-1 && res2==-1) || (v[res1] == v[res2]));
    }
    printf("Two binary search implementations give the same result.\n");

}

double perf_experment(int v[], int n, int xs[], int nx,
        int (*search) (int, int *, int)) {
    int ix, ir;
    clock_t begin = clock();
    for (ir = 0; ir < REPEAT; ++ ir)
        for (ix = 0; ix < nx; ++ix)
            search(xs[ix], v, n);
    clock_t end = clock();
    return (double)(end - begin) * 1000 / CLOCKS_PER_SEC;
}


int binarysearch_1(int x, int v[], int n) {
    int low, high, mid;
    low = 0;
    high = n - 1;
    while (low <= high) {
        mid = (low + high) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else
            return mid;
    }
    return -1;
}

int binarysearch_2(int x, int v[], int n) {
    int low, high, mid;
    low = 0;
    high = n - 1;
    while (low < high) {
        mid = (low + high) / 2;
        if (x <= v[mid])
            high = mid;
        else
            low = mid + 1;
    }
    if (v[high] == x)
        return high;
    return -1;
}

