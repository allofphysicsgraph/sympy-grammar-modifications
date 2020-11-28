echo -e export CLASSPATH=\".:/usr/local/lib/antlr-4.7.1-complete.jar:\$CLASSPATH\" >> ~/.bashrc
echo -e  alias antlr4=\'java -Xmx500M -cp \"/usr/local/lib/antlr-4.7.1-complete.jar:\$CLASSPATH\" org.antlr.v4.Tool\' >> ~/.bashrc
echo -e alias grun=\'java -Xmx500M -cp \"/usr/local/lib/antlr-4.7.1-complete.jar:\$CLASSPATH\" org.antlr.v4.gui.TestRig\'  >> ~/.bashrc

