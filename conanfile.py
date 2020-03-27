from conans import ConanFile, CMake, python_requires


base = python_requires("conan-shared/0.1@demo/testing")

class BoostExampleConan(base.Base):
    name = "BoostExample"
    version = "1.0.1"
    description = "Example of Conan Package - Boost"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    requires = "boost/[>=1.71.0]@conan/stable" # comma-separated list of requirements
    python_requires = "conan-shared/0.1@demo/testing"
    generators = "cmake"

    # How to append an option?
    default_options = {"boost:shared": True, "werror": True}

    scm = {
        "type": "git",
        "url": "https://github.com/antonindrawan/conan-example-boost.git",
        "revision": "master"
    }
