stehessel.server.rsync
======================

Ansible role to deploy a minimal rsync service. Sets up `ufw` rules for rsync port.

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Set up rsync"
      include_role:
        name: "stehessel.server.rsync"
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
