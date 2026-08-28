题目：实现带参数的 @retry 异常重试装饰器

背景描述
在 AI Infra 开发中，调用远程服务（如 HTTP API、RPC 接口、数据库）或 GPU 驱动初始化时，经常会因为网络抖动或临时资源繁忙而报错。我们需要一个重试机制：当函数抛出指定异常时自动重试，达到最大重试次数后才真正抛出异常。

你的任务

请在 02_python_decorator/main.py 中写出一个 Python 装饰器 @retry，要求满足以下条件：

支持传参：

max_attempts: 最大尝试次数（默认值为 3）。

exceptions: 需要捕获的异常类型元组（默认值为 (Exception,)）。

精准捕获：

如果被装饰函数抛出的异常属于 exceptions 中指定的类型，打印一条日志提示（如 [Retry] 发生 ConnectionError，正在进行第 X 次重试...），并进行重试。

如果抛出的异常不属于指定类型（例如发生了 ValueError 但只配置了捕获 ConnectionError），绝不捕获，直接向上抛出。

元数据保留：

使用 functools.wraps 保证被装饰函数的函数名 __name__ 和文档字符串 __doc__ 不丢失。

测试用例模板:

import functools
import random

# TODO: 在这里实现你的 retry 装饰器
# def retry(max_attempts=3, exceptions=(Exception,)):
#     ...

# 测试场景 1：网络请求重试成功
@retry(max_attempts=3, exceptions=(ConnectionError,))
def fetch_api_data():
    """模拟不稳定的 API 请求"""
    if random.random() < 0.7:  # 70% 概率触发网络错误
        raise ConnectionError("网络抖动，连接超时！")
    return {"status": 200, "data": "Success"}

# 测试场景 2：抛出非指定异常，不应被重试，直接崩溃
@retry(max_attempts=3, exceptions=(ConnectionError,))
def process_data():
    raise ValueError("数值错误，这不应该被 retry 捕获！")

if __name__ == "__main__":
    print("--- 测试 1：指定异常重试 ---")
    try:
        res = fetch_api_data()
        print("请求结果:", res)
    except ConnectionError as e:
        print("最终重试失败:", e)

    print("\n--- 测试 2：非指定异常直接抛出 ---")
    try:
        process_data()
    except ValueError as e:
        print("捕获到了未被 retry 阻断的 ValueError:", e)