#

Some notes on Mindustry masm, might want to build my own compiler later

### if-else

Achieving a if-else statement in MASM


```c
if (a < b) {
    printf("a less than b")
} else {
    printf("b greater or equal a")
}
printf("outside")

```

The equivalent in MASM, please note that all jump label should be replaced by line number

```masm
jump %IF% lessThan a b
jump %ELSE% always
IF: print "a less than b"
jump %OUTSIDE% always
ELSE: print "b greater or equal a"
jump %OUTSIDE% always
OUTSIDE: print "outside"
```


### if

Some how a singular if statement is less intuitive for me than an if-else

```c
if ( a < b ) {
    printf("a less than b")
}
printf("outside")
```

```masm
jump %INSIDE% lessThan a b
jump %OUTSIDE always
INSIDE: print "a less than b"
OUTSIDE: printf "outside"
```

### if if-else else

```c
if (a < b) {
    printf(" a less than b")
} else if ( a == b) {
    printf("a equal b")
// infinite number of else if between
} else {
    printf("a greater than b")
}
printf("outside")
```

The following code could also be scaled infinitely

```masm
jump %IF% lessThan a b
jump %IFELSE1% equal a b
    // ... infinite number of if-else clause
jump %ELSE% always
IF: print "a less than b"
jump %OUTSIDE% always
IFELSE1: print "a equal b"
jump %OUTSIDE% always
    // ... infinite number of if-else body
    IFELSE-N: jump %OUTSIDE% always
ELSE: print "b greater or equal a"
jump %OUTSIDE% always
OUTSIDE: print "outside"
```
