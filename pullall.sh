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

	if [ -d "$targetpath/$file" ] && [ -d "$targetpath/$file/.git" ]
	then
		echo git pull $targetpath/$file
		cd "$targetpath/$file"
		git pull
		cd "$targetpath"
	elif [ -d "$targetpath/$file" ]
	then
		cfilelist=$(ls $targetpath/$file)
		for cfile in $cfilelist
		do
			if [ -d "$targetpath/$file/$cfile" ] && [ -d "$targetpath/$file/$cfile/.git" ]
			then
				echo git pull $targetpath/$file
				cd "$targetpath/$file/$cfile"
				git pull
				cd "$targetpath"
			fi
		done
	fi
done
