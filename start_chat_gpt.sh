#!/bin/bash

. .venv/bin/activate

# 获取当前日期和时间
NOW=$(date +"%Y-%m-%d-%H-%M")

# 指定log文件的路径
LOGFILE="./log/$NOW.log"

# 启动uWSGI服务器
uwsgi --http 0.0.0.0:5511 --master -p 1 --threads 5 -w app:app --daemonize $LOGFILE
# 看看log到哪儿
echo $LOGFILE

# 打印日志
tail -f $LOGFILE
