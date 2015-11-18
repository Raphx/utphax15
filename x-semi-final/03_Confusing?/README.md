# Confusing?

**Points:** 300
**Description:**

> http://teratai.utphax.my/39STR9STRMNZ9STRMNZVqnVqnM9STRMNZVqnNZVqn/question.html

## Write-up

I must say, YES THIS WAS REALLY CONFUSING!

Opening up the web page, we were greeted with tons of GIF, a line of suspicious text in the middle of screen, as well as an MP3 audio playing in the background. On the page source, there were some interesting looking PHP codes that have been commented:

```php
str_replace("sense","submit",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("Years","answer",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("Silence","ayam",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("about","Real",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("voice","with",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("drown","space",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("strong","sexy",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("saved","is",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("way","Nanami",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("drown","movie?",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("start","watched",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("Fading","troll",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("to","the",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("day","cute",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("make","really?",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("around","flag",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("noise","underscore",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("end","then",$abc);babsfasmfa;smfliqhworiho28yhn19pyc249y1mc4o1j,xpj.pqjzi1hu2hzeim1bi2,zeb12bz,iy1b,eb,1izb2e12
str_replace("sounds","replace",$abc);
```

After a looong while, we figured out that it is replacing the strings in a lyrics for the MP3 song that was playing in the background. After replacing the strings in the lyrics, and looking at the end of each line (as pointed by the hint for the challenge), we got the flag `Nanami_is_cute`.
