
find_package(benchmark REQUIRED)

add_executable(${PROJECT_NAME}_bench benches.cpp)
target_link_libraries(${PROJECT_NAME}_bench PRIVATE StaticFoo benchmark::benchmark)