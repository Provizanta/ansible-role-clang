Ansible role: clang
=========

Install Clang LLVM compiler & tools for repo.

Requirements
------------

None

Role Variables
--------------

These variables are defined in defaults/main.yml

    versions: []    # list, clang version

    tools: false    # bool, install all clang tools

Dependencies
------------

None

Example Playbook
----------------

    - hosts: localhost
      roles:
        - role: clang
          vars:
            versions:
              - 7
            tools: true

License
-------

MIT

Author Information
------------------

Tibor Csóka
