% swipl -s test.pl -g "results_to_file(path(start,end,Vs))." -t halt. | wc -l

%     start
%     /   \
% c--A-----b--d
%     \   /
%      end

% start-A
% start-b
% A-c
% A-b
% b-d
% A-end
% b-end

is_big(uA). % large caves

edge(start,uA).
edge(start,b).
edge(uA,c). edge(c,uA).
edge(uA,b). edge(b,uA).
edge(b,d). edge(d,b).
edge(uA,end).
edge(b,end).

mib(U,Vs) :- % test membership, ignoring large caves
  not(is_big(U)),
  member(U,Vs).

% adapted from https://stackoverflow.com/questions/47022203/counting-number-of-paths-between-two-nodes-in-prolog-program

path(U,V,L) :- path(U,V,L,[U]). % entry point

path(U,V,[U,V],L) :- % base
  \+ mib(V,L),
  edge(U,V).

path(U,V,[U|Us],L) :- % recursive
  edge(U,W),
  \+ mib(W,L),
  path(W,V,Us,[W|L]).

% https://stackoverflow.com/questions/48227836/how-to-output-all-solutions-for-goal-from-non-interactive-script

results_to_file(Goal) :- forall((call(Goal)), (write(Goal), nl)).
