CC = g++ -std=c++03
CFLAGS = -Wall 
all : main.exe 
SRC = ./source
INC = ./header
main.exe : $(SRC)/main.cpp $(SRC)/BaseVector.cpp $(INC)/*.hpp
	$(CC) $(CFLAGS) -o main.exe $^
clean:
	rm main.exe 
	rm a.out