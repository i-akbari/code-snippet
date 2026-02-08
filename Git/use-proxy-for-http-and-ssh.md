# http 

# ssh
- ~/.ssh/config
```
Host github.com
    Hostname github.com
    User git
    ProxyCommand nc -X connect -x <proxy_host>:<proxy_port> %h %p
```

### for HTTP proxy is running on 127.0.0.1:8080
```
Host github.com
    Hostname github.com
    User git
    ProxyCommand nc -X connect -x 127.0.0.1:8080 %h %p
```

### socks proxy
```
Host github.com
    Hostname github.com
    ProxyCommand nc -X 5 -x 127.0.0.1:1080 %h %p
```

# test connection
```
ssh -T git@github.com
```