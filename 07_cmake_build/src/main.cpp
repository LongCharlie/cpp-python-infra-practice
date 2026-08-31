#include<iostream>
#include"math_utils.h"

int main(){
    int val = 7;
    std::cout << val << " 的平方是: " << math_utils::compute_square(val) << "\n";
    return 0;
}