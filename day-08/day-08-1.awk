BEGIN {split("2 3 4 7", t); {for(i in t) a[t[i]]}} {for(i=12;i<=NF;i++) {if(length($i) in a) {c+=1}}} END {print c}
