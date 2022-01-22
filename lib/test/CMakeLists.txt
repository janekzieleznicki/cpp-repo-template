find_package(GTest REQUIRED)
include(GoogleTest)
add_executable(${PROJECT_NAME}_test
    FooTest.cpp
)


target_link_libraries(${PROJECT_NAME}_test PRIVATE StaticFoo GTest::gtest_main GTest::gmock)
gtest_discover_tests(${PROJECT_NAME}_test)