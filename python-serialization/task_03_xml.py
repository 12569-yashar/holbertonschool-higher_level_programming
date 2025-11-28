#!/usr/bin/python3
"""Serialization"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """salam"""
    # Create root element
    root = ET.Element("data")

    # Add child elements for each dictionary item
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert value to string

    # Write XML tree to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """sashbass"""

    tree = ET.parse(filename)
    root = tree.getroot()

    data_dict = {}
    for child in root:
        data_dict[child.tag] = child.text  # All values will be strings

    return data_dict
