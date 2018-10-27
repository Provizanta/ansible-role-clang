Ignore files
=========

Create an ignore file for a programming project.

Requirements
------------

None

Role Variables
--------------

    path: path to the project directory
    language: project programming language
    ignore: list of elements to add to the default ignore file

Dependencies
------------

None

Example Playbook
----------------

At least project path and language should be supplied.

    - hosts: localhost
      roles:
         - role: dev/create/ignore_file
           vars:
             path: "~/proj/system/"
             language: "Python"
             ignore:
               - "bin/"

License
-------

MIT

Author Information
------------------

Tibor Csoka
