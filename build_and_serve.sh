#!/bin/bash

# Path to the Python script
PYTHON_SCRIPT="layouts/section/generate_html_from_bib.py"
# Path to the BibTeX file
BIB_FILE="content/publication/publications.bib"
# Output HTML file
OUTPUT_HTML="layouts/section/publications.html"

# Function to regenerate the HTML
regenerate_html() {
    python3 $PYTHON_SCRIPT $BIB_FILE $OUTPUT_HTML
}

# Initial generation
regenerate_html

# Run Hugo server
hugo server --ignoreCache -D
