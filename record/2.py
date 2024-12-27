import csv

def read_csv_as_dict(filename, delimiter=',', quotechar='"'):
  """Reads a CSV file as a list of dictionaries.

  Args:
    filename (str): The name of the CSV file.
    delimiter (str, optional): The delimiter used in the CSV file. Defaults to ','.
    quotechar (str, optional): The quote character used in the CSV file. Defaults to '"'.

  Returns:
    list: A list of dictionaries, where each dictionary represents a row in the CSV file.
  """

  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
    data = []
    for row in reader:
      data.append(row)
    return data

# Example usage:
filename = 'your_data.csv'
data = read_csv_as_dict(filename)
print(data)