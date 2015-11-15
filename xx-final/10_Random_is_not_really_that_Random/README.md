# Random is not really that Random

**Points:** 300
**Description:** 

> Connect to mawar.utphax.my:10081

## Write-up

For this challenge, the server sends 3 encoded strings, and we need to decode it accordingly and submit the solution.

The first string is Base64 encoded, the second one is ROT13, and the last one, which is the tricky part, is EBCDIC encoded.

Solution [here](c10.py).
