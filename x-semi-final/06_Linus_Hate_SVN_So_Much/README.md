# Linus Hate SVN So Much

**Points:** 200
**Description:**

> Go to     
http://mawar.utphax.my/1f0f5d639c27a06467df0f96f4e0a9f8ac99f6b1/
We probably have overloaded our operators.

## Write-up

Linus hates SVN, and he created Git :)

Let's navigate to `http://mawar.utphax.my/1f0f5d639c27a06467df0f96f4e0a9f8ac99f6b1/.git` and here, we see some files in it, namely `aaa.txt`, which is empty, and `index.php.bak`, the exact same page as the challenge home page, except with the addition of commented PHP codes.

Looking at `index.php.bak`, we see this:

```php
    ...

    $filename = '#PROTECTED';
    extract($_GET);
    if (isset($cubaan)) {
        $combination = trim(file_get_contents($filename));
        if ($cubaan === $combination) {
            echo "<p>You are an elite . What kind of password is " .
                " $combination!?</p>";
             $flag = file_get_contents('#PROTECTED');
             echo "<p>The flag is" .
                " $flag</p>";
        }

    ...
```

We know that it is reading the combination from some file, and then compare that combination with our input, but we do not know what's the file name. This is where the `aaa.txt` comes in! Supply an additional GET parameter with the key-value pair of `filename=aaa.txt`, the `extract($_GET)` function will expand the `$_GET` array and override the `$filename` variable before it.

So now our `$filename` is `aaa.txt`. Guess what's the combination required? Yeap, just an empty string. We wrote a [script](solve.py), executed it and the flag is echoed on the screen.
