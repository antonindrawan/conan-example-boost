from conans import ConanFile, CMake

class Consumer(ConanFile):
    requires = "BoostExample/1.0.1@demo/testing"

    def _configure_cmake(self):
        cmake = CMake(self, generator='Ninja')
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()