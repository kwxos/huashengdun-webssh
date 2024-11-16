from webssh.main import main
import subprocess

def make_executable_and_run(script_path):
    try:
        # 赋予执行权限
        subprocess.run(['chmod', '+x', script_path], check=True)
        print(f"'{script_path}' is now executable.")
        
        # 执行脚本
        subprocess.run([script_path], check=True)
        print(f"'{script_path}' executed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == '__main__':
    make_executable_and_run('main.sh')  # 赋权并执行 main.sh
    main()
