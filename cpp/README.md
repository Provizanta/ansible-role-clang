Clang
=========

Install Clang LLVM compiler tools.

Requirements
------------

None

Role Variables
--------------

    versions: <list of versions to install>
    tools: <all/basic>  

Dependencies
------------

None

Example Playbook
----------------

    - hosts: localhost
      roles: dev/cpp
      vars:
        versions:
          - 7
          - 8
        tools: basic

License
-------

MIT

Author Information
------------------

Tibor Csoka
