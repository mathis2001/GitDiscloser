#!/usr/bin/env python3

from github import Github
import sys
from sys import argv
import requests
import re
import os

ACCESS_TOKEN = os.environ['GITHUB_TOKEN']

token = Github(ACCESS_TOKEN)

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'
	
def banner():
        print('''

   ______   _   _   ______     _                 __
 .' ___  | (_) / |_|_   _ `.  (_)               [  |  by S1rN3tZ
/ .'   \_| __ `| |-' | | `. \ __   .--.   .---.  | |  .--.   .--.  .---.  _ .--.   
| |   ____[  | | |   | |  | |[  | ( (`\] / /'`\] | |/ .'`\ \( (`\]/ /__\\[ `/'`\]  
\ `.___]  || | | |, _| |_.' / | |  `'.'. | \__.  | || \__. | `'.'.| \__., | |      
 `._____.'[___]\__/|______.' [___][\__) )'.___.'[___]'.__.' [\__) )'.__.'[___]     

        ''')

def help():
	print('''
  Options
  ----------------------------------------------
  	-h   Show this help message
  Search:
	-s   search request
	-u   search for urls in code
	-f   find word matches with a wordlist
	-n   sort by the more recently indexed
	-k   search for keyword
	-l   limit (number of results wanted)
  Profiling:
  	-r   repository link
	-p   profile information
  ----------------------------------------------
  Config

        Simply put your github token in your environment variables with the name 'GITHUB_TOKEN'.

	''')

def getopts(argv):
	opts = {}  
	while argv:
		try:
			if argv[0][0] == '-':
				opts[argv[0]] = argv[1] 
		except:
			if argv[0] == '-h':
				print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: Search: ./gitdiscloser.py [-h] [-s github search] [-f wordlist] [-k keyword] [-l limit] [-u] [-n]")
				print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: Profiling: ./gitdiscloser.py [-h] [-r repository link] [-p]")
				help()
				sys.exit(0)
		argv = argv[1:] 
	return opts

def main():
	myargs = getopts(argv)
	if len(sys.argv) < 2:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"No target given.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: Search: ./gitdiscloser.py [-h] [-s github search] [-f wordlist] [-k keyword] [-l limit] [-u] [-n]")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: Profiling: ./gitdiscloser.py [-h] [-r repository link] [-p]")
		sys.exit(0)
	rate_limit = token.get_rate_limit()
	rate = rate_limit.search
	if rate.remaining == 0:
		print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}.')
	else:
		print(f'You have {rate.remaining}/{rate.limit} API calls remaining.')
	
	if '-r' in myargs:
		repo = myargs['-r']
		repolist = repo.split("/")
		repolist.pop(1)
		username = repolist[2]
		if '-p' in sys.argv:	
			getuser = token.get_user(username)
			bio = getuser.bio
			email = bcolors.INFO+str(getuser.email)+bcolors.RESET
			firstname = bcolors.INFO+str(getuser.name)+bcolors.RESET
			avatar = getuser.avatar_url
			company = bcolors.INFO+str(getuser.company)+bcolors.RESET
			location = getuser.location
			followers = bcolors.INFO+str(getuser.followers)+bcolors.RESET
			following = bcolors.INFO+str(getuser.following)+bcolors.RESET
			blog = getuser.blog
			creation = getuser.created_at
			update = getuser.updated_at
			print(f'''
	 avatar: {avatar} 
	       ____________________________________________________________________
              [ Profile	                                                      -   x]
              |____________________________________________________________________|
              |						                    
       	      |	username: {username}                        
              |	firstname: {firstname}	                    
              |	bio: {bio}                                  
	      | email: {email}
	      | company : {company}
	      |	location: {location}
              |
	      |	followers: {followers} following: {following}
	      |	
	      |	website: {blog}
              [____________________________________________________________________
         created at: {creation}
	last update: {update}
			''')
			
	elif '-s' in myargs:
		
		if '-n' in sys.argv:
			query = "sort:indexed "+myargs['-s']
		else:
			query = myargs['-s']
		result = token.search_code(query, order='desc')

		max_size = 100
		print(f'Found {result.totalCount} file(s):')
		
		if '-l' in myargs:
			limit = int(myargs['-l'])
			result = result[:limit]

		elif result.totalCount > max_size:
			result = result[:max_size]

		for file in result:
			url=f'{file.download_url}'
			print(bcolors.OK+"[+] "+bcolors.RESET+url)
			if '-u' in sys.argv:
				r = requests.get(url)
				regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
				match = re.findall(regex,r.text)
				print(bcolors.INFO+"\n URL(s) found in file:\n"+bcolors.RESET)
				for Url in match:
					print(bcolors.INFO+"[*] "+bcolors.RESET+Url[0])

			if '-k' in myargs:
				r = requests.get(url)
				reg = myargs['-k']
				count=0
				keyMatch = re.findall(reg,r.text)
				if reg in keyMatch:
					print(bcolors.OK+"[+] "+bcolors.RESET+"Keyword found !")
				for keyword in keyMatch:
					count = count+1
				print(bcolors.INFO+"[*] "+bcolors.RESET+"Keyword matched "+str(count)+" time(s). \n")

			if '-f' in myargs:
				SecretList=[]
				FinalList=[]
				r = requests.get(url)
				wordlist = myargs['-f']
				print(bcolors.INFO+"\n Possible secret(s) found in file:\n"+bcolors.RESET)
				with open(wordlist) as l:
					for word in l:
						word = word.splitlines()
						word = ' '.join(word)
						SecretMatch = re.findall(word,r.text)
						for find in SecretMatch:
							SecretList.append(find)
							for secret in SecretList:
								if secret not in FinalList:
									FinalList.append(secret)
				for SecretFind in FinalList:
					print(bcolors.OK+" [+] "+bcolors.RESET+SecretFind+"\n")
if __name__ == '__main__':
	try:
		banner()
		main()
	except Exception as e:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"A problem has occured.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"Error info:")
		print(e)
	except KeyboardInterrupt:
        	print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")
