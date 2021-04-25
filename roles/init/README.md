stehessel.server.init
=====================

Initial setup of operating system including timesync, locale, users and ssh.

Role Variables
--------------

```yaml
```

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Initial setup"
      include_role:
        name: "stehessel.server.init"
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
