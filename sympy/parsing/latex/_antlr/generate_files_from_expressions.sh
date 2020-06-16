while read f;do 
	echo $f > test_file;
	dst="$(md5sum test_file|cut -d ' ' -f1)";
	mv test_file test_expressions/"$dst" ;
done < <(cat test_input)

