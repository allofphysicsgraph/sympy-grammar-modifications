while read f;
	do echo $f;
	grep -c -P "expecting|missing" <<< $(python LaTeX.py "$f");
	done < <(find test_expressions -type f )
