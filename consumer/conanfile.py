from conans import ConanFile, CMake

class Consumer(ConanFile):
    name = "BoostExampleConsumer"
    version = "0.1"
    requires = "BoostExample/1.1@demo/testing"

    def _configure_cmake(self):
        cmake = CMake(self, generator='Ninja')
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()