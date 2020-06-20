if [[ ! -f amsath.zip ]];
then
	wget http://mirrors.ctan.org/macros/latex/required/amsmath.zip
fi
if [[ ! -d amsmath ]];
then
	unzip amsmath.zip
fi
