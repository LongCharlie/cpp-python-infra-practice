from functools import wraps
import random
from collections.abc import Callable
from typing import ParamSpec,TypeVar

P = ParamSpec("P")
R = TypeVar("R")

def retry(max_attempts:int,exceptions:tuple[type[BaseException],...]=(Exception,)) -> Callable[[Callable[P,R]],Callable[P,R]]:
    def decorator(func:Callable[P,R]) -> Callable[P,R]:
        @wraps(func)
        def wrapper(*args: P.args,**kwargs: P.kwargs) -> R:
            for attempt in range(1,1+max_attempts):
                try:
                    return func(*args,**kwargs)
                except exceptions as error:
                    print(f"[RETRY]:Function {func.__name__}触发{type(error).__name__},正在进行第{attempt}次尝试")
                    if attempt == max_attempts:
                        raise 

            raise RuntimeError("Unexpected retry failure")
        return wrapper
    return decorator
  

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