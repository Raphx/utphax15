# Web 1.0

**Points:** 100
**Description:** 

> http://kemboja.utphax.my/YmVjNTMwNGNmYTg0ZGIzZjFlZWY3OGI3/index.html

## Write-up

Open up the webpage, it's a blank page. Let's view the page source.

At the bottom part of the page source, there are some interesting scripts to be looked at.

```js
    var _0x371d = ["\x75\x73\x65\x72\x41\x67\x65\x6E\x74"];
    var x = navigator[_0x371d[0]];

    ..
    ..

    if (x.indexOf('The supreme art of war is to subdue the enemy without fighting.') >= 0) {
        ..
        ..
        document.getElementById("v").innerHTML = MD5(document.getElementById("v").innerHTML)
    }
```

Decoding the hexadecimal string yields `userAgent` and the string is assigned to the variable `x`. The variable `x` is then checked against a hardcoded string.

Now we know that it is checking the user-agent field of the HTTP request, simply change the value of the field using some utilities, such as User Agent Switcher, which is what my mate used ;) , to the hardcoded string.

Refresh the page, view the source again, and the flag is the MD5 value at the `v` element of the HTML DOM tree.

A tricky challenge making use of simple Javascript obfuscation technique :)
