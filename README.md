Ansible role: clang
=========

![Build & Deploy](https://github.com/Provizanta/ansible-role-clang/workflows/molecule/badge.svg?branch=master)

Install Clang LLVM compiler & tools for repo.

Requirements
------------

None

Role Variables
--------------

These variables are defined in [defaults/main.yml](./defaults/main.yml):

    clang_version: 10              # int, clang versions

    clang_install_tools: false      # bool, install all clang tools

Dependencies
------------

None

Example Playbook
----------------

    - hosts: localhost
      roles:
        - role: clang
          vars:
            clang_version: 9
            clang_install_tools: true

License
-------

MIT

Author Information
------------------

Tibor Csóka
