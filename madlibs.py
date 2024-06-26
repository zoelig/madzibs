# r (read mode)
# small issue where story.txt file wasnt found when testing with print(story), i fixed it by making the madlibs project it's own folder
 


with open("story.txt" , "r") as f: 
    # f.read() gives all the of the text inside the file
    story = f.read()


# variables
words = set()

start_of_word = -1

target_start = "<"
target_end = ">"



# enumerate gives access to the position, as well as the element at that position in the index of the story
for i, char in enumerate(story):

# if start_of_word is equal to target_start, start_of_word changes to i
# if the last char(aracter) it checks is equal to target_end (>) AND the prior conditions have been met making start_of_word equal i, then it continues to list words found
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
for word in words:
    #replaces every instance of one string with another
    story = story.replace(word, answers[word])

print(story)