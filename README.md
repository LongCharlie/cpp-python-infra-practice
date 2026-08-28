帮你写好了！你可以直接将以下内容复制到仓库根目录的 **`README.md`** 文件中。

---

# C++ & Python AI Infra 基础实战练习

本项目包含一系列针对 **AI 基础设施（AI Infra）** 核心技能的实战练习题，涵盖 Python 高级特性、多线程/多进程并发、C++17/20 现代特性、CMake 构建系统以及 Python/C++ 跨语言数据传递（零拷贝）等核心主题。

---

## 📁 目录结构与题目索引

| 序号 | 目录 / 模块 | 核心技术标签 | 简介 |
| --- | --- | --- | --- |
| **01** | [`01_python_copy/`](https://www.google.com/search?q=./01_python_copy/) | `Python` `内存模型` | 复现浅拷贝共享内层列表引发的数据污染，并给出重构与深拷贝修复方案。 |
| **02** | [`02_python_decorator/`](https://www.google.com/search?q=./02_python_decorator/) | `Python` `装饰器` | 实现带参数的 `@retry(max_attempts=3)` 装饰器，仅捕获指定异常类型。 |
| **03** | [`03_concurrency_benchmark/`](https://www.google.com/search?q=./03_concurrency_benchmark/) | `并发` `ThreadPool` `ProcessPool` | 针对 I/O 密集型与 CPU 密集型任务，对比线程池与进程池的耗时差异。 |
| **04** | [`04_cprofile_analysis/`](https://www.google.com/search?q=./04_cprofile_analysis/) | `性能调优` `cProfile` | 使用 `cProfile` 识别 Python 瓶颈函数，进行算法优化并对比测量收益。 |
| **05** | [`05_cpp_raii_file/`](https://www.google.com/search?q=./05_cpp_raii_file/) | `C++` `RAII` `移动语义` | 实现持有文件句柄的 RAII 类，禁用拷贝构造/赋值，支持移动构造/赋值。 |
| **06** | [`06_sanitizer_heap_overflow/`](https://www.google.com/search?q=./06_sanitizer_heap_overflow/) | `C++` `ASan` `内存安全` | 故意制造堆内存越界，对比普通运行崩溃与 AddressSanitizer 的详细报错。 |
| **07** | [`07_cmake_library_target/`](https://www.google.com/search?q=./07_cmake_library_target/) | `CMake` `模块化构建` | 将 C++ 库拆分为头文件、源文件与可执行文件，使用 Target-based CMake 构建。 |
| **08** | [`08_binary_inspection/`](https://www.google.com/search?q=./08_binary_inspection/) | `ABI` `ldd` `nm` | 利用 `ldd`/`otool` 与 `nm -C` 分析 Python 原生扩展（`.so`）的依赖与导出符号。 |
| **09** | [`09_pytorch_env_verification/`](https://www.google.com/search?q=./09_pytorch_env_verification/) | `PyTorch` `CUDA` `环境隔离` | 在干净虚拟环境中验证 Python 解释器路径、PyTorch 版本、CUDA 版本与 GPU 可见性。 |
| **10** | [`10_numpy_c_extension_zero_copy/`](https://www.google.com/search?q=./10_numpy_c_extension_zero_copy/) | `C++` `pybind11` `零拷贝` | 接收 NumPy 数组，校验 Dtype 与连续性，比较内存复制版与共享缓冲区（零拷贝）版的耗时。 |

---

## 🛠️ 环境要求

* **Python**: 3.8+
* **C++ 编译器**: GCC 9+ / Clang 10+ / MSVC (支持 C++17 及以上)
* **CMake**: 3.14+
* **深度学习基础**: PyTorch, NumPy, pybind11 (题 09 & 10)

---

## 🚀 快速开始

### 1. 克隆本仓库

```bash
git clone https://github.com/YOUR_USERNAME/cpp-python-infra-practice.git
cd cpp-python-infra-practice

```

### 2. 运行单个练习（以 01 为例）

```bash
cd 01_python_copy
python main.py

```

### 3. CMake 项目构建（以 07 为例）

```bash
cd 07_cmake_library_target
cmake -S . -B build
cmake --build build
./build/main  # Windows 下运行 .\build\Debug\main.exe

```

---

针对每道题目的具体实现说明与踩坑记录，可以点进对应的子目录查看独立文档。