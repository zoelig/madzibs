# open fucntion allows you to open a file
# r (read mode) is the way it is being loaded in
# f is the context, which allows any file operations to be completed in the indent under it
# this is best practice in terms of opening files!

# small issue where story.txt file wasnt found when testing with print(story), i fixed it by making the madlibs project it's own folder
 


with open("story.txt" , "r") as f: 
    # f.read() gives all the of the text inside the file
    story = f.read()


# variables to help find words
    
# below is to store the words in the bracket
words = set()
# start of the word variable 
start_of_word = -1

# marks the start and ends of the brackets to then see what's inside them
target_start = "<"
target_end = ">"



# accessing all individual characters as an index
# enumerate gives access to the position, as well as the element at that position
for i, char in enumerate(story):

# if start_of_word is equal to target_start, start_of_word changes to i
# if the last char it checks is equal to target_end (>) AND the prior conditions have been met making start_of_word equal i, then it continues to list words found
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        # gives access to a slice (subsection of a string)
        word = story[start_of_word: i + 1]
        # adds word found from slice into set of words (sets do not repeat)
        words.add(word)
        # resetting word finder
        start_of_word = -1

# empty dictionary to ask the users for the word
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    # creates a dictionary associated with all of the values
    answers[word] = answer

# replacing the words in the story
    # this is a for loop
for word in words:
    #replaces every instance of one string with another
    story = story.replace(word, answers[word])

print(story)