project := "system-user-backup"
repo := "ghcr.io/jdmarble"

rpm:
    tito build --rpm --test --offline
