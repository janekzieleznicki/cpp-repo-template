#include <benchmark/benchmark.h>

#include "Foo.hpp"

static void BM_virtual(benchmark::State &state) {
  for (auto _ : state)
    (void)foo::Foo{};
}
BENCHMARK(BM_virtual);

BENCHMARK_MAIN();