#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    
    int a, b;
    cin >> a >> b;
    if (a > b) {
        printf(">");
    }
    else if (a == b) {
        printf("==");
    }
    else {
        printf("<");
    }

    return 0;
}