docker:
	sudo service docker start
	sudo docker build -t sympy_antlr .
	sudo docker run -it --rm sympy_antlr /bin/bash

