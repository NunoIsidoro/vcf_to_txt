import re
import quopri

def decode_quoted_printable(name):
    if "=" in name:
        decoded_name = quopri.decodestring(name).decode('utf-8', 'replace')
        return decoded_name
    return name

def parse_vcf(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        contacts = content.split("END:VCARD")
        parsed_contacts = []

        for contact in contacts:
            name = re.search(r'FN;?.*:(.+)', contact)
            phone = re.search(r'TEL;?.*:(.+)', contact)

            if name and phone:
                name = name.group(1).strip()
                name = decode_quoted_printable(name)
                phone = phone.group(1).strip()
                parsed_contacts.append((name, phone))
        return parsed_contacts

def export_to_txt(contacts, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for name, phone in contacts:
            file.write(f'{name}: {phone}\n')

def main():
    input_file_path = 'contacts.vcf'
    output_file_path = 'contacts.txt'

    contacts = parse_vcf(input_file_path)
    export_to_txt(contacts, output_file_path)

if __name__ == '__main__':
    main()
