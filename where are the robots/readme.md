Can you find the robots? [link](https://jupiter.challenges.picoctf.org/problem/56830/) or http://jupiter.challenges.picoctf.org:56830

## Lösung

Der Name und die Seite redet von Robots, viele Websiten besitzen eine Robots.txt, diese Seite auch wenn diese Seite geöffnet wird, öffnet sich folgende Meldung

```

User-agent: *
Disallow: /1bb4c.html

```

Wenn nun der Pfad **/1bb4c.html**

Eingegeben wird öffnet sich die Flag

Flag:
picoCTF{ca1cu1at1ng_Mach1n3s_1bb4c} 