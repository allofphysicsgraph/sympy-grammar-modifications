cd /opt/sympy/sympy/parsing/latex/
CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"
java -jar /usr/local/lib/antlr-4.7.1-complete.jar LaTeX.g4 -no-visitor -no-listener -o _antlr
sleep 3
python3 rename.py        
cd ..
cd ..
cd ..
python3 setup.py install
cd /opt/
python3 generate_latex_files.py
