
find_package(benchmark REQUIRED)
file(GLOB ${PROJECT_NAME}_BENCH_SOURCE_FILES ${CMAKE_CURRENT_LIST_DIR}/*.cpp)
add_executable(${PROJECT_NAME}_bench
    ${${PROJECT_NAME}_BENCH_SOURCE_FILES} 
)

target_link_libraries(${PROJECT_NAME}_bench PRIVATE TemplateLib benchmark::benchmark)