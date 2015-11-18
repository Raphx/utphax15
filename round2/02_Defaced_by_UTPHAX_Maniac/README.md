# Defaced by UTPHAX Maniac

**Points:** 200
**Description:** 

```
Hate those defacers. Find me his track! http://kekwa.utphax.my/YmZlZjg5OTQwODQ2ZDM3YThlZmVkMzBm/deface_proof.7z
```

## Write-up

A website has been defaced! Let's track the hacker. Extract the `7z` archive file given and we see a list of directories. Inside `sekainoowari`, there's a `PNG` file. Looks suspicious, let's run `strings` command on it.

```bash
$ strings hacked-600x366.png | less
```

Now we see some binary strings (`01110011 01101111 00110000 01101111 00110000 01101111 00110000 01101111 00110000 01101111 00110000 01101111 01011111 01101000 01100001 01111000 00110000 00110000 00110000 00110000 01110010 01110010 00100001 00100001`). Convert those strings to its equivalent ASCII characters and viola, the flag is `so0o0o0o0o0o_hax0000rr!!`
