help:
	@echo "make docker"
	@echo "         for linux"
	@echo "  "
	@echo "make docmac"
	@echo "         for Mac"

docker:
	sudo service docker start
	#sudo docker build --no-cache -t sympy_antlr .
	sudo docker build  -t sympy_antlr .
	sudo docker run -it --rm sympy_antlr /bin/bash

docmac:
	docker build -t sympy_antlr .
	docker run -it --rm sympy_antlr /bin/bash

local:
	virtualenv /home/user/venv -p python3
	wget https://raw.githubusercontent.com/allofphysicsgraph/proofofconcept/gh-pages/v7_pickle_web_interface/flask/data.json
