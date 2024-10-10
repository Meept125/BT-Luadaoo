import psutil
import sys

def terminate_process(identifier):
    # duyệt qua các process đang chạy và lấy thông tin
    for proc in psutil.process_iter(['pid', 'name']):
        if str(proc.info['pid']) == identifier or proc.info['name'] == identifier:
            proc.terminate()  # hoặc sử dụng proc.kill() nếu cần kết thúc ngay lập tức
            print(f"Terminated process: {proc.info['name']} (PID: {proc.info['pid']})")
            return
    print(f"No process found with identifier: {identifier}")

if __name__ == "__main__":
    # kiểm tra nếu script đang được chạy tiếp <không phải được nhập từ 1 module khác>
    if len(sys.argv) != 3 or sys.argv[1] not in ['pid', 'name']:
        # kiểm tra số lượng tham số
        print("Usage: python taskkill.py [pid|name] [value]")
        sys.exit(1)

    terminate_process(sys.argv[2]) 
    # truyền vào giá trị thứ 2 từ tham số dòng lệnh <PID hoặc tên process>
