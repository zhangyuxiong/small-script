#
# @Author: zhangyuxiong 
# @Date: 2017-06-25 17:04:54 
# @Last Modified by:   zhangyuxiong 
# @Last Modified time: 2017-06-25 17:04:54 
#
targetpath=./
if [ $1 ] ;then
	targetpath=$1
fi
echo git pull all $targetpath
filelist=$(ls $targetpath)
for file in $filelist
do

	if [ -d "$targetpath/$file" ]
	then
		echo git pull $targetpath/$file
		cd "$targetpath/$file"
		git pull
		cd ..
	fi
done
