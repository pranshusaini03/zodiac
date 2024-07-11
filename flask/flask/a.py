import csv
def read_dataset():
    dataset = []
    with open('zoDATA.csv', 'r', newline='') as file:  # Replace 'zodiac_dataset.csv' with 'zoDATA.csv'
        reader = csv.DictReader(file)
        for row in reader:
            dataset.append(row)
    return dataset
def calculate_compatibility(user_zodiac, partner_zodiac, dataset):
    compatibility_score = 0
    for row in dataset:
        if row['Zodiac Sign'] == user_zodiac:
            partner_zodiac = row['Compatible Signs'].split(', ')
            compatibility_score=row['Compatibility Score']
            break
    return compatibility_score
a=read_dataset()
b='Sagittarius'
c='Aries'
print(calculate_compatibility(c, b, a))