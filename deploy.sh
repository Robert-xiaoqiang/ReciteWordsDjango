#! /usr/bin/bash

git checkout master
git add .
git commit -m "hook merge"
git pull origin master:master
cd ReciteWords
python3 fuck.py
cp static/html/recite_words.html /home/appveyor/WebAPP/ReciteWords/index.html
