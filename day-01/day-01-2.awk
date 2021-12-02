BEGIN {c = 0; p1 = -1; p2 = -1; p3 = -1} {if(p3>=0) {if(($1-p3)>0) { c += 1 }} ; p3 = p2; p2 = p1; p1 = $1} END {printf "%s\n", c}
