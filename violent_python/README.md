# Things to improve:

## Chapter 1 - connect2socket
If running a scan against a range, add a block of code to see which IP addresses are able to be hit and which aren't. It would be nice to have that so that there are not a bunch of `[-] Error Timed out` errors.

Thinking about it though, what if the org blocks ICMP. Do I just need to suck it up and roll with a bunch of `[-] Error Timed out`'s?

### Chapter Challenge 
Password cracker:
using the crypt library, write a program that you can pass in a passwords.txt and a dictionairy.txt and compare the two. 

the password file will contain hashed and salted passwords (hashing alg is known to you) when the program reads the password compare the results to the dictionairy results.

The dictionairy.txt will be a list of dictionairy words in plaintext, the program will take each word and hash it with the appropriate algo and salt it then compare that to your list of hashed passwords. 