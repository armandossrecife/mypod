import requests

# Fetch the interview text from the URL
url = "https://raw.githubusercontent.com/armandossrecife/teste/main/ipek.txt"
response = requests.get(url)
my_text = response.text

# Count the number of words in the text
words = my_text.split()
num_words = len(words)

# Count the number of occurrences of "Technical debt"
count_term = my_text.count("technical debt")

# Print the result
print(f"The file contains {num_words} words.")
print(f"The term 'Technical debt' appears {count_term} times in the interview.")