from conans import ConanFile, CMake


class TemplateConan(ConanFile):
    name = 'Template'
    version = '0.0.1'
    settings = "os", "compiler", "build_type", "arch"
    requires = [
        "benchmark/[>=1.6.0]",
        "gtest/[>=1.8.1]"
    ]
    generators = "cmake", "cmake_find_package"
    default_options = {}
    exports_sources = [
        "conanfile.py",
        "CMakeLists.txt",
        "lib/*",
        "src/*",
        ]

    def configure_cmake(self):
        """Create CMake instance and execute configure step
        """
        cmake = CMake(self)
        cmake.configure(source_folder='.', build_folder='build/')
        return cmake

    def build(self):
        """Configure, build and install FlatBuffers using CMake.
        """
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def deploy(self):
        self.copy("*", src="bin", dst="/usr/bin")
        self.copy("*.so", src="lib", dst="/usr/lib")
