import psutil

print(f"{'Image Name':<30} {'PID':<10}")
print('-' * 40)

for proc in psutil.process_iter(['name', 'pid']):
    try:
        process_name = proc.info['name']
        process_pid = proc.info['pid']
        print(f"{process_name:<30} {process_pid:<10}")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue
