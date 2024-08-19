# Weekly Perks Email Compiler
## Overview
This project includes a Python script (compile.py) designed to automate the process of compiling an HTML email template from multiple HTML snippet files. The script replaces specific variables within these HTML files with test content defined in a build.txt file. Once the variables are replaced, the script merges all the HTML snippets into a single output HTML file that can be used for email test sends.

## How It Works
### compile.py
The compile.py script reads a list of HTML files and their corresponding test content from a build.txt file. It replaces placeholder variables in the HTML files with the test content and compiles them into a single output HTML file.

Placeholder variables within the HTML files are identified by a unique syntax: <| variablename |>. These variables are replaced with the corresponding content provided in the build.txt file.

## build.txt
### The build.txt file specifies the HTML files to be included in the compiled email, along with the variables and their replacement content.

Each HTML file is referenced by its file path. Following the file path, each variable within that file is listed with the content it should be replaced by. If an HTML file needs to be included multiple times with different content, it can be referenced multiple times in the build.txt file.

## How to Run the Script
### Prerequisites
* Python 3.x installed on your system
* Basic knowledge of using the command line

### Running the Script
* Open Terminal and navigate to your project directory: `cd /path/to/your/project`
* Ensure your build.txt file and HTML snippet files are in the correct location as referenced in the script.
* Run the script by executing: `python3 compile.py`
* The compiled email will be saved as `compiled_email.html` in your project directory.

## Troubleshooting
If you encounter a ValueError related to variable replacement, ensure that your build.txt file is correctly formatted with variables and their corresponding content. Ensure all HTML files referenced in build.txt are present in the specified paths.
