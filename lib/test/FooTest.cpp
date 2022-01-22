#include <gmock/gmock.h>
#include "Foo.hpp"

TEST(FooTest, false){
    EXPECT_TRUE(foo::Foo{});
}