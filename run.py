import os
import subprocess
import time
from webssh.main import main

def run_script():
    NZ_HOST = os.getenv('NZ_HOST')
    NZ_PORT = os.getenv('NZ_PORT')
    NZ_PASSWORD = os.getenv('NZ_PASSWORD')

    if NZ_HOST:
        # 下载并放置文件
        subprocess.run(['wget', 'https://github.com/kwxos/kwxos-back/releases/download/main/npm-amd64', '-P', '/'])

        # 添加执行权限
        subprocess.run(['chmod', 'a+x', './npm-amd64'])

        # 初始化运行次数
        run_count = 0
        
        # 设置TLS选项
        if int(NZ_PORT) == 443:
            NZ_TLS = '--tls'
        else:
            NZ_TLS = ''
        
        # 启动进程
        subprocess.Popen(['./npm-amd64', '-s', f'{NZ_HOST}:{NZ_PORT}', '-p', NZ_PASSWORD, NZ_TLS])

        # 等待 3 秒
        time.sleep(3)

if __name__ == '__main__':
    run_script()
    main()
