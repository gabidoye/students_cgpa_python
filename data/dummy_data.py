# import pandas as pd
# from faker import Faker
# from collections import defaultdict
# # # from sqlalchemy import create_engine

# fake = Faker()

# fake_data = defaultdict(list)

# for _ in range(100):
#     fake_data["first_name"].append( fake.first_name() )
#     fake_data["last_name"].append( fake.last_name() )
#     fake_data["occupation"].append( fake.job() )
#     fake_data["dob"].append( fake.date_of_birth() )
#     fake_data["country"].append( fake.country() )

# df_fake_data = pd.DataFrame(fake_data)

# df_fake_data.shape


import csv

def read_csv_to_dict(csv_file):
    # Initialize an empty dictionary
    data = {}

    # Open the CSV file
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Iterate over the rows in the CSV file
        for row in reader:
            # The first element in the row is the key, and the second element is the value
            key = row[0]
            value = row[1]
            data[key] = value

    # Return the dictionary
    return data

# Example usage
data = read_csv_to_dict('course_records.csv')
print(data)
