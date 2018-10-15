Python
=========

Install Python environment.

Requirements
------------

None

Role Variables
--------------

use_legacy: a boolean value determining whether a legacy Python or Python3 is to be used

Dependencies
------------

None

Example Playbook
----------------

    - hosts: localhost
      roles: dev/python
      vars:
        use_legacy: true

License
-------

MIT

Author Information
------------------

Tibor Csoka
