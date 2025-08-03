"""
 1. Reverse a String
Write a program to reverse a given string.
📌 Input: "hello" → Output: "olleh"

🔹 2. Check Palindrome
Check whether a string is a palindrome (reads the same forwards and backwards).
📌 Input: "madam" → Output: True

🔹 3. Count Vowels and Consonants
Count the number of vowels and consonants in a string.
📌 Input: "Python" → Output: Vowels: 1, Consonants: 5

str = "This is sachin sharma"
vowel = 0
consonent = 0
arr = ['a','i','e','o','u']
for char in str :
    if char in arr:
        vowel += 1
    else:
        consonent += 1
print("Vowel in string", vowel)
print("Consonent in string", consonent)

🔹 4. Remove All Duplicates
Remove all duplicate characters from a string while keeping the first occurrences.
📌 Input: "banana" → Output: "ban"

🔹 5. Count Words in a Sentence
Count the number of words in a string (sentence).
📌 Input: "I love Python programming" → Output: 4

sen = "I love Python programming"
newSen = sen.split(" ")
print(len(newSen))

🔹 6. Find the Most Frequent Character
Find the character that appears the most in the string.
📌 Input: "aabbbccccd" → Output: 'c'

🔹 7. Capitalize First Letter of Each Word
Capitalize the first letter of each word in a sentence.
📌 Input: "hello world" → Output: "Hello World"

str = "hello world this is the world of coding"
newStr = str.split(' ');
list2 = []
for cap in newStr :
    print(cap.capitalize(), end=' ')

🔹 8. Check Anagram
Check if two strings are anagrams (contain the same characters in different order).
📌 Input: "listen", "silent" → Output: True

🔹 9. Remove Punctuation from a String
Remove all punctuation characters from a string.
"""