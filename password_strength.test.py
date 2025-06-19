#password strength check
import re

#define a function
def password_strength(password):
    score = 0
    feedback = []

    # password must be at least 8 characters long
    if len(password) >= 8:
        score += 1
    else:
        feedback.append('Password must be at least 8 characters long.') 
    
    # password check for uppercase letter
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append('Password must contain at least one uppercase letter.')
    
    # password check for lowercase letter
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append('Password must contain at least one lowercase letter.')
    
    # password check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append('Password must contain at least one digit.')
    
    # password check for special character
    special_character = "!@#$%^&*()_+=-`~[]{}\\|;':\",./<>?" 
    if any(char in special_character for char in password):
        score += 1
    else:
        feedback.append('Password must contain at least one special character.')

    # determine password strength based on score
    if score == 5:
       strength = 'strong'
    else: 
        strength = 'Weak'
    
    return strength, feedback
#main
password = input("Enter the password:")
print(password_strength(password))


        
        
    

