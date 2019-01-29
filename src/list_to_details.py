import __main__ as main
from bs4 import BeautifulSoup, Tag
import bs4
import os

# List directories in current dir on netlify when building for debugging
# print(os.listdir('.'))

# Set working dir for interactive use of this script. Note that path in
# os.chdir() may need to be tweaked based on this file's location:
if not hasattr(main, '__file__'):
    import os
    os.chdir('/Users/justinkroes/Scripts/R/slick-website')

# Read .html into DOM tree ('soup')
with open('public/misc/resources/index.html', 'r', encoding="utf-8") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc)

# Parse DOM tree to replace unordered list with collapsible list
for box in soup.find_all('div', class_='l-box'):
    ''' Notice how extract removes content from each contents list, meaning
    the index shifts need to be accounted for '''
    box.ul.replaceWithChildren()  # Rm the outer <ul>
    for li in box.find_all('li'):
        extra_p = li.find_all('p')
        for p in extra_p:  # Rm unwanted <p> tags added by footnote shortcodes
            p.unwrap()
        if li.find('ul'):  # If a collpasible list element:
            # Surround text of <li> in <summary>
            summary = soup.new_tag('summary')
            summary_str = li.contents[0].extract()  # List element's text
            summary.insert(0, summary_str)
            # If footnote follows text, include in <summary>
            if li.contents[0].name == 'sup':
                fn = li.contents[0].extract()
                summary.insert(1, fn)
            li.insert(0, summary)  # Make <summary> a child of <li>
            li.ul.replaceWithChildren()  # Remove li's <ul> child
            li.name = 'details'  # Replace <li> with <details>
        else:  # If a non-collapsible list element:
            li.name = 'p'  # Replace <li> with <p>

# Overwrite original HTML file
with open('public/misc/resources/index.html', 'w', encoding="utf-8") as f:
    f.write(str(soup))

# for li in lis:
#     contents = []
#     for c in li.contents:
#         if isinstance(c, str):
#             strip_c = c.strip()  # Strip space character (e.g. newlines)
#             if strip_c:  # Remove isolated newlines
#                 contents.append(strip_c)
#         else:
#             contents.append(c)
#     li.contents = contents

# https://www.bryanklein.com/blog/hugo-python-gsheets-oh-my/
# https://www.netlify.com/docs/continuous-deployment/
# https://gohugo.io/hosting-and-deployment/hosting-on-netlify/
# https://www.netlify.com/docs/build-settings/
# https://www.netlify.com/docs/build-gotchas/#command-not-found
# https://www.netlify.com/docs/ ( see pep freeze > requirements.txt -- need to add a requirements.txt file to the base directory. Install beautifulsoup4 and python 3.6 in slick-website env)

# HTML:
# https://html.com/
# https://dev.w3.org/html5/html-author/
# https://htmlreference.io/
# http://www.htmldog.com/references/
# https://www.geeksforgeeks.org/
# https://www.freecodecamp.org/
