Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 41120 to get the flag?

## Lösung:

Auszug aus cheat.sh:

Netcat(nc) is a versatile utility for working with TCP or UDP data.
More information: <https://nmap.org/ncat>.

Die Lösung war es mit dem Socket zu verbinden:

### Befehl:

`$ nc jupiter.challenges.picoctf.org 41120`