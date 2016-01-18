#the parser shell
#!/bin/bash
WorkingFolder=/home/stock
DataFolder="/home/stock/export"
Date=`date | nawk '{ print $6"_"$2"_"$3 }'`
rm report
for configList in `ls $DataFolder`
    do
        echo "Parsing the export/$configList"
        gawk -f ma.awk export/$configList >> temp_log_$Date
    done
echo "######### Feature List ##################" > summary_log_$Date
sort -u temp_log_$Date >> summary_log_$Date
echo "######### Hardware List ##################" >> summary_log_$Date
grep "Product Name" R17/* >> summary_log_$Date
rm temp_log_$Date
