/*
 * @Author: zhangyuxiong 
 * @Date: 2017-06-25 17:11:20 
 * @Last Modified by: zhangyuxiong
 * @Last Modified time: 2017-06-25 17:24:57
 */
targetpath=./
if [ $1 ] ;then
	targetpath=$1
fi
echo build all $targetpath
filelist=$(ls $targetpath)
for file in $filelist
do

	if [ -d "$targetpath/$file" ]
	then
		echo sh gradlew build $targetpath/$file
		cd $targetpath/$file
		sh gradlew build
		cd ..
	fi
done
