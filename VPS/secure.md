1. change ssh port
2. create sudo account
3. disable root login
4. disable password login
5. setup firewall
6. setup fail2ban
7. setup automatic updates

# sources.list
```
# deb-src http://archive.ubuntu.com/ubuntu/ jammy main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ jammy-updates main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ jammy-backports main restricted universe multiverse
deb https://archive.ubuntu.petiak.ir/ubuntu/ jammy main restricted universe multiverse
deb https://archive.ubuntu.petiak.ir/ubuntu/ jammy-updates main restricted universe multiverse
deb https://archive.ubuntu.petiak.ir/ubuntu/ jammy-security main restricted universe multiverse
deb https://archive.ubuntu.petiak.ir/ubuntu/ jammy-backports main restricted universe multiverse
deb http://archive.canonical.com/ubuntu/ jammy partner
```

# check
```
Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

```