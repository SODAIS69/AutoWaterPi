#!/bin/bash
# Program:
#       AutoWaterPi 移除
# History:
# 2021/12/2	

#取得現在的路徑
#https://www.ltsplus.com/linux/shell-script-get-script-location
get_script_dir () {
     SOURCE="${BASH_SOURCE[0]}"
     # While $SOURCE is a symlink, resolve it
     while [ -h "$SOURCE" ]; do
          DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
          SOURCE="$( readlink "$SOURCE" )"
          # If $SOURCE was a relative symlink (so no "/" as prefix, need to resolve it relative to the symlink base directory
          [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
     done
     DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
     echo "$DIR"
}

BASEDIR=$(get_script_dir)

crontab -u $USER -l | grep -v $BASEDIR/capture.py  | crontab -u $USER -
crontab -u $USER -l | grep -v $BASEDIR/check.py  | crontab -u $USER -
#https://askubuntu.com/questions/408611/how-to-remove-or-delete-single-cron-job-using-linux-command