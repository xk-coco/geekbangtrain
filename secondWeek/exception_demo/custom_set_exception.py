#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 0:47
# @File    : custom_set_exception.py


class UserInputError(Exception):
    """先当固定的用法记着"""

    def __init__(self, info):
        super(UserInputError, self).__init__(info)
        self._info = info

    def __str__(self):
        return self._info


if __name__ == '__main__':
    userinput = input("Please input: ")
    try:
        if (not userinput.isdigit()):
            raise UserInputError('用户输入错误')
    except UserInputError as ue:
        print(ue)
