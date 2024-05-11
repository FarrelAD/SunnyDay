#!/bin/sh

# TITLE: TWICE AS OLD
# TASK: Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old)
# SOURCE: https://www.codewars.com/kata/5b853229cfde412a470000d0
# 11 May 2024


dad_years_old=$1
son_years_old=$2

# implement me
dad_old_twice_son_old=$(expr $dad_years_old - $(expr 2 \* $son_years_old))

if [ $dad_old_twice_son_old -lt 0 ]; then
    echo $(expr $dad_old_twice_son_old \* -1)
else
    echo $dad_old_twice_son_old
fi

exit