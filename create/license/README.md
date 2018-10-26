Create license
=========

Create a license file for a programming project.

Requirements
------------

None

Role Variables
--------------

    license: license type
    project:
      name: project name
      path: path to the project directory
      owner: project owner
    

Dependencies
------------

None

Example Playbook
----------------

All variables are mandatory.

    - hosts: localhost
      roles:
         - role: dev/create/license
           vars:
             license: bsd-3
             project:
               name: "test"
               path: "~/proj/system/"
               owner: "Test Corp."

License
-------

MIT

Author Information
------------------

Tibor Csoka
