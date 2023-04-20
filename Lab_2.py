# Maka a books dictionary, with 3 authors as keys and multiple books as values.
#Use an input() asking for author name and print as a string the list of books by that 
# author. Use the .join() method. 

books_dictionary = {"Albert Camus": ["The Outsider","The Stranger"],"Joe Weaver": ["Devops 101","Stunlocked"]}

author = input("Enter the name of an author: ")

print(",".join(books_dictionary[author]))
