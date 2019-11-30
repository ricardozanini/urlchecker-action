#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pytest
from check import clone_repo, del_repo, check_repo


@pytest.mark.parametrize('git_path', ["https://github.com/SuperKogito/SuperKogito.github.io"])
def test_clone_and_del_repo(git_path):
    """
    test clone and del repo function.
    """
    # test correct functioning
    # clone
    base_path = clone_repo(git_path)
    assert(base_path == os.path.basename(git_path))
    # delete
    deletion_status = del_repo(base_path)
    assert(deletion_status == True)


@pytest.mark.parametrize('file_paths', [["tests/test_files/sample_test_file.md"],
                                        ["tests/test_files/sample_test_file.py"],
                                        ["tests/test_files/sample_test_file.rst"]])
@pytest.mark.parametrize('print_all', [False, True])
def test_check_repo(file_paths, print_all):
    """
    test check repo function.
    """
    check_repo(file_paths, print_all)

@pytest.mark.xfail
def test_script():
    os.system("python3 check.py")