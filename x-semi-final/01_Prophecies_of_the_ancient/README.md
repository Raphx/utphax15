# Prophecies of the ancient

**Points:** 150
**Description:**

```
Oyster Sauce to Chinese is ******* to Yankee
    
http://kekwa.utphax.my/b38a2e555438195aea3e548d7847ff73d2507556.7z
```

## Write-up

In this challenge we were given a VMware image file, for Windows 3.1!

Load it up, and we are in pure command-line mode, with no GUI at all. There is a directory, `COOK` that piqued our interest. Unfortunately, we were unable to launch the `COOK.EXE` inside it, since it requires some graphical display components.

We then navigated around some folders, and launched an executable that initialized the graphical interface (well, yeah, forgot what's the name of it). Back to launching the `COOK.EXE`, it succeeded!

`COOK.EXE` is a cookbook program, so let's search for "oyster sauce" in it. Look around some recipe, and we found `Oyster Sauce to Chinese is Catsup to Yankee` (well, something like this, again, can't remember).

The flag is `catsup`... or was it in uppercase? Baddddd memory :(
