#!/bin/bash

python3 to_prolog.py "$1" | cat - <(tail -20 test.pl) > run.pl
swipl -s run.pl -g "results_to_file(path(start,end,Vs))." -t halt. | wc -l
rm run.pl

# part 2
for f in run_*.pl ; do
    tail -20 test.pl >> $f
    swipl -s $f -g "results_to_file(path(start,end,Vs))." -t halt.
    rm $f
done | sed 's/prime//g' | sort | uniq | wc -l
