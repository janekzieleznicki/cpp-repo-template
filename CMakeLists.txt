cmake_minimum_required(VERSION 3.5)
project(FormatOutput CXX)

# Add project_options v0.14.2
# https://github.com/cpp-best-practices/project_options
include(FetchContent)
FetchContent_Declare(_project_options URL https://github.com/cpp-best-practices/project_options/archive/refs/tags/v0.14.2.zip)
FetchContent_MakeAvailable(_project_options)
include(${_project_options_SOURCE_DIR}/Index.cmake)

if(CONAN_EXPORTED)
     project_options(
          ENABLE_IPO
     )
     include(conanbuildinfo.cmake)
     conan_basic_setup()
else()
     project_options(
      ENABLE_CACHE
      ENABLE_CPPCHECK
      ENABLE_CLANG_TIDY
      ENABLE_CONAN
      ENABLE_IPO
      # ENABLE_DOXYGEN
      # ENABLE_COVERAGE
      WARNINGS_AS_ERRORS
      ENABLE_SANITIZER_ADDRESS
      ENABLE_SANITIZER_LEAK
      ENABLE_SANITIZER_UNDEFINED_BEHAVIOR
      # ENABLE_SANITIZER_THREAD
      # ENABLE_SANITIZER_MEMORY
      # ENABLE_INCLUDE_WHAT_YOU_USE
      # ENABLE_USER_LINKER
      # ENABLE_BUILD_WITH_TIME_TRACE
      # ENABLE_UNITY
      # CONAN_OPTIONS
     )
endif()

target_compile_features(project_options INTERFACE cxx_std_20)

include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-march=native" COMPILER_SUPPORTS_MARCH_NATIVE)
if(COMPILER_SUPPORTS_MARCH_NATIVE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native")
endif()

add_subdirectory(lib)
add_subdirectory(src)