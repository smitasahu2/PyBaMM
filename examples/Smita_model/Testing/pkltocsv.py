import pickle        
import base64
import csv

# your_pickle_obj = pickle.loads(open('SEI_Solo125e20.pkl', 'rb').read())
# with open('output.csv', 'a', encoding='utf8') as csv_file:
#     wr = csv.writer(csv_file, delimiter='|')
#     pickle_bytes = pickle.dumps(your_pickle_obj)            # unsafe to write
#     b64_bytes = base64.b64encode(pickle_bytes)  # safe to write but still bytes
#     b64_str = b64_bytes.decode('utf8')          # safe and in utf8
#     wr.writerow(['col1', 'col2', b64_str])


import pickle
import csv

# Load the PKL file
with open('SEI_Solo125e20.pkl', 'rb') as f:
    data = pickle.load(f)

# Extract the data
header = ['column1', 'column2', 'column3']
rows = [[row['column1'], row['column2'], row['column3']] for row in data]

# Convert the data to CSV format
csv_data = [header] + rows

# Write the CSV data to a new file
with open('SEI_Solo125e20.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
