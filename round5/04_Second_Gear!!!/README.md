# Second Gear!!!

**Points:** 200
**Description:**

> It's called reverse engineering it means something.   
 
http://kekwa.utphax.my/8d799967e6b3c5ed5df7611b19c4d8e0331f39d8

## Write-up

Another reversing challenge, a tricky one this time!

Run it in Ollydbg and we can see that it is executing almost the same operation as the binary in round 1, but this time round it XOR the input with `0x44`. If we successfully solve it using the same method as in round 1, the program outputs `Congratulations but is it the correct answer?`. Hmm, the same method cannot be applied twice.

Looking at the assembly instructions just before the `printf()` function is called, we see the following:

```asm
00401511  |. C64424 3B 76   MOV BYTE PTR SS:[ESP+3B],76              ; ||
00401516  |. C64424 3C 74   MOV BYTE PTR SS:[ESP+3C],74              ; ||
0040151B  |. C64424 3D 76   MOV BYTE PTR SS:[ESP+3D],76              ; ||
00401520  |. C64424 3E 2A   MOV BYTE PTR SS:[ESP+3E],2A              ; ||
00401525  |. C64424 3F 2B   MOV BYTE PTR SS:[ESP+3F],2B              ; ||
0040152A  |. C64424 40 2D   MOV BYTE PTR SS:[ESP+40],2D              ; ||
0040152F  |. C64424 41 30   MOV BYTE PTR SS:[ESP+41],30              ; ||
00401534  |. C64424 42 25   MOV BYTE PTR SS:[ESP+42],25              ; ||
00401539  |. C64424 43 28   MOV BYTE PTR SS:[ESP+43],28              ; ||
0040153E  |. C64424 44 31   MOV BYTE PTR SS:[ESP+44],31              ; ||
00401543  |. C64424 45 30   MOV BYTE PTR SS:[ESP+45],30              ; ||
00401548  |. C64424 46 25   MOV BYTE PTR SS:[ESP+46],25              ; ||
0040154D  |. C64424 47 36   MOV BYTE PTR SS:[ESP+47],36              ; ||
00401552  |. C64424 48 23   MOV BYTE PTR SS:[ESP+48],23              ; ||
00401557  |. C64424 49 2A   MOV BYTE PTR SS:[ESP+49],2A              ; ||
0040155C  |. C64424 4A 2B   MOV BYTE PTR SS:[ESP+4A],2B              ; ||
00401561  |. C64424 4B 07   MOV BYTE PTR SS:[ESP+4B],7               ; ||
```

Suspicious enough. Concatenate the hex values bottom up and XOR it with `0x44` each, thus yielding `0x436f6e67726174756c6174696f6e323032`, which is also, in ASCII, `Congratulation202`.
