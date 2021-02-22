Can you find the flag in file without running it?


## Lösung


mit dem Command `strings` können lesbare Strings in einem File ausgegeben werden

nun kann Folgender Command gebildet werden

`curl {link} | strings | grep "picoCTF"`

Flag:
picoCTF{5tRIng5_1T_7f766a23}