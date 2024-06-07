import pandas as pd
#
# pip install pandas openpyxl
#

# Path to your Excel file
file_path = '/data/FedRAMP-POAM.xlsm'

# For FedRAMP POAM  the header starts at Row 5 
# Header is set to 4 because headers start from row 5 (Python index starts from 0)
# Python uses zero-based indexing, so row 5 is indexed as 4.
df = pd.read_excel(file_path, header=4, engine='openpyxl')

# TO-DO: 
# - Perform any data manipulation here
# - df['new_column'] = df['existing_column'] * 2

# Save the edited file
df.to_excel('/data/FedRAMP-POAM.xlsm', index=False, engine='openpyxl')
