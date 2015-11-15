# Yeah..management..

**Points:** 500
**Description:** 

> CEO send this file. He cannot open it. Help him. Download the file at http://kekwa.utphax.my/ODEwYzI4NTMxNjYwNGUzZmQ2NjJkYTIx/platipus.xlsx

## Write-up

A spreadsheet document, well, is just another archive file. Extract it normally just like an archive file. There are several interesting items here, `makethisfilecorrupt.txt` and the directory `New folder`. We tried `strings` command on the text file:

```
$ strings makethisfilecorrupt.txt | less
maybe you should remove this?
flag is inside
```

It's telling us that the flag is inside, let's dive deeper. Inside `New Folder` there's another `ayam.xlsx`. Extract it but this time, nothing interesting. Nevertheless, we went and used `strings` on everything, eventually, we found the flag in `xl/worksheets/sheet4.xml`.

The flag is `myfileisbrokenmommy`. 500 points nabbed!

Note: Files extracted from the `.xlsx` file has no read, write nor execute permission for all users. Before viewing or extracting the files, run `chmod 700 <filename>`.
