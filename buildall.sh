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
	#echo $targetpath/$file
	if [ -a "$targetpath/$file/gradlew" ]
	then
		echo sh gradlew build $targetpath/$file
		cd $targetpath/$file
		sh gradlew build
		cd "$targetpath"
	elif [ -a "$targetpath/$file/package.json" ] && [ -a "$targetpath/$file/gulpfile.js" ]
	then
		echo npm install & gulp $targetpath/$file
		cd $targetpath/$file
		npm install
		gulp
		cd "$targetpath"
	elif [ `ls -1 $targetpath/$file/*.sln 2>/dev/null | wc -l`!=0 ]
	then 
		echo npm install & gulp $targetpath/$file
		slnfilelist=$(ls $targetpath/$file/*.sln)
		for slnfile in $slnfilelist
		do
			xbuild $slnfile
		done
	fi
done
