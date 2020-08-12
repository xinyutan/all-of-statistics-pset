### 5.7 Multidimensional Array

Initialization:

```
int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
```

Passing `arr[2][3]` to a function, we can use `f(int arr[2][3]) {}` or `f(int arr[][3])` or `f(int (*arr)[3])`.

Difference between `int *arr[3]` and `int (*arr)[3]`: 
- `int *arr[3]` is an array of 3 pointers to intergers
- `int (*arr)[3]` is a pointer to an array of 3 integers

### 5.10 Command-line Arguments

I probably will be confused later by the content in the following paragraph:

For `int main(int argc, char *argv[]) {}`:

> Notice that `*++argv` is a pointer to an argument string, so `(*++argv)[0]` is its first character. (An alternate valid form would be `**++argv`.) Because [] binds tighter than * and ++, the parentheses are necessary; without them, the expression would be taken as `*++(argv[0])`. In fact, this is what we use in the inner loop, where the task is to walk along a specific argument string. In the inner loop, the expression `*++argv[0]`increments the pointer argv[0]!

Luckily,
> It is rare that one uses pointer expressions more complicated than these; in such acases, breaking them into two or three steps will be more intuitive.

