from conans import ConanFile
import os

class BoostExampleTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def imports(self):
        self.copy("BoostExample*", src="bin", dst="bin")

    def build(self):
        self.output.info("Placeholder for building a test package")

    def test(self):
        os.chdir("bin")
        self.output.info("test_package: test(). Path: " + os.getcwd())
        self.output.info("Does BoostExample exist? " + str(os.path.isfile("BoostExample")))