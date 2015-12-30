#!/usr/bin/env bash

while getopts 'd:' OPT; do
    case $OPT in
        d)
            arg_d="$OPTARG";;
        ?)
            echo 'incorrect usage'
            exit 2;;
    esac
done

echo "$arg_d"
echo "$#"
echo "$0 $1 $2"

