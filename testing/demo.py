#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pytest

# a = 1
# b = "2{}{}"
# c = 3
# print(b.format(a, c))

# @pytest.fixture(scope="module")
# def open_brower():
#     print("\n打开浏览器，打开百度首页")
#
#     yield
#
#     print("执行teardown")
#     print("最后关闭浏览器")

@pytest.mark.parametrize("test_input, expected", [("3+5", 8)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

#参数组合
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y",[8, 10, 11])
def test_foo(x, y):
    print(f"测试组合数据x: {x}, y: {y}")

#参数组合
@pytest.mark.parametrize("username",  ['username1', 'username2'])
@pytest.mark.parametrize("passwd",['password1', 'password2','password3'])
def test_combination(username, passwd):
    print(f"测试组合数据username: {username}, passwd: {passwd}")

#方法名作为参数
test_user_data = ['Tome', 'Jerry']
@pytest.fixture(scope="module")
def login(request):
    user = request.param
    print(f"登录用户: {user}")
    return user
# @pytest.mark.skip("此次测试不执行登录")
@pytest.mark.parametrize("login", test_user_data,indirect=True)
def test_login(login):
    a = login
    print(f"测试用例中login的返回值；{a}")
    assert a !=''

@pytest.mark.parametrize(["a", "b"],yaml.safe_load(open("./data.yaml")))
def test_param(self, a, b):
    print(a+b)





if __name__ == '__main__':
    pytest.main('-v')