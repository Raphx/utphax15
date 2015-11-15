# Piracy is no good

**Points:** 300
**Description:** 

> Did I bought a fake software?! http://kenanga.utphax.my/ZGRmMmVmNDNhOWFkYmI4Y2M5MjgwMDQ2/BukuNota2.0.exe

## Write-up

Reversing challenge. First let's launch the program and try to activate it using a license. Well, wrong license, it says `Try harder`.

Open up IDA and load the binary, search for the string `Try harder`, and ta-da, we see a list of strings just above the address of the searched string. Concatenate the list of strings and there's our flag.
