# GitDiscloser
Python recon tool for Github information disclosure research

## Install:
```bash
$ git clone https://github.com/mathis2001/GitDiscloser

$ cd GitDiscloser

$ python3 gitdiscloser.py
```
## Usage:
```bash
Search: ./gitdiscloser.py [-h] [-s "github search"] [-f wordlist] [-l limit] [-u] [-n] [-c]
Profiling: ./gitdiscloser.py [-h] [-r repository link |-p username]
```
## options:
```bash
Options
  ---------------------------------------------------------
        -h   Show this help message
  Search:
        -s   search request
        -u   search for urls in code
        -f   find word matches with a wordlist
        -n   sort by the more recently indexed
        -l   limit (limit of results wanted)
        -c   profile information for each result
  Profiling:
        -r   profile information by repository link
        -p   profile information by username
  --------------------------------------------------------
  Config 

        Simply put your github token in the api.cfg file. 

```
## Configuration:

In your Github account, clic on your profile in the top right of the page.

Then go to settings > Developer settings > personal access tokens > Generate a new token.

Give a name to your token, select only the public_repo access and clic on "Generate token".

![image](https://user-images.githubusercontent.com/40497633/171192364-aa66b523-cb2f-40e4-bcf2-8b007a1ad682.png)


You can now copy your token and paste it in the api.cfg file.

## Use case:

You search for information disclosure on a target website/domain (exp:target.com), so you can use GitDiscloser like this:
```bash
./gitdiscloser.py -s target.com -f <wordlist> -n
```
or if you want to use dorks:
```bash
./gitdiscloser.py -s "<dork>:target.com" -f <wordlist> -n
```
this command will make a github search on all recently shared file ("-n") and will search for all keywords of your wordlist in it ("-f").
  
If the tool find interesting results, you maybe want to know more about the author of the file.
So you can use the profiling option of GitDiscloser to get profile information about it and then see his/her firstname and the company where he/she work. (if company is not written in his/her github account, you can check his/her firstname on Linkedin to check it).

Exemple:

GitDiscloser response:

https://raw.githubusercontent.com/mathis2001/code.xyz

Possible secret(s) found in file:

[+] token

Check if mathis2001 work at target.com:

./gitdiscloser -r https://raw.githubusercontent.com/mathis2001/code.xyz or -p mathis2001

you can also profile each results with the '-c' option.
  
If your target work at the target company, you can now check for (potentially other) information disclosure in his/her other codes thanks to the "user:" dork
Exemple:
```bash 
./gitdiscloser -s "user:<username>" -f <wordlist> -n
```
## Some screens:

![image](https://user-images.githubusercontent.com/40497633/171843426-39d00404-c76d-4883-96e5-c0832f55b026.png)
![image](https://user-images.githubusercontent.com/40497633/171844662-ffea0b28-9e91-4602-93ef-caa3b588db03.png)
![image](https://user-images.githubusercontent.com/40497633/171844784-ab67d302-5875-4d10-ac20-a49dbc318a43.png)
![image](https://user-images.githubusercontent.com/40497633/171850660-4daa556b-c592-4559-93ff-bb5f98330cf2.png)



## TO DO

- fix bugs
- Add an output file option (you can use "| tee -a" to get an output anyway")
- Secondary rate-limit restriction when making a query with to many responses.
