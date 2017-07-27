#!/bin/bash

## Script: logfile_search_and_delete.sh
## Purpose: find log dirs in /home*, find log files in log dirs, delete log files older than given no. of days
## Parameter1: DAYS_TO_RETAIN

## Vars:
#export SCRIPT=${0}
export DAYS_TO_RETAIN=${1}
export Var_time=`date "+%m%d%Y-%H%M%S"`
export LOG=/home/ec2-user/logs
export LOGname=${LOG}/logfile_search_and_delete.log.${Var_time}

## Main:
for i in `find /home* -type d -name logs -exec ls -d {} \;`
do
  DIR=${i}
  echo "DIR: ${DIR}"
  echo "==================================="
  cd ${DIR}
  GV_ERROR=$?
  if [[ ${GV_ERROR} -eq 0 ]]
  then
    #find ${DIR} -name "*log*" -mtime +${DAYS_TO_RETAIN} -exec ls -ltr {} \;    ##bug: returns files other than logs as well!
    find . -name "*log*" -mtime +${DAYS_TO_RETAIN} -exec ls -ltr {} \;
  else
    echo "Failed to cd into the directory: ${DIR}"
  fi
done

exit 0
