from conans import ConanFile, CMake

class PocoTimerConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = [
       "benchmark/[>=1.6.0]",
       "gtest/[>=1.8.1]"
   ]
   generators = "cmake", "gcc", "txt", "cmake_find_package"
   default_options = {
       
   }