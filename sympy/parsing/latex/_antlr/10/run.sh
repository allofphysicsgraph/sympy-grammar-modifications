cd ../
export CLASSPATH=".:/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH"
antlr4='java -jar /usr/local/lib/antlr-4.8-complete.jar'
grun='java org.antlr.v4.gui.TestRig'
$antlr4 LaTeX.g4 -visitor -Dlanguage=Python3

