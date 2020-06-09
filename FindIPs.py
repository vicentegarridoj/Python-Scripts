import re #import Regular Expression Python module

ipAddRegex = re.compile(r'\d+\S\d+\S\d+\S\d+') #This is the pattern that I want to match
ipList = ''' paste your text which contains IP addresses ''' #Paste the values inside triple-quote syntax

ipAddRegex.findall(ipList) #Run this function passing the ipList argument
