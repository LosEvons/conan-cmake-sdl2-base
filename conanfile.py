from conan import ConanFile

class GameRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    
    def requirements(self):
        self.requires("sdl/2.26.1")
        self.requires("sdl_image/2.0.5")
        self.requires("sdl_ttf/2.20.1") 