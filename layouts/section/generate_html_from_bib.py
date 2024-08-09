import os
import html
import re
import bibtexparser


# Define paths
bib_dir = os.path.abspath("../../content/publication/")
bib_file = os.path.join(bib_dir, 'publications.bib')
html_file = 'publications_list.html'
layout_file = 'publications_page_layout.html'
output_file = 'publications.html'

def clean_title(title):
    """Remove braces from the title while preserving the content."""
    if not title:
        return title
    # Remove braces around content but keep the content itself
    title = re.sub(r'\{([^\{\}]*)\}', r'\1', title)
    # Remove any leftover braces or extra spaces
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def generate_html_from_bib(bib_file, html_file):
    """Generate HTML from a BibTeX file, grouping by year."""
    try:
        # Read the .bib file
        with open(bib_file) as f:
            bib_database = bibtexparser.load(f)
    except FileNotFoundError:
        print(f"Error: The file {bib_file} was not found.")
        return
    except Exception as e:
        print(f"Error reading {bib_file}: {e}")
        return

    try:
        # Group entries by year
        grouped_entries = {}
        for entry in bib_database.entries:
            year = entry.get('year', 'Unknown year')
            if year not in grouped_entries:
                grouped_entries[year] = []
            grouped_entries[year].append(entry)
        
        # Sort the years in descending order
        sorted_years = sorted(grouped_entries.keys(), reverse=True)

        # Write the HTML file
        with open(html_file, 'w') as f:
            f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
            f.write('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
            f.write('<title>Publications</title>\n<link rel="stylesheet" href="path/to/bootstrap.min.css">\n')
            f.write('<link rel="stylesheet" href="path/to/your-custom-styles.css">\n</head>\n<body>\n')
            f.write('<div class="container mt-5">\n<div id="accordion">\n')

            # Generate HTML for each year
            for year in sorted_years:
                entries = grouped_entries[year]
                unique_id = f"year_{year}"

                # Write HTML for the year tab
                f.write(f'<div class="card">\n')
                f.write(f'<div class="card-header year-title-bg" role="tab" id="heading{unique_id}">\n')
                f.write(f'<h5 class="mb-0">\n')
                f.write(f'<a data-toggle="collapse" data-parent="#accordion" href="#collapse{unique_id}" aria-expanded="false" aria-controls="collapse{unique_id}">\n')
                f.write(f'<span class="year-title">{year}</span>\n')
                f.write(f'</a>\n</h5>\n</div>\n')

                f.write(f'<div id="collapse{unique_id}" class="collapse" role="tabpanel" aria-labelledby="heading{unique_id}">\n')
                f.write(f'<div class="card-body">\n')

                # Write HTML for each publication in the year
                for entry in entries:
                    title = clean_title(entry.get('title', 'No title'))
                    authors = html.escape(entry.get('author', 'No authors'))
                    journal = html.escape(entry.get('journal', 'No journal'))
                    volume = html.escape(entry.get('volume', ''))
                    pages = html.escape(entry.get('pages', ''))
                    url = html.escape(entry.get('url', '#'))

                    f.write(f'<div class="col-md-9">\n')
                    f.write(f'<p><a href="{url}"><strong>{title}</strong></a></p>\n')
                    f.write(f'<p>{authors}</p>\n')
                    f.write(f'<p><em>{journal}. {year} {volume}: {pages}. </em></p>\n')
                    f.write(f'</div>\n<hr>\n')

                f.write(f'</div>\n</div>\n</div>\n')

            # Close the HTML tags
            f.write('</div>\n</div>\n</body>\n</html>')
    except Exception as e:
        print(f"Error writing {html_file}: {e}")

# Example usage
generate_html_from_bib('your_bib_file.bib', 'output.html')


def update_publications_page_layout(publications_file, layout_file, output_file):
    """Update the layout with the generated publications content."""
    try:
        with open(publications_file, 'r') as f:
            publications_content = f.read()
        
        with open(layout_file, 'r') as f:
            layout_content = f.read()
        
        updated_content = layout_content.replace('<!-- Include the HTML content from publications.html here -->', publications_content)
        
        with open(output_file, 'w') as f:
            f.write(updated_content)
            print(f"Updated content written to {output_file}.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error updating layout: {e}")

# Call the functions
generate_html_from_bib(bib_file, html_file)
update_publications_page_layout(html_file, layout_file, output_file)
