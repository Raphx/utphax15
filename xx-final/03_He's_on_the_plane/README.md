# He's on the plane

**Points:** 300
**Description:** 

> Hacker leave this only file and his message 'JiUTMtMJH9hlkBHAjtWkT086ZKqCf0kdpu5S1hkOGdk=' . File can be downloaded at http://kekwa.utphax.my/NzUzYWQxNDhlNWUzNGE5ZDU0N2E4M2Y1/Backup.7z

## Write-up

Extract the `7z` archive, and we see some text files. `Backup/pastebin.txt` contains exactly the same string as the one given at the description. Another important file is `Backup/junk stuff.txt`. Yup, junk stuff is not actually junk.

A quick glance at the file tells us that the string `param` is Base64 decoded followed by a Triple DES decryption using `strPassPhrase` as the passphrase. So `param` is the Base64 string, now we just need the passphrase. There is a string, `#2015_utphax_by_yap_osem!` at the bottom of the file and we decided to try using it as the passphrase. It works, wonderfully!

The decryption result yields `49.7494° N, 113.6250° W`. Put it in Google Map, and with some advice from the judges, we got the flag `Head-Smashed-In_Buffalo_Jump`.
