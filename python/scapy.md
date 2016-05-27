# some notes about scapy
We often use srp function of scapy to send some packet and then receive from the interface we sent.
The source code of srp is as below, and the conf.L2socket is from ```scapy/arch/linux.py``` if you're using scapy on linux
* **srp**
```py
@conf.commands.register
def srp(x,iface=None, iface_hint=None, filter=None, nofilter=0, type=ETH_P_ALL, *args,**kargs):
    """Send and receive packets at layer 2
nofilter: put 1 to avoid use of bpf filters
retry:    if positive, how many times to resend unanswered packets
          if negative, how many times to retry when no more packets are answered
timeout:  how much time to wait after the last packet has been sent
verbose:  set verbosity level
multi:    whether to accept multiple answers for the same stimulus
filter:   provide a BPF filter
iface:    work only on the given interface"""
    if not "timeout" in kargs:
        kargs["timeout"] = -1
    if iface is None and iface_hint is not None:
        iface = conf.route.route(iface_hint)[0]
    s = conf.L2socket(iface=iface, filter=filter, nofilter=nofilter, type=type)
    a,b=sndrcv(s ,x,*args,**kargs)
    s.close()
    return a,b
```
