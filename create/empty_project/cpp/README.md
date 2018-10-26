Empty C++ project
=========

Create an empty C++ project.

Requirements
------------

None

Role Variables
--------------

    path: project destination path
    
    project:
      name: project name
      license: license, under which the project is licensed

Dependencies
------------

None

Example Playbook
----------------

At least project name should be supplied.

    - hosts: localhost
      roles:
         - role: dev/create/empty_project/cpp
           vars:
             path: "~/proj/system/"
             project:
               name: "Fantasy project name"
               license: "BSD-3"

License
-------

MIT

Author Information
------------------

Tibor Csoka
