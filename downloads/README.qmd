
The current version is stored in psm-quarto. Use VS Code to generate it from the "Run and Debug" menu and "Python: PSM Process"

It will download everything in the Joplin notebook "PSM", including all subdirectories. _It does not download frontmatter_

All Joplin content from "PSM" is placed in the `/downloads` directory and all file extensions converted from `.md` to `.qmd`.

Finally, the main `_book.yml` Quarto instructions tell it explicitly which of those downloaded files to attach to the final Quarto render.

Some of the Joplin-downloaded content is included under `include` statements of the appropriate other sections. The file `microbes-and-health.qmd` is made up entirely of these `include`s.



## Old
This is the (draft) Quarto edition of the  Personal Science Guide to the Microbiome, a detailed summary of how to use the Personal Science site to learn about the microbiome.

It is automatically generated with
```
quarto publish gh-pages
```

which is hooked into [Github Pages](https://github.com/personalscience/psm-quarto/settings/pages) as the branch `gh-pages`.

The final result is published here:

[https://personalscience.github.io/psm-quarto/](https://personalscience.github.io/psm-quarto/)

and a mirror copy is at https://psm.personalscience.com

