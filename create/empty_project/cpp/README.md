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
      description: project description
      author:
        name: author's full name
        email: e-mail contact
      license: license, under which the project is licensed

    scm: source control mechanism

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
               owner: "Fantasy Corp."
               license: "BSD-3"
             scm: "git"

License
-------

MIT

Author Information
------------------

Tibor Csoka
