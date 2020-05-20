help:
	@echo "make docker"
	@echo "         for linux"
	@echo "  "
	@echo "make docmac"
	@echo "         for Mac"

docker:
	sudo service docker start
	sudo docker build -t sympy_antlr .
	sudo docker run -it --rm sympy_antlr /bin/bash

docmac:
	docker build -t sympy_antlr .
	docker run -it --rm sympy_antlr /bin/bash

