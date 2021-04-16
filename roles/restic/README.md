stehessel.server.restic
=======================

Sets up `restic` backups attached to B2 repositories. The backup schedule can be set via cron.

Role Variables
--------------

```yaml
restic__repos:
    - bucket: bucket-name
      account_id: b2-account-id
      account_key: b2-account-key
      password: repo-password
      path: local-path-to-backup

      minute: "0"
      hour: "*"
      day: "*"
      month: "*"
      weekday: "*"
```

Backup repositories in B2 cloud.

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Set up restic"
      include_role:
        name: "stehessel.server.restic"
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
