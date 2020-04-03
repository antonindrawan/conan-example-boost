from conans import ConanFile, python_requires

class BoostExampleConan(ConanFile):
    name = "BoostExample"
    version = "1.2"
    description = "Example of Conan Package - Boost"

    # New way of python_requires
    python_requires = "conan-shared/0.2@demo/testing"
    python_requires_extend = "conan-shared.Base"

    requires = "boost/[>=1.71.0]@conan/stable" # comma-separated list of requirements

    # Additional default_options
    default_options = {"*:shared": True}

    scm = {
        "type": "git",
        "url": "https://github.com/antonindrawan/conan-example-boost.git",
        "revision": "master"
    }

    # Use the new method init() to append default options (since conan 1.24)
    # (https://github.com/conan-io/conan/pull/6614)
    def init(self):
        base = self.python_requires["conan-shared"].module.Base

        # Extend default options
        self.default_options.update(base.default_options)
        self.output.info("Default options: " + str(self.default_options))
