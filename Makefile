help:
	@echo "make docker"
	@echo "         for linux"
	@echo "  "
	@echo "make docmac"
	@echo "         for Mac"



docker:
	/bin/bash scripts/amsmath.sh
	/bin/bash scripts/data_json.sh
	/bin/bash scripts/antlr_4_7_1_download.sh 
	sudo service docker start
	sudo docker build  -t sympy_antlr .
	sudo docker run -it --rm sympy_antlr /bin/bash

docmac:
	docker build -t sympy_antlr .
	docker run -it --rm sympy_antlr /bin/bash

