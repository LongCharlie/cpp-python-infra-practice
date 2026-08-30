import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 1. IO 密集型任务：模拟休眠 0.5 秒
def io_task() -> None:
    time.sleep(0.5)

# 2. CPU 密集型任务：计算 1000 万次平方和
def cpu_task() -> int:
    return sum(i * i for i in range(10_000_000))

# 3. 通用基准测试函数
def run_benchmark(pool_cls, task_func, tasks_count: int = 8, max_workers: int = 4) -> float:
    start_time = time.perf_counter()
    
    # TODO: 使用 with 语句创建 pool_cls(max_workers=max_workers)
    # 并使用 submit 或 map 并行提交 tasks_count 次 task_func 任务
    # 提示：需要等待所有任务执行完毕（例如拉取 future.result() 或 list(map)）

    with pool_cls(max_workers = max_workers) as executor:

        futures = [executor.submit(task_func) for _ in range(tasks_count)]
        
        for future in futures:
            future.result()
    
    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    # ⚠️ 踩坑提示：Windows 上使用 ProcessPoolExecutor 必须在 if __name__ == "__main__": 保护下运行！
    WORKERS = 4                
    TASKS = 8

    print("=== 1. 测试 IO 密集型任务 (8次 sleep(0.5)) ===")
    thread_io_time = run_benchmark(ThreadPoolExecutor, io_task, tasks_count=TASKS, max_workers=WORKERS)
    process_io_time = run_benchmark(ProcessPoolExecutor, io_task, tasks_count=TASKS, max_workers=WORKERS)
    print(f"线程池 (ThreadPoolExecutor)  耗时: {thread_io_time:.4f} 秒")
    print(f"进程池 (ProcessPoolExecutor) 耗时: {process_io_time:.4f} 秒")

    print("\n=== 2. 测试 CPU 密集型任务 (8次 1000万次计算) ===")
    thread_cpu_time = run_benchmark(ThreadPoolExecutor, cpu_task, tasks_count=TASKS, max_workers=WORKERS)
    process_cpu_time = run_benchmark(ProcessPoolExecutor, cpu_task, tasks_count=TASKS, max_workers=WORKERS)
    print(f"线程池 (ThreadPoolExecutor)  耗时: {thread_cpu_time:.4f} 秒")
    print(f"进程池 (ProcessPoolExecutor) 耗时: {process_cpu_time:.4f} 秒")