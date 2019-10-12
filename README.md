Ansible role: clang
=========

[![Build Status](https://travis-ci.com/Provizanta/ansible-role-clang.svg?branch=master)](https://travis-ci.com/Provizanta/ansible-role-clang)

Install Clang LLVM compiler & tools for repo.

Requirements
------------

None

Role Variables
--------------

These variables are defined in [defaults/main.yml](./defaults/main.yml):

    clang_versions: []    # list, clang version

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
            clang_versions:
              - 7
            clang_install_tools: true

License
-------

MIT

Author Information
------------------

Tibor Csóka
