import xml.etree.ElementTree as ET

xml_data = """
<employees>
    <employee>
        <name>Alice</name>
        <age>25</age>
    </employee>
    <employee>
        <name>Bob</name>
        <age>30</age>
    </employee>
</employees>
"""

# Parse the XML string
root = ET.fromstring(xml_data)

for employee in root.findall('employee'):
    name = employee.find('name').text
    age = employee.find('age').text
    print(f"Name: {name}, Age: {age}")
