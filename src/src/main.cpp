#include <iostream>

#include "Foo.hpp"
#include <csignal>
#include <semaphore>
#include <stop_token>
#include <thread>

std::binary_semaphore semaphore{0};

int main() {
  std::signal(SIGTERM, [](int) { semaphore.release(); });
  std::signal(SIGINT, [](int) { semaphore.release(); });
  while (!semaphore.try_acquire()) {
    // sanitizer test
    auto i = new int{};
    std::cout << "Address: " << i << std::endl;
  }
  return 0;
}