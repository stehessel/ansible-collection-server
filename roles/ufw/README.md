stehessel.server.ufw
====================

Sets up 'ufw' as a firewall service.

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Set up ufw"
      include_role:
        name: "stehessel.server.ufw"
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
