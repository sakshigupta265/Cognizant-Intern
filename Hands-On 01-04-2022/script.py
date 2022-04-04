import re
import io

# file_name = input("Enter the name of the file: ")
file_name = 'test_file5.txt'
try:
    f = io.open(file_name, mode="r", encoding="utf-8")
    print("ACCESSING FILE:",file_name)
    with open(file_name,'r') as file:
        f = file.read()

except FileNotFoundError:
    print("FILE NOT FOUND!")

line = '='

#########################################################
# pattern 1
print(line*50)

print("PATTERN 1: PRINT ALL CURRENCY SYMBOLS")

print(line*50)

match = re.search('£', f)
if match:
    print('£ : Euro')

# python was not taking ₹ symbol 
# so I had to figure out how it was accessing the ₹ symbol
match = re.search('â‚¹', f)
if match:
    print(chr(8377),': Indian Rupee')

match = re.search('\$', f)
if match:
    print('$ : US Dollar')  

#########################################################
# pattern 2
print(line*50)

print("PATTERN 2: PRINT ALL DATES")

print(line*50)

# date_pattern = r'(\d{2}/\d{2}/(\d{2,4}))'

md = r'((0[1-9]|1[012])[/](0[1-9]|[12][0-9]|3[01])[/]\d{2,4})'
dm = r'((0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[0-2])[/]\d{2,4})'

# mm/dd/yyyy, mm/dd/yy
data_md = re.findall(md,f)

# dd/mm/yyyy, dd/mm/yy, 
data_dm = re.findall(dm,f)

# removing duplicates
data = list(set(data_md + data_dm))
for i in data:
    print(i[0])

#########################################################
# pattern 3
print(line*50)

print("PATTERN 3(i): PRINT ALL ORDERS/CARDINALITIES")

print(line*50)
order_pattern = r'\d{1,}th|\d{0,}1st|\d{0,}2nd|\d{0,}3rd'
data = re.findall(order_pattern,f)
# removing duplicates
data = list(set(data))
for i in data:
    print(i)

#########################################################
print(line*50)

print("PATTERN 3(ii): PRINT ALL ORDERS/CARDINALITIES")

print(line*50)
order_patter_words = r'(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|(four|fif|six|seven|eigh|nin)(tieth|teenth|hundredth)|tenth|eleventh|twelfth)'
data = re.findall(order_patter_words,f)
# removing duplicates
data = list(set(data))
for i in data:
    print(i[0])

#########################################################
# pattern 4
print(line*50)

print("PATTERN 4: PRINT ALL 4 LETTERED WORDS STARTING WITH A VOWEL")

print(line*50)
letter_pattern = r'(\b[AEIOUaeiou][A-Za-z]{3})'
data = re.findall(letter_pattern,f)
# removing duplicates
data = list(set(data))
for i in data:
    print(i)

file.close()

#########################################################