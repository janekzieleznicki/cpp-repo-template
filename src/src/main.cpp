#include <iostream>

#include "Foo.hpp"

int main() {
  std::cout << "Hello, World! Foo: " << foo::Foo{} << std::endl;
  return 0;
}