import psutil 
# psutil: sd để truy cập thông tin về các process

print(f"{'Image Name':<30} {'PID':<10}")
# tên process căn trái chiều rộng 30 kí tự , PID: 10 kí tự
print('-' * 40)

for proc in psutil.process_iter(['name', 'pid']):
    # try: đảm bảo chương trình k bị dừng nếu có process k tồn tại hoặc k thể truy cập
    try:
        process_name = proc.info['name']
        process_pid = proc.info['pid']
        print(f"{process_name:<30} {process_pid:<10}")
        # tiếp tục chương trình khi gặp process không hợp lệ
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue
