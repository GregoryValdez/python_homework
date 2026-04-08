def hello(): # Task 1
    return 'Hello!'

def greet(name): # Task 2
    return f'Hello, {name}!'

def calc(*args): # Task 3
    match args: # Due to the fact that the number of arguments can vary, I have used "pattern matching" to determine which operation to perform.
        case (a, b):
            return a * b
        case (a, b, 'add'):
            return a + b
        case (a, b, 'divide'):
            if b == 0:
                return "You can't divide by 0!"
            return a / b
        case (a, b, 'multiply'):
            if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
                return "You can't multiply those values!"
            return a * b
        case (a, b, 'subtract'):
            return a - b
        case (a, b, 'modulo'):
            return a % b
        case (a, b, 'int_divide'): # Floor division, which divides and rounds down to the nearest whole number.
            return a // b 
        case (a, b, 'power'): # Exponentiation
            return a ** b
        case _:
            return 'Invalid operation or number of arguments.'

def data_type_conversion(value, data_type): # Task 4
    try: # Error handling 
        match data_type:
            case 'int':
                return int(value)
            case 'float':
                return float(value)
            case 'str':
                return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

def grade(*args): # Task 5
    try:
        match args:
            case(args):
                average = sum(args) / len(args)
                if average >= 90:
                    return 'A'
                elif average >= 80:
                    return 'B'
                elif average >= 70:
                    return 'C'
                elif average >= 60:
                    return 'D'
                else:
                    return 'F'
    except TypeError:
        return 'Invalid data was provided.'
    
def repeat(str, int): # Task 6
    result = ''
    for i in range(int):
        result += str # Add the string to result each iteration.
    return result
    
def student_scores(operation, **kwargs): # Task 7
    for key, value in kwargs.items():
        match operation:
            case 'mean':
                return sum(kwargs.values()) / len(kwargs)
            case 'best':
                return max(kwargs, key=kwargs.get) # Returns the key (name) with the highest value (score)
            case _:
                return 'Invalid operation'

def titleize(str): # Task 8
    exceptions = ['and', 'a', 'on', 'an', 'the', 'of', 'is', 'in'] # Words to ignore unless they are at the start or end of string.
    words = str.split()
    if not words:
        return '' # If the input string is empty, return an empty string.
    result = [] # This list will hold the processed words.
    for i, word in enumerate(words): # enumerate() provides both the word and its index (position), which is necessary to identify the first and last index positions.
        if i == 0 or i == len(words) - 1 or word not in exceptions:
            result.append(word.capitalize())
        else:
            result.append(word)
    return ' '.join(result) # Merges the list of words back into a single string with spaces in between.

def hangman(word, letters): # Task 9
    only_letters = ''.join([char for char in word if char.isalpha()]) # Removes any non-alphabetic characters from the input word.
    matches = ''.join([char if char in letters else '_' for char in only_letters]) # Creates a pattern where letters that are in the "letters" string are shown, and others are replaced with underscores.
    return matches 

def pig_latin(str): # Task 10
    def convert_word(word):
        vowels = 'aeiou'
        if word[0] in vowels:
            return word + 'ay'
        elif word.startswith('qu'):
            return word[2:] + word[:2] + 'ay'
        elif word[1:3] == 'qu': # Handles words that start with a consonant followed by "qu", such as "squeal" -> "ealsquay". It concatenates the first three letters (the consonant and "qu") to the end of the word and adds "ay".
            return word[3:] + word[:3] + 'ay' 
        else:
            for i, char in enumerate(word):
                if char in vowels:
                    return word[i:] + word[:i] + 'ay'
    words = str.split()
    return ' '.join(convert_word(word) for word in words) # Converts each word in the input string to Pig Latin and joins them back into a single string.
