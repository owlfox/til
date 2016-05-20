# ntpd
is a linux program developed by , it's both a client and a server.

## Why
Linux server syncs UTC time with remote server, The server time varies

## How
```
#config /etc/ntpd.conf
sudo vim /etc/ntpd.conf

# to run many instances at same machine
cp /etc/ntpd.conf /etc/ntpd1.conf
# note that you must end the file name with conf, otherwise when you run
$ ntpd -d -c /etc/ntpd1.conf
# you will read file cannot be loaded error
# and be sure to
interface ignore all
interface listen <ip address> or <interface name>
# to listen to specific interface
```
## Conclusion
