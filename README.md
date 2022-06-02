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
Search: ./gitdiscloser.py [-h] [-s "github search"] [-f wordlist] [-k keyword] [-u] [-n]
Profiling: ./gitdiscloser.py [-h] [-r repository link] [-p]
```
## options:
```bash
Options
  ----------------------------------------------
        -h   Show this help message
  Search:
        -s   search request
        -u   search for urls in code
        -f   find word matches with a wordlist
        -n   sort by the more recently indexed
        -k   search for keyword
  Profiling:
        -r   repository link
        -p   profile information
  ----------------------------------------------
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
So you can use the profiling option of GitDiscloser to get profile information about it and then see the firstname of the author or if he/she work in your target company. (if it is not written in github you can check is firstname on Linkedin.
  
If your target work at the target company, you can now check for (potentially other) information disclosure in his/her other codes thanks to the "user:" dork
Exemple:
```bash 
./gitdiscloser -s "user:<username>" -f <wordlist> -n
```
## Some screens:

![image](https://user-images.githubusercontent.com/40497633/171599615-d4ea31ac-a6bb-4d8d-9be7-0ef7a1e6ab33.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/171599909-f942bc64-7e95-4c89-8fcd-a190b79dd45b.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/171600194-a5504367-0d29-411e-9af2-c05a3fb4899a.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/171600770-77d167e8-b95f-4e4b-a234-bc65a4c50cbf.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/171601131-718194d0-2fbf-4eba-8aaf-7623ad8ad950.png)
![image](https://user-images.githubusercontent.com/40497633/171602264-671fb8a0-8369-4e38-9c55-caca6ea2b96c.png)

## TO DO

- fix bugs
- Add an output file option (you can use "| tee -a" to get an output anyway") 
- Add a limit option
