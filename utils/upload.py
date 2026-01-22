import subprocess
import sys
import os

def upload_file(port, file_path):
    try:
        result = subprocess.run(
            ['ampy', '--port', port, 'put', file_path, '/main.py'],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✅ Successfully uploaded {file_path} to ESP32")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error uploading: {e.stderr}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python upload.py <PORT> <FILE_PATH>")
        print("Example: python upload.py /dev/cu.usbserial-0001 step1_led_blink/main.py")
        sys.exit(1)
    
    port = sys.argv[1]
    file_path = sys.argv[2]
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(1)
    
    upload_file(port, file_path)

