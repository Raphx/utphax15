# Binary Warmup For you

**Points:** 150
**Description:**

> Ready Steady 
http://kekwa.utphax.my/8891b3cde3085a3fe8706585f78f162420f98177
Very simple.

# Write-up

A PE32 binary slapped in the face as soon as round 1 started ;)

Execute the program, and we see that it is asking for a secret key input and performs some checks on the input after it has been entered.

We use Ollydbg for this challenge. Set a breakpoint after the `gets` function, and step through each of the innstruction one-by-one.

In general, the program will move one character into `EAX`, XOR it with `0x41`, and compare the result with a hardcoded hex value. If both the operands are not the same, it will terminate.

So just supply a dummy input, step through the instruction to inspect the hardcoded hex value, and XOR that value with `0x41` to get back the desired input. Repeat it until the program prints `You win!`.

The secret key, which is the flag, is `Hack101`.

We solved this challenge just right after round 1 ended, no points for us :(
