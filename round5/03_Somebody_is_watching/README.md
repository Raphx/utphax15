# Somebody is watching

**Points:** 200
**Description:**

> get [me](http://kenanga.utphax.my/1e7f681f1280d0b2ee9454d077fcc16c/SpyMe.exe)

## Write-up

Spy me, intuition tells me it is a .NET assembly. Nevertheless, let's `file` it.

```bash
$ file SpyMe.exe 
SpyMe.exe: PE32 executable for MS Windows (GUI) Intel 80386 32-bit Mono/.Net assembly
```

Yup, it's .NET, now decompile it with ILSpy (this is where my intuition comes from). Scroll down at the relevant class, and this shows up:

```c#
private void button1_Click(object sender, EventArgs e)
        {
            string str = "the flag";
            string str2 = "is";
            string text = "nasikakwokbest";
            this.output_fl.Text = str + " " + str2;
            this.output_fl.AppendText(" md5(");
            this.output_fl.AppendText(text);
            this.output_fl.AppendText(")");
        }
```

Flag is `MD5("nasikakwokbest")` which is `2483ecdda3f3ee4b46bd3e18f0cfcf76`.
