# system-user-backup
Service templates for systemd that backup and restore system user state.

These templates are for backing up the state of individual applications.
They are opinionated and have specific requirements.

For each instance, `foo`:
* An encrypted, systemd credential called `foo_backup` must exist.
* The contents of that credential are used as configuration for `rclone`.
* The configuration must have a section called `foo`.
* The contents of `/var/lib/foo` are backed up.
* The service is run as user `foo` and group `foo`.
