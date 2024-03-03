#!/bin/bash

# 获取uWSGI进程的PID
PID=$(ps aux | grep '[u]wsgi --http 0.0.0.0:5511' | awk '{print $2}')

# 如果PID不为空, 则杀死该进程
if [ ! -z "$PID" ]; then
    kill -9 $PID
    echo "Killed uWSGI process with PID: $PID"
else
    echo "No uWSGI process found."
fi