# monitor.py
import psutil # 这是一个第三方库，需要安装
import time
import os

def log_system_info():
    print("--- 实验室系统监控启动 ---")
    # 确保日志文件夹存在
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    with open('logs/system_stats.txt', 'a') as f:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        log_str = f"{time.ctime()}: CPU {cpu}%, MEM {mem}%"
        f.write(log_str + '\n')
        print(f"记录成功: {log_str}")

if __name__ == "__main__":
    # 连续运行 5 次作为测试
    for _ in range(5):
        log_system_info()
        time.sleep(1)