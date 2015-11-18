# Hello World

**Points:** 300
**Description:**

> http://perbendaharaan.utphax.my

## Write-up

Not solved :(

... actually we were on the right track to solving it, but we didn't focus much on this challenge.

This is a web challenge, viewing the page source gives us info that site uses Joomla CMS. After researching Joomla directory structure for awhile, we discovered that there is an administrator page at `http://perbendaharaan.utphax.my/administrator`.

We were then greeted with the login page, and that was all that we have done.

After semi-final ended, the judges informed us that the Joomla version in use is vulnerable to an SQL injection attack that has been discovered disclosed recently, for more info refer [here](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-7857). 
