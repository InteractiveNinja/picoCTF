Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

## Lösung

Die Lösung war es die File zu curlen und den Output dann durch grep zu schicken um diesen dann nach "picoCTF" zu suchen

Befehl:
`$ curl {link} | grep 'picoCTF'`