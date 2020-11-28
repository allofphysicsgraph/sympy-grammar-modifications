help:
	@echo "make docker"
	@echo "         for linux"
	@echo "  "
	@echo "make docmac"
	@echo "         for Mac"


debian_standalone:
	SHELL=/bin/bash
	#requires git, wget
	#edits bashrc with export classpath,#alias for (grun and antlr4)
	git submodule update --init
	/bin/bash scripts/amsmath.sh
	/bin/bash scripts/data_json.sh
	/bin/bash scripts/antlr_4_7_1_download.sh 
	pip3 download antlr4-python3-runtime==4.7.1 -d python_packages
	pip3 download mpmath -d python_packages
	@/bin/bash scripts/antlr4_updatebashrc.sh
	

docker:
	sudo service docker start
	sudo docker build  -t sympy_antlr .
	sudo docker run -it --rm sympy_antlr /bin/bash

docmac:
	docker build -t sympy_antlr .
	docker run -it --rm sympy_antlr /bin/bash

