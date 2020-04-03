from conans import ConanFile, CMake

# conan export . demo/testing
class Base(ConanFile):
    name = "conan-shared"
    version = "0.2"
    license = "MIT"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    options = { "werror": [True, False] }
    default_options = {"werror": True}

    def _add_cmake_definitions(self, cmake):
        if self.develop:
            if self.options.werror:
                self.output.info("[develop mode], enabling warnings-as-errors")
                cmake.definitions["ENABLE_WERROR"] = "ON"
            else:
                self.output.info("[develop mode], explicitly disabling warnings-as-errors")
                cmake.definitions["ENABLE_WERROR"] = "OFF"
        else:
            self.output.info("[consumer mode], not enabling warnings-as-errors")
            cmake.definitions["ENABLE_WERROR"] = "OFF"

        return cmake

    def _configure_cmake(self):
        cmake = CMake(self, generator='Ninja')
        cmake = self._add_cmake_definitions(cmake)

        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
