#! /bin/bash
# Given two integers,  and , identify whether  or  or .
# Exactly one of the following lines:
# - X is less than Y
# - X is greater than Y
# - X is equal to Y

read a 
read b 
if [[ $a == $b ]] 
then 
    echo "X is equal to Y"
    
elif [[ $a > $b ]]
then
    echo "X is greater than Y"
    
else 
    echo "X is less than Y"

fi
