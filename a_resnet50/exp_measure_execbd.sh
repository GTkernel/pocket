#!/bin/bash

bash exp_script.sh measure-exec -n=1 --policy=1 2>&1 | grep 'total_time\|be_time\|fe_time\|fe_ratio\|>>>>>>>'
bash exp_script.sh measure-exec -n=1 --policy=3 2>&1 | grep 'total_time\|be_time\|fe_time\|fe_ratio\|>>>>>>>'
bash exp_script.sh measure-exec -n=1 --policy=4 2>&1 | grep 'total_time\|be_time\|fe_time\|fe_ratio\|>>>>>>>'