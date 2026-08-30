import time

# 任务 A：低效的字符串拼接操作
def slow_string_concat(n=100_000):
    result = ""
    for i in range(n):
        result += str(i) # 字符串不可变，每次 += 都重新分配内存
    return len(result)

# 任务 B：密集数学计算
def heavy_math(n=2_000_000):
    m = n-1
    return m*(m+1)*(2*m+1) // 6

# 任务 C：模拟 IO 阻塞
def simulate_io():
    time.sleep(0.3)

def main():
    print("开始执行任务...")
    slow_string_concat()
    heavy_math()
    simulate_io()
    print("任务执行完毕！")

if __name__ == "__main__":
    main()