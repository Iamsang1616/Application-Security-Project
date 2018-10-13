
#Various Includes go here
import mmap
import re
import string

#Maintain status of if typo is found or not
typo = False;

my_file = "";


while True:


        #Turn the list of words into an mmap to prevent any major memory issues
        dictionary = open("english-words-master\words.txt", "r");
        d = mmap.mmap(dictionary.fileno(), 0, access=mmap.ACCESS_READ)
        
        #Accept input from user as the raw input (string)
        my_file = raw_input("Enter the name of the file you wish to check, or type 'stop' to exit: ");


        
        if (my_file == "stop"):
                break;

        typos = [];

        print("NOW CHECKING: " + my_file + "\n");

        

        
        try:
                #open the file and for every word in each line:
                with open(my_file, "r") as f:
                        for line in f:
                                for word in line.split():

                                       


                                        #Check if the word doesn't exist as it is.
                                        if d.find(word) == -1:
                                                
                                                
                                                #strip any punctuation (periods, colons, etc.)
                                                word = re.sub("[^A-Za-z'-]", '', word);

                                                #If it starts with a capital letter, and has all lowercase following it
                                                if (re.match("^[A-Z][a-z-'.]+$", word)):
 
                                                        #if the word isn't found in the dictionary as it is
                                                        #(Proper Nouns)
                                                        if d.find(word) == -1:
                                                                
                                                                #And if the word doesn't exist as a lowercase version, then consider it a typo
                                                                if d.find(string.lower(word)) == -1:
                                                                        typos.append(word);
                    
                                                #if it's not that particular format
                                                else:

                                                        #If the word doesn't exist, even as a lowercase version, then consider it a typo
                                                        if d.find(string.lower(word)) == -1 and d.find(word) == -1:

                                                            typos.append(word);


                #Print all the typos found, if any. Or tell user none were found
                if len(typos)==0:
                        print ("No typos found\n");
                else:
                        print ("The following typos were found in " + my_file + ": \n");
                        for w in typos:
                                print (w);

                        print ("\n");


                #close the file before exiting
                f.close()



        #If file doesn't exist, notify user and stop the program
        except IOError: 
                print ("ERROR: File " + my_file + " does not exist\n");
                

#Close the dictionary file    
dictionary.close()



