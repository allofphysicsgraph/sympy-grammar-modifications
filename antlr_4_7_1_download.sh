if [[ ! -f /usr/local/lib/antlr-4.7.1-complete.jar ]];
then
	curl -O https://www.antlr.org/download/antlr-4.7.1-complete.jar
fi
sudo cp antlr-4.7.1-complete.jar /usr/local/lib/
