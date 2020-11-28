if [[ ! -f /usr/local/lib/antlr-4.7.1-complete.jar ]];
then
	cd /tmp/
	curl -O https://www.antlr.org/download/antlr-4.7.1-complete.jar 
	checksum="$(md5sum /tmp/antlr-4.7.1-complete.jar |grep -c 8084572679b2b2a1c126aa6e62e48ce5)"
	echo $checksum
	if [[ $checksum -eq 1 ]];
	then
		sudo rsync -axr /tmp/antlr-4.7.1-complete.jar /usr/local/lib/ --progress --remove-source-files;
	fi
fi
