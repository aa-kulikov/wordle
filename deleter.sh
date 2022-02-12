#!/bin/bash
value=$(<english_words.txt)
grep -E '^.{6}$' english_words.txt > sing_en.txt
val=$(<sing_en.txt)
sed  '/^[[:space:]]*$/d' <<< "$val" &> sing_en.txt
