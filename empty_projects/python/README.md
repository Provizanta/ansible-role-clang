Empty Python project
=========

Create an empty Python project with setuptools support.

Requirements
------------

None

Role Variables
--------------

    path: "~/projects/"

    python:
      version: '3'

    project:
      name: 'new-project'
      description: "This is a new project's description."
      author:
        name: "Name Surname"
        email: "name@surname.com"
      version: 0.1
      license: 'MIT'
      classifiers:
        - 'Programming Language :: Python :: 3'
      keywords: []
      dependencies: []

Dependencies
------------

None

Example Playbook
----------------

At least project path and basic project details should be specified.

    - hosts: localhost
      roles:
         - role: dev/empty_projects/python
           vars:
             path: "~/proj/system/"
             python:
               version: 2.7
             project:
               name: "Project name"
               author:
                 name: "My name"
                 email: "my@name.com"

License
-------

MIT

Author Information
------------------

Tibor Csoka
