while read f;
do
echo  "$f"
echo
echo "$f"|python LaTeX.py
echo
echo
done <test_input
