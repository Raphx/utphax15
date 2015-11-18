# Now it getting serious

**Points:** 100
**Description:**

> Our threat analyst,Shitoka, found that there's a malicious Windows executable file was downloaded by the victim. Shitoka already provide the MD5 Hash of that file to our Firewall expert, Robert so he can put in watch mode. Do you know the hash?!  Download the analysis file at http://kekwa.utphax.my/NTg4MzRmZGZhN2IzYTg5MjViMGI1MjI4/senang4.pcap

## Write-up

The last challenge in the 'senang' series of pcap forensics :D

Open the capture file using Wireshark. The challenge mentions some `exe` file being downloaded by the victim, so the first thing we did was to export the HTTP objects, and save any objects with a MIME type of `application/octet-stream`.

There are two executables being transmitted, calculate the MD5 hash of both files and one of results is the flag.
