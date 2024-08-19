import os

def parse_build_file(build_file_path):
    replacements = []
    current_file = None
    current_replacements = {}

    with open(build_file_path, 'r') as build_file:
        for line in build_file:
            line = line.strip()

            if line.startswith("/"):
                if current_file and current_replacements:
                    replacements.append((current_file, current_replacements))
                current_file = line
                current_replacements = {}
            elif line:
                if "=" in line:
                    variable, content = line.split("=", 1)
                    variable = variable.strip()
                    content = content.strip().strip('"')
                    current_replacements[variable] = content
                else:
                    print(f"Skipping line due to missing '=': {line}")

        if current_file and current_replacements:
            replacements.append((current_file, current_replacements))

    return replacements

def replace_variables_in_file(file_path, replacements):
    with open(file_path, 'r') as file:
        content = file.read()

    for variable, replacement in replacements.items():
        content = content.replace(variable, replacement)

    return content

def compile_email(replacements, output_file_path):
    compiled_content = ""

    for index, (file_path, replacement) in enumerate(replacements):
        file_path = os.path.join(os.getcwd(), file_path.strip("/"))
        content = replace_variables_in_file(file_path, replacement)
        
        # Optionally, add a separator or comment to indicate repeated sections
        compiled_content += f"<!-- Start of section {index + 1} from {file_path} -->\n"
        compiled_content += content + "\n"
        compiled_content += f"<!-- End of section {index + 1} from {file_path} -->\n\n"

    with open(output_file_path, 'w') as output_file:
        output_file.write(compiled_content)

if __name__ == "__main__":
    # Specify the path to your build.txt file
    build_file_path = "build.txt"
    # Define the output file for the compiled email
    output_file_path = "compiled_email.html"
    
    # Parse the build.txt file to get the list of files and their variable replacements
    replacements = parse_build_file(build_file_path)
    
    # Compile the email by replacing variables and merging files
    compile_email(replacements, output_file_path)
    
    print(f"Compiled email has been saved to {output_file_path}")
