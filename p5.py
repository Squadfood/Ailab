import csv

num_attribute = 6  # Number of attributes
a = []  # List to store data from CSV

# Open the CSV file and read its content
with open('climatee.csv', 'r') as file:
    reader = csv.reader(file)
    a = list(reader)

# Initialize hypothesis with the first positive example
hypothesis = None
for row in a:
    if row[-1] == 'yes':
        hypothesis = row[:-1]
        break

# If there's no positive example, we cannot form a hypothesis
if hypothesis is None:
    print("No positive examples in the dataset")
else:
    # Update the hypothesis based on positive examples
    for row in a:
        if row[-1] == 'yes':
            for j in range(num_attribute):
                if row[j] != hypothesis[j]:
                    hypothesis[j] = '?'

    # Print the final hypothesis
    print(hypothesis)
    print("/the maximally specific hypothesis for a given examples")
    print(hypothesis)