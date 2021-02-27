What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.


## Lösung:

Linux besitzt die Programme base64 und base32, diese können zum en-decoden verwendet werden.


Verwendeter Befehl:

`echo bDNhcm5fdGgzX3IwcDM1 | base64 -d`