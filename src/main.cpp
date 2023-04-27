#include <SDL2/SDL.h>
#include <iostream>

int main(int argc, char *argv[]){
	SDL_Init(SDL_INIT_EVERYTHING);
	std::cout << "Test" << std::endl;
	SDL_Quit();
	return 0;
}
