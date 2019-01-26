# Set base and change paths?
# Change build command to:
# hugo && python ./src/list_to_details.py
from bs4 import BeautifulSoup
with open('../public/misc/resources/index.html', 'r', encoding="utf-8") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')







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
