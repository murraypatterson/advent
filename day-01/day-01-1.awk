BEGIN {c = 0; p = -1} {if(p>=0) {if(($1-p)>=0) { c+= 1 }} ; p = $1} END {printf "%s\n", c}
