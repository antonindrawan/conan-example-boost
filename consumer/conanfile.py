from conans import ConanFile, CMake

class Consumer(ConanFile):
    name = "BoostExampleConsumer"
    version = "0.1"
    requires = "BoostExample/1.1@demo/testing"

    # If a package is created (using conan create), all imported files will be packaged if keep_imports is True.
    keep_imports = True

    def imports(self):
        self.copy("BoostExample*", src="bin", dst="bin")

    def package(self):
        self.copy("bin/*")