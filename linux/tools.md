# some notes on *nix commands
* [tee](http://superuser.com/questions/847714/how-to-save-console-output-still-showing-it)

Descriptions from man:
> The tee utility copies standard input to standard output, making a copy in zero or more files.  The output is unbuffered.

Useful for recording down what received from a telnet session. For example, when I need the configuration of a switch, and I don't have tftp server at hand. We can use the following commands to get the config.

```sh
$ telnet 192.168.1.10 | tee -a /tmp/record.txt
> enable
...
> terminal length 0
...
> show running-config
brabra...the config we need

> exit
$
```
