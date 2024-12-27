from xml.dom import minidom

# Parse the XML file
doc = minidom.parse('data.xml')

employees = doc.getElementsByTagName('employee')
for employee in employees:
    name = employee.getElementsByTagName('name')[0].firstChild.data
    age = employee.getElementsByTagName('age')[0].firstChild.data
    print(f"Name: {name}, Age: {age}")
