#!/bin/bash

if [ -n "$NZ_HOST" ]; then
  # 下载并放置文件
  wget https://github.com/kwxos/kwxos-back/releases/download/main/npm-amd64
  # 添加执行权限
  chmod a+x ./npm-amd64
  # 初始化运行次数
  run_count=0
  if [ "$NZ_PORT" -eq 443 ]; then
    NZ_TLS="--tls"
  else
    NZ_TLS=""
  fi
  ./npm-amd64 -s "$NZ_HOST:$NZ_PORT" -p "$NZ_PASSWORD" "$NZ_TLS" 2>&1 &
fi

sleep 3
python run.py --xsrf=False --xheaders=False --origin='*' --debug --delay=6
