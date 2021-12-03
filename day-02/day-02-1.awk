BEGIN {h = 0; d = 0} {if($1=="forward") {h += $2} ; if($1=="down") {d += $2} ; if($1=="up") {d -= $2}} END {print h * d}
