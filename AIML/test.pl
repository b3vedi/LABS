female(vimla).
female(deepa).
female(krishna).
female(nani).
male(bhuvanesh).
male(lilesh).
male(chunilal).
male(mithalal).

parent(lilesh,bhuvanesh).
parent(lilesh,krishna).
parent(deepa,bhuvanesh).
parent(deepa,krishna).
parent(chunilal,lilesh).
parent(vimla,lilesh).
parent(mithalal,deepa).
parent(nani,deepa).

mother(X,Y):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).
haschild(X):- parent(X,_).
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
paternalGrandfather(X,Y) :- parent(X,Z),parent(Z,Y),male(X),male(Z),X\==Y.
paternalGrandmother(X,Y) :- parent(X,Z),parent(Z,Y),female(X),male(Z),X\==Y.
maternalGrandfather(X,Y) :- parent(X,Z),parent(Z,Y),male(X),female(Z),X\==Y.
maternalGrandmother(X,Y) :- parent(X,Z),parent(Z,Y),female(X),female(Z),X\==Y.