#include <stdio.h>
#include "example.h"  // example_component's public interface

int main(void) {
    int result = add(2, 3);
    printf("2 + 3 = %d\n", result);
    return 0;
}
