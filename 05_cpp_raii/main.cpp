#include <iostream>
#include <cstdio>
#include <utility>

class FileWrapper {
private:
    FILE* file_ptr_ = nullptr; // 底层 C 风格文件句柄

public:
    // 构造函数：获取资源
    explicit FileWrapper(const char* filepath, const char* mode) {
        file_ptr_ = std::fopen(filepath, mode);
        if (file_ptr_) {
            std::cout << "[RAII] 文件成功打开: " << filepath << "\n";
        } else {
            std::cout << "[RAII] 文件打开失败！\n";
        }
    }

    // TODO 1: 析构函数 —— 如果 file_ptr_ 不为空，关闭文件并打出日志
    ~FileWrapper() {
        // 提示：std::fclose(file_ptr_)
        if (file_ptr_ != nullptr){
            std::fclose(file_ptr_);
        }
    }

    // 禁用拷贝构造和拷贝赋值（禁止复制句柄）
    FileWrapper(const FileWrapper&) = delete;
    FileWrapper& operator=(const FileWrapper&) = delete;

    // TODO 2: 实现移动构造函数 (Move Constructor)
    // 提示：抢过来 other 的 file_ptr_，并将 other.file_ptr_ 置为 nullptr
    FileWrapper(FileWrapper&& other) noexcept {
        // ...
        this -> file_ptr_ = other.file_ptr_;
        other.file_ptr_ = nullptr;
    }

    // TODO 3: 实现移动赋值运算符 (Move Assignment Operator)
    // 提示：先关掉自己现有的 file_ptr_，再抢 over 的，最后将 other.file_ptr_ 置为 nullptr
    FileWrapper& operator=(FileWrapper&& other) noexcept {
        if (this != &other) {
            if (file_ptr_ != nullptr){
                std::fclose(file_ptr_);
            }

            file_ptr_ = other.file_ptr_;
            other.file_ptr_ = nullptr ;
            // ...
        }
        return *this;
    }

    // 辅助方法：判断文件句柄是否有效
    bool is_valid() const {
        return file_ptr_ != nullptr;
    }
};

int main() {
    std::cout << "--- 1. 测试 RAII 自动释放 ---\n";
    {
        FileWrapper f1("test.txt", "w");
    } // f1 离开作用域，析构函数应自动关闭文件

    std::cout << "\n--- 2. 测试移动所有权 ---\n";
    FileWrapper f2("test2.txt", "w");
    
    // 转移所有权：f2 的句柄赋给 f3，f2 变为空
    FileWrapper f3 = std::move(f2); 

    std::cout << "f2 是否有效: " << (f2.is_valid() ? "是" : "否") << "\n";
    std::cout << "f3 是否有效: " << (f3.is_valid() ? "是" : "否") << "\n";

    return 0;
}