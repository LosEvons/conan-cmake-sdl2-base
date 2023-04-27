#include "SDL2.h"

#include <iostream>

int main(int argc, char *argv[]){
	SDL_Init(SDL_INIT_EVERYTHING);
	std::cout << "Test" << std::endl;
	SDL_Quit();
	return 0;
}
