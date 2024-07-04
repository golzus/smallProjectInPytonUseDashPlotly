# test_main.py

import subprocess

def test_app():
    # הרצת האפליקציה ב-subprocess
    process = subprocess.Popen(['python', 'anothergraph.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        # המתנה לזמן קצר לראות אם יש שגיאות
        stdout, stderr = process.communicate(timeout=10)

        if process.returncode != 0:
            print("App failed to start")
            print(stderr.decode())
            exit(1)
        else:
            print("App started successfully")

    except subprocess.TimeoutExpired:
        process.kill()
        print("App started successfully (timeout reached)")

if __name__ == "__main__":
    test_app()
