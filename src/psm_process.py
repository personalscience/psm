# psm_process.py:  process Joplin "PSM" notes 

import os
import sys



from joplinexport import get_save_path, notebook_handling, note_handling

# Define the directory where you want to download the notes

# resource_id_to_file_path_main = {}
# note_id_to_title_main = {} # Initialize an empty dictionary outside save_note_to_file

JOINED_FILENAME = "notes.qmd" # f"all_{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"


def main(notebook_name):
    save_path = get_save_path("downloads")
     # check if save_path directory exists, if not create it
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    notebook_handling.export_notebook(notebook_name, frontmatter=False)
       # Check if the directory exists
    if not os.path.isdir(save_path):
        print(f"Error: Directory not found: {save_path}")
        sys.exit(1)


    # Convert all .md files to .qmd
    for filename in os.listdir(save_path):
        base_file, ext = os.path.splitext(filename)
        if ext == ".md":
            os.rename(os.path.join(save_path, filename), os.path.join(save_path, base_file + ".qmd"))


    print(f"Output written to directory: {save_path}")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python psm_process.py <notebook_name>")
    else:
        main(sys.argv[1])
