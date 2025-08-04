#!/usr/bin/env python3
"""
Convert CSV to Excel format using only standard library
Creates a simple Excel-compatible file
"""

import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom

def csv_to_excel_xml(csv_file, excel_file):
    """Convert CSV to Excel XML format"""
    
    # Read CSV data
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    # Create XML structure for Excel
    workbook = ET.Element('Workbook', {
        'xmlns': 'urn:schemas-microsoft-com:office:spreadsheet',
        'xmlns:o': 'urn:schemas-microsoft-com:office:office',
        'xmlns:x': 'urn:schemas-microsoft-com:office:excel',
        'xmlns:ss': 'urn:schemas-microsoft-com:office:spreadsheet',
        'xmlns:html': 'http://www.w3.org/TR/REC-html40'
    })
    
    # Add styles
    styles = ET.SubElement(workbook, 'Styles')
    style = ET.SubElement(styles, 'Style', {'ss:ID': 'Header'})
    font = ET.SubElement(style, 'Font', {'ss:Bold': '1'})
    
    # Create worksheet
    worksheet = ET.SubElement(workbook, 'Worksheet', {'ss:Name': 'Dataset'})
    table = ET.SubElement(worksheet, 'Table')
    
    # Add header row
    header_row = ET.SubElement(table, 'Row')
    for cell_value in data[0]:
        cell = ET.SubElement(header_row, 'Cell', {'ss:StyleID': 'Header'})
        data_elem = ET.SubElement(cell, 'Data', {'ss:Type': 'String'})
        data_elem.text = str(cell_value)
    
    # Add data rows
    for row_data in data[1:]:
        row = ET.SubElement(table, 'Row')
        for cell_value in row_data:
            cell = ET.SubElement(row, 'Cell')
            if cell_value == '':
                # Empty cell
                data_elem = ET.SubElement(cell, 'Data', {'ss:Type': 'String'})
                data_elem.text = ''
            else:
                # Try to determine if it's a number
                try:
                    float(cell_value)
                    data_elem = ET.SubElement(cell, 'Data', {'ss:Type': 'Number'})
                    data_elem.text = str(cell_value)
                except ValueError:
                    data_elem = ET.SubElement(cell, 'Data', {'ss:Type': 'String'})
                    data_elem.text = str(cell_value)
    
    # Write to file
    xml_str = ET.tostring(workbook, encoding='unicode')
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent='  ')
    
    with open(excel_file, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)

def main():
    print("📊 Converting CSV to Excel format...")
    
    csv_file = "data/dataset.csv"
    excel_file = "data/dataset.xlsx"
    
    try:
        csv_to_excel_xml(csv_file, excel_file)
        print(f"✅ Successfully converted {csv_file} to {excel_file}")
        print("💡 This creates an Excel XML format that can be opened by Excel")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        print("💡 The CSV file is still available for testing")

if __name__ == "__main__":
    main()