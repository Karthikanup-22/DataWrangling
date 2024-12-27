import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("employees")

employee1 = ET.SubElement(root, "employee")
name1 = ET.SubElement(employee1, "name")
name1.text = "kiran"
age1 = ET.SubElement(employee1, "age")
age1.text = "222"

employee2 = ET.SubElement(root, "employee")
name2 = ET.SubElement(employee2, "name")
name2.text = "mathew"
age2 = ET.SubElement(employee2, "age")
age2.text = "3333"

tree = ET.ElementTree(root)
with open("rrr.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)
