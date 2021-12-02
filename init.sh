#!/bin/bash
# Program:
#       AutoWaterPi 初始化
# History:
# 2021/12/2	

#Check interval
minute=5
#Capture interval
cminte=1

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

mkdir -p $BASEDIR/Captured #建立Captured資料夾
(crontab -u root -l 2>/dev/null; echo "*/$cminte * * * * python3 $BASEDIR/capture.py") | crontab -u root - #每15分拍一次照
(crontab -u root -l 2>/dev/null; echo "*/$minute * * * * python3 $BASEDIR/check.py") | crontab -u root - #每X分檢查水位跟土壤濕度
apt-get install apache2 -y
mkdir /var/www/html/AutoWaterPi
ln -s $BASEDIR/Captured /var/www/html/AutoWaterPi
ip=$(hostname -I)
ip=${ip// /} #去除空白
RED='\033[0;91m'
NC='\033[0m' # No Color
echo -e "${RED}You can now check your captured pictures at \"http://${ip}/AutoWaterPi/Captured\"${NC}"
