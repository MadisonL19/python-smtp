import pyodbc
import xml.etree.ElementTree as ET
import urllib
from xml.dom.minidom import parse, parseString
import csv
import os

def csv_writer():
    strFile = r'C:\users\username\Desktop\csvfilename.csv'
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=servername;'
                        'Database=databasename;'
                        'Trusted_Connection=no;'
                        'UID=username;'
                         'PWD=password;')
    cursor = conn.cursor()
    sql = "SELECT * FROM sqlview"
    cursor.execute(sql)
    f = open(strFile, "w")
    csvwriter = csv.writer(f)
    try: 
        if os.path.isfile(strFile):
            os.remove(strFile)
    except PermissionError:
        pass
    head = ['Ticket No', 'Customer Id', 'Name', 'Order No', 'Po No', 'Print Date', 'MST', 'Location ID', 'Name2']
    csvwriter.writerow(head)
    for row in cursor.fetchall():
        print(row)
        csvwriter.writerow(row)

csv_writer()
