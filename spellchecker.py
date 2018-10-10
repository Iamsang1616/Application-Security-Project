
#Various Includes go here
import mmap
import re
import string

#Maintain status of if typo is found or not
typo = False;

#Accept input from user as the raw input (string)
my_file = raw_input("Enter the name of the file you wish to check: ");

#Turn the list of words into an mmap to prevent any major memory issues
dictionary = open("english-words-master\words.txt", "r") 
d = mmap.mmap(dictionary.fileno(), 0, access=mmap.ACCESS_READ)

typos = [];

#debug statement
print("NOW CHECKING: " + my_file + "\n");



#open the file and for every word in each line:
try:
    with open(my_file, "r") as f:
        for line in f:
            for word in line.split():

                #strip any non-essential punctuation (periods, colons, etc.)
                word = re.sub("[^A-Za-z'-]", '', word);

                
                #If something doesn't even look like a word in the first place
                #Mention it and continue searching
                if (not re.match("^[A-Za-z'-]+$", word)):

                    #debug
                    print ("\"" + word + "\" is not a word\n");

                    
                    continue;

                #if something seems like a word
                else:

                    #If it starts with a capital letter, and has lowercase following it
                    if (re.match("^[A-Z][a-z-']+$", word)):

                        #debug
                        #print ("\"" + word + "\" starts with a capital");

                        #if the word isn't found in the dictionary as it is
                        if d.find(word) == -1:

                            #And if the word doesn't exist as a lowercase version, then consider it a typo
                            if not d.find(string.lower(word)):
                                
                                typos.append(word);
                                
                    #if it's not that particular format
                    else:

                        #If not in the dictionary, add it to the typo list
                        if d.find(word) == -1:

                            #debug
                            #print ("\"" + word + "\" seems like a word, but is ultimately not a word\n");
                            typos.append(word);


    print ("The following typos were found in the file:\n")

    if len(typos)==0:
        print ("No typos found\n");
    else:
        for w in typos:
            print (w + "\n");


    #close the file before exiting
    f.close()
    dictionary.close()


#If file doesn't exist, notify user
except IOError: 
    print ("ERROR: File " + my_file + " does not exist\n");
    




