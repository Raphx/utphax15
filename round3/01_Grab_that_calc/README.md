# Grab that calc

**Points:** 200
**Description:**

> As you know.. We all love our math teacher.
    
http://kekwa.utphax.my/06b1e9e77227cba3b8886fbd9511952cc688b6b3

## Write-up

This is another reversing challenge, but it is quite simple. Let's Ollydbg it.

```asm
0040152E  |. 8B4424 1C      MOV EAX,DWORD PTR SS:[ESP+1C]            ; ||
00401532  |. 35 FECAADDE    XOR EAX,DEADCAFE                         ; ||
00401537  |. 894424 1C      MOV DWORD PTR SS:[ESP+1C],EAX            ; ||
0040153B  |. 8B4424 1C      MOV EAX,DWORD PTR SS:[ESP+1C]            ; ||
0040153F  |. 35 ADDEFECA    XOR EAX,CAFEDEAD                         ; ||
00401544  |. 894424 1C      MOV DWORD PTR SS:[ESP+1C],EAX            ; ||
00401548  |. 8B4424 1C      MOV EAX,DWORD PTR SS:[ESP+1C]            ; ||
0040154C  |. 35 FF1000C0    XOR EAX,C00010FF                         ; ||
00401551  |. 894424 1C      MOV DWORD PTR SS:[ESP+1C],EAX            ; ||
00401555  |. 8B4424 1C      MOV EAX,DWORD PTR SS:[ESP+1C]            ; ||
00401559  |. 3D E9461296    CMP EAX,961246E9                         ; ||
```

At first, the program prompts for an input. It then XOR it sequentially with `0xDEADCAFE`, `0xCAFEDEAD`, `0xC00010FF` and compares the result with `0x961246E9`. All we need to do is just XOR `0x961249E9` backwards with all the operands to get the required input.

After XOR-ing it, we got `0x42414245`, convert it to ASCII string, and `BABE` is our flag.
