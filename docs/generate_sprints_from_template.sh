#!/bin/bash

END=14
for ((i=8;i<=END;i++)); do
    mkdir -p "sprints/sprint$i/img"
    cp -a "sprints/template/." "sprints/sprint$i/"
    echo $i
done