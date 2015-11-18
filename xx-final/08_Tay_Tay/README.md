# Tay tay

**Points:** 300
**Description:** 

> Taylor Swift love you if you concat everything . Kyaaa    
 
http://kekwa.utphax.my/099c48df51343379a3f79620cbcffb84b0a38c24.E01

## Write-up

This challenge is quite different. We were given a very huge file with an extension of `.E01`. The `file` command outputs the following:

```bash
$ file 099c48df51343379a3f79620cbcffb84b0a38c24.E01 
099c48df51343379a3f79620cbcffb84b0a38c24.E01: EWF/Expert Witness/EnCase image file format
```

EnCase image file, hmm, we googled around and decided to use OSForensics to open it up on Windows. After browsing through the file system for quite a while, we found some stuff inside the directory (iirc) `C:\Windows\Desktop`.

The file `C:\Windows\Desktop\IMPORTANT.txt` contains crap loads of text, but the important ones are capitalized, something like `LOOK INSIDE DOOM`, and there's a `doom` folder in the same directory :)

Go in the `doom` folder, launch `DOOM.EXE`, and load the game. There are save states that have been created beforehand, with each of them having a unique label. Concatenate the all the labels from top to bottom, and there's the flag (forgot what's the exact flag).

We had trouble launching the `DOOM.EXE` due to 64-bit compatibility issue, but eventually my resourceful teammate  installed an XP VM on the spot, and we got it done!

Note: For this challenge, the file is too big, ~600M, so we are not going uploading it.
