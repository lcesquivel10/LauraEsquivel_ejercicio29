plot.png: Data.dat plot.py
	python plot.py

%.dat : a.out
	./a.out 

a.out: Ondas.cpp
	g++ Ondas.cpp
