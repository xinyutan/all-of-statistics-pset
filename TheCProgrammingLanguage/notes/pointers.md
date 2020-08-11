### 5.7 Multidimensional Array

Initialization:

```
int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
```

Passing `arr[2][3]` to a function, we can use `f(int arr[2][3]) {}` or `f(int arr[][3])` or `f(int (*arr)[3])`.

Difference between `int *arr[3]` and `int (*arr)[3]`: 
- `int *arr[3]` is an array of 3 pointers to intergers
- `int (*arr)[3]` is a pointer to an array of 3 integers


