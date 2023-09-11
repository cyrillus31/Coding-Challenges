#! /bin/bash
#
#Your task is to use for loops to display only odd natural numbers from 1 to 99.

# for number in {1..99}
  # do
  # 	if [ $(($number % 2)) != 0 ]
  #     then
  # 	  echo $number
  #     else true
  #     fi
  # done


for number in {1..99..2}
  do
      echo $number
  done
