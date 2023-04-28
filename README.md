# vcf_to_txt
Description:

This Python script parses contact information from VCF (vCard) files and exports the data to a plain text file. It processes each contact's name and phone number, and supports decoding Quoted-Printable encoded names. The exported text file contains contact names and phone numbers in a readable format.

Features:

Parses VCF (vCard) files containing contact information
Supports Quoted-Printable encoded names
Exports contact names and phone numbers to a plain text file
Usage:

Place your VCF file in the same directory as the script and name it 'contacts.vcf'
Run the script using the command python main.py
The parsed contacts will be saved in a new file called 'contacts.txt' in the same directory
Requirements:

Python 3.x
Note: This script has been tested with standard VCF files. However, VCF files may vary depending on the source or application used to create them. Modifications to the script may be required to accommodate different VCF file structures.