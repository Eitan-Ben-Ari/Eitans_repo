#!/bin/bash

for key in `ls Keitan.itlab.com*.key`
do
echo "\$INCLUDE $key">> db.Eitan.itlab.com
done