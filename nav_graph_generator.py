import os
import getpass
import re

directory_path = f'/Users/{getpass.getuser()}/Development/code/work/pnb-merchant-app-lending/fldgbusinessloans/src/main/java/com/bnb/paynearby/fldgbusinessloans/centrum'
directory_path_base = f'/Users/{getpass.getuser()}/Development/code/work/pnb-merchant-app-lending/fldgbusinessloans/src/main/java/com/bnb/paynearby/fldgbusinessloans/base/fragment' # all the base classes stay here
output_file_path = 'nav_graph.txt'  # replace with your desired output file path
package_name = 'com.bnb.paynearby.fldgbusinessloans.centrum'  # replace with your desired output file path
default_label = '@string/lbl_business_loans' # In Case it is same for all
default_layout = '@layout/fragment_business_loans_landing'


java_path = f"/Users/{getpass.getuser()}/Development/code/work/pnb-merchant-app-lending/fldgbusinessloans/src/main/java/"

def main():
    generate_nav_graph()

#### Business Logic [start]
def generate_nav_graph():
    # open the output file in write mode
    with open(output_file_path, 'w') as output_file:
        # loop through all files in the directory and its subdirectories
        for root, dirs, files in os.walk(directory_path):
            # write the full path of each file to the output file
            for file in files:
                if file.endswith('Fragment.kt'):
                    output_file.write(populate_nave_graph(
                        first_char_to_lower(remove_substring(file,"Fragment.kt")),
                        get_organised_path(os.path.join(root, remove_substring(file,".kt"))),
                        get_label(root, file),
                        get_layout_file_name(root, file),
                        get_screen_actions(root, file)
                    ))

def populate_nave_graph(id, package, label, layout, actions):
    return f'<fragment\n\tandroid:id="@+id/{id}Screen"\n\tandroid:name="{package}"\n\tandroid:label="{label}"\n\ttools:layout="{layout}">\n {actions} \n</fragment>' + '\n\n'

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

def get_string_after_match_until(s, match_str, end_str):
    start_index = s.find(match_str)  # Find the index of the first match
    if start_index != -1:  # If the match was found
        end_index = s.find(end_str, start_index)  # Find the index of the next comma
        if end_index != -1:  # If a comma was found
            return s[start_index+len(match_str):end_index].strip()  # Slice the string from the match until the comma and remove leading/trailing spaces
    return ''

def get_label(root, file):

    pattern = "setTitle(R.string."  # The string to match

    with open(os.path.join(root,file), "r") as infile:
        for line in infile:
            if pattern in line:
                return f'@string/{get_string_after_match_until(line, pattern, ")")}'
                break

    return default_label

def get_layout_file_name(root, file):

    pattern = "R.layout."  # The string to match

    with open(os.path.join(root,file), "r") as infile:
        for line in infile:
            if pattern in line:
                return f'@layout/{get_string_after_match_until(line, pattern, ",")}'
                break

    # If Layout file not found probably go to the Base Class
    # Define the pattern to match the BaseClass
    pattern = re.compile(r'\w*Fragment\(\)\w*')

    with open(os.path.join(root,file), "r") as file:
        matches = pattern.findall(file.read())
        if len(matches) > 0 :
            base_file_name = matches[0].replace("()","")
            abs_dir = directory_path_base + '/' + base_file_name + ".kt"
            if os.path.exists(abs_dir):
                return get_layout_file_name(directory_path_base, base_file_name + ".kt" )

    return 'null'

def get_screen_actions(root, file):

    pattern = re.compile(r'\w*Fragment.initiateFragment\w*')

    output_data = ""

    with open(os.path.join(root,file), "r") as file:
        matches = pattern.findall(file.read())
        if matches:
            for destination in set(matches):
                destination_final = destination.replace("Fragment.initiateFragment","")

                action_id = f'navigateTo{destination_final}Screen'
                action_destination = f'{first_char_to_lower(destination_final)}Screen'

                # Generate the output data
                output_data_format = '\n<action\n' \
                            '\tandroid:id="@+id/{}"\n' \
                            '\tapp:destination="@id/{}"\n' \
                            '\tapp:enterAnim="@anim/slide_in_right"\n' \
                            '\tapp:exitAnim="@anim/slide_out_left"\n' \
                            '\tapp:popEnterAnim="@anim/slide_in_left"\n' \
                            '\tapp:popExitAnim="@anim/slide_out_right" />\n' \
                            .format(action_id, action_destination)

                output_data += output_data_format
    
    return output_data

#### Business Logic [end]

if __name__ == '__main__':
        main()