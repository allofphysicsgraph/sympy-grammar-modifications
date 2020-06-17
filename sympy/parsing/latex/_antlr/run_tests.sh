while read f;
	do echo $f;
		count="$(grep -c -P "recognition erro|expecting|missing" <<< $(python LaTeX.py "$f"))";
	if [[ $count -eq 0 ]];
	then
		echo $f
		mv "$f" test_expressions/passed/
	fi
	done < <(find test_expressions -type f )
