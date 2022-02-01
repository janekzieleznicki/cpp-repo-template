find_package(GTest REQUIRED)
include(GoogleTest)
file(GLOB ${PROJECT_NAME}_TEST_SOURCE_FILES ${CMAKE_CURRENT_LIST_DIR}/*.cpp)
add_executable(${PROJECT_NAME}_test
    ${${PROJECT_NAME}_TEST_SOURCE_FILES} 
)


target_link_libraries(${PROJECT_NAME}_test PRIVATE TemplateLib GTest::gtest_main GTest::gmock)
gtest_discover_tests(${PROJECT_NAME}_test)