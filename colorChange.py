import re

# Input and output file names
input_file = "input.tex"
output_file = "output.tex"

# Read the .tex file
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace \color{blue} with \color{black}
content = re.sub(r'\\color\{blue\}', r'\\color{black}', content)

# Replace \textcolor{blue}{...} with \textcolor{black}{...}
content = re.sub(r'\\textcolor\{blue\}', r'\\textcolor{black}', content)

# Optional:
# Remove "~" before \textcolor{black}
content = re.sub(r'~\\textcolor\{black\}', r'\\textcolor{black}', content)

# Write modified content
with open(output_file, "w", encoding="utf-8") as f:
    f.write(content)

print("All blue text changed to black.")
