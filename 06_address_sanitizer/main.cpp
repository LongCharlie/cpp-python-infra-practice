#include <iostream>

int main() {
    // 1. 在堆上分配容量为 5 的整型数组（合法索引范围：0 ~ 4）
    int* arr = new int[5]{10, 20, 30, 40, 50};

    std::cout << "[合法访问] arr[0] = " << arr[0] << "\n";
    std::cout << "[合法访问] arr[4] = " << arr[4] << "\n";

    // 2. 故意触发堆越界读（索引 5 已超出申请范围）
    std::cout << "[故意越界] 正在尝试读取 arr[5]...\n";
    int val = arr[5]; 
    std::cout << "[越界读出] arr[5] = " << val << "\n";

    delete[] arr;
    return 0;
}