stehessel.server.seafile
========================

Sets up a `seafile` cloud service.

Role Variables
--------------

```yaml
seafile__admin_email: admin@example.com
seafile__admin_password: asecret
seafile__database_password: db_dev
seafile__domain: seafile.example.com
seafile__garbage_collect_cron: 0 6 * * SUN
seafile__memcache: 512
seafile__path: /srv/seafile
seafile__timezone: Europe/Berlin
```

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Set up Seafile"
      include_role:
        name: "stehessel.server.seafile"
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
