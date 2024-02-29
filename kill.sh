#!/bin/bash
# 获取进程ID
pid=$(ps -ef | grep 'drink_reminder.py' | grep -v grep | awk '{print $2}')
if [ -z "$pid" ]; then
    echo "No process found"
else
    # 杀死进程
    kill $pid
    echo "Process $pid has been terminated"
fi

