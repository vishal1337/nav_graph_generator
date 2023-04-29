import os

directory_path = '/Users/nbt1736/Development/code/work/pnb-merchant-app-lending/fldgbusinessloans/src/main/java/com/bnb/paynearby/fldgbusinessloans/centrum'  # replace with your directory path
output_file_path = 'file.txt'  # replace with your desired output file path
package_name = 'com.bnb.paynearby.fldgbusinessloans.centrum'  # replace with your desired output file path
default_label = '@string/lbl_business_loans' # In Case it is same for all
default_layout = '@layout/fragment_business_loans_landing'


java_path = "/Users/nbt1736/Development/code/work/pnb-merchant-app-lending/fldgbusinessloans/src/main/java/"

def main():
    generateTemplate()
    # roughWork()

#### Business Logic [start]
def generateTemplate():
    # open the output file in write mode
    with open(output_file_path, 'w') as output_file:
        # loop through all files in the directory and its subdirectories
        for root, dirs, files in os.walk(directory_path):
            # write the full path of each file to the output file
            for file in files:
                if file.endswith('Fragment.kt'):
                    # output_file.write(get_organised_path(os.path.join(root, file)) + "\n")
                    output_file.write(f'<fragment\n\tandroid:id="@+id/{first_char_to_lower(remove_substring(file,"Fragment.kt"))}Screen"\n\tandroid:name="{get_organised_path(os.path.join(root, remove_substring(file,".kt")))}"\n\tandroid:label="{default_label}"\n\ttools:layout="{default_label}">\n</fragment>' + '\n')

def first_char_to_lower(s):
    if not s:
        return ''
    return s[0].lower() + s[1:]

def remove_substring(s, substring):
    if not s:
        return ''
    return s.replace(substring, '')

def get_organised_path(str):
    return get_string_from_match(str.replace("/", "."), package_name)

def get_string_from_match(s, match_str):
    if not s:
        return ''
    index = s.find(match_str)
    if index == -1:
        return ''
    return s[index:]

#### Business Logic [end]


#Rough Work. Todo : Remove me later

def roughWork():
    print("Something Important")

#Rough Work. end.

if __name__ == '__main__':
        main()