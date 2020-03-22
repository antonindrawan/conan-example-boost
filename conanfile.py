from conans import ConanFile, CMake, tools

class BoostExampleConan(ConanFile):
    name = "BoostExample"
    version = "1.0.1"
    description = "Example of Conan Package - Boost"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    requires = "boost/[>=1.71.0]@conan/stable" # comma-separated list of requirements
    generators = "cmake"
    default_options = {"boost:shared": True}

    scm = {
        "type": "git",
        "url": "https://github.com/antonindrawan/conan-example-boost.git",
        "revision": "master"
    }

    def _configure_cmake(self):
        cmake = CMake(self, generator='Ninja')

        if self.develop:
            self.output.info("[develop mode], enabling warnings-as-errors")
            cmake.definitions["CMAKE_C_FLAGS"]="-Werror"
            cmake.definitions["CMAKE_CXX_FLAGS"]="-Werror"
        else:
            self.output.info("[consumer mode], not enabling warnings-as-errors explicitly")

        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()