#cp sdf input.sdf
#/home/opt/Fragmentor2019/lnx64/Fragmentor_lnx64 -i input.sdf \
#-t $t -l $l -u $u
#cp input.svm RESULT
#cp sdf RESULT
md5sum  /home/opt/Fragmentor2019/data/BCF_std_train.sdf
md5sum  sdf
#diff /home/opt/Fragmentor2019/data/BCF_std_train.sdf sdf > RESULT