antlr:

	sudo apt install curl -y
	sudo apt install default-jdk
	curl -O https://www.antlr.org/download/antlr-4.8-complete.jar
	sudo mv antlr-4.8-complete.jar /usr/local/lib/
	sudo apt install virtualenv
	/bin/bash install.sh
run:
	/bin/bash run.sh

tests:
	find test_expressions -type f -exec rm {} \;
	/bin/bash generate_files_from_expressions.sh 
	/bin/bash run_tests.sh
pass_fail_counts:
	echo failed
	ls test_expressions|wc -l
	echo passed
	ls test_expressions/passed|wc -l
