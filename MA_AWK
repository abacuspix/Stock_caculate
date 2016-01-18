BEGIN {FS=","; print "*"}
         {DATE[NR]=$1; OPEN[NR]=$2; HIGH[NR]=$3; LOW[NR]=$4; CLOSE[NR]=$5; VOL[NR]=$6; MOUNT[NR]=$7
# print $5
         }
#############Function Area######################
function closeAver(data, MA ,temp, aver) {
        for (i = NR-MA+1; i<=NR; i++) {
        temp+=CLOSE[i]
        }
        aver=temp/MA;
        print temp "----" aver
        return temp aver;
}
function highMax(max, MA, temp ) {
        temp=0;
        for (i=j-MA+1; i <= NR; i++) {
        if (HIGH[i]>temp)
             temp=HIGH[i];
        }
     print "---------------" temp
     return temp
 }
function lowMin(min, MA, temp ) {
        temp=LOW[NR];
        for (i=j-MA+1; i <= NR; i++) {
                if (LOW[i]<temp)
                temp=LOW[i];
        }
        print "---------------" temp
        return temp
}
#######################################################################################
END {
for (j=12; j <= NR; j++) {
        sum1=0; #for the MA10
        sum2=0; #for the MA20
        sum3=0; #for the MA60
        sum4=0; #for the VOL5
        sum5=0; #for the VOL10
        sum6=0; #for the VOL60
############## For the MA system#######################################################
        for (x=j-13; x <= j; x++) {
                sum1+=CLOSE[x];
                sum4+=VOL[x]
        }
        aver1= sum1/13;
        vol13= sum4/13
        for (x=j-21; x <= j; x++) {
                sum2+=CLOSE[x];
                sum5+=VOL[x]
        }
        aver2 = sum2/21;
        vol34 = sum5/21;
        for (x=j-55; x <= j; x++) {
                sum3+=CLOSE[x];
                sum6+=VOL[x]
        }
        aver3 = sum3/55;
        vol55 = sum6/55;
####################################################
        #print "sum1 is :" sum1 ;
        #print "MA10 is :" aver1 ;
        #closeAver(CLOSE[j],13)
        #print "sum2 is :" sum2 ;
        #print "sum3 is :" sum3 ;
        #print "MA20 is :" aver2 ;
        #print "MA60 is :" aver3 ;
############# FOR the analyze system#################
        a1=CLOSE[j];
        a2=CLOSE[j+13];
        b1=OPEN[j];
        v1=VOL[j]
        if ( aver1=aver3 && a1<a2 && b1>a1 && v1<vol34) {
        # print "present:" CLOSE[j];
        # print "DATE-------------------------->>" DATE[j]
         present=CLOSE[j]
        c=j+20;
       # print "<<<<<<--------------->>>>>>" j c
        # print "Ater :" CLOSE[c];
         after=CLOSE[c]
         increase = (after-present)/present*100;
         if (increase>0 && j>NR-5 )
         {print "You can play with it:" DATE[1] >> "stockpool"
         print "BEST pointer:" DATE[j]>> "stockpool" }
        # print "increase:" increase;
       if (after>present)
         { counter++;}
        total++;
   }
}
  stock= DATE[1]
  print "the stock number:"DATE[1] >> "report"
  print "total times:" total >> "report";
  print "Success counter:" counter >> "report"; ;
  print "Succecess rate is :" counter/total*100 "%" >> "report";
}
