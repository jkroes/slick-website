Steps to create this website:
```
D:
cd Scripts\R
hugo new site slick-website
git init
# commit
git submodule add https://github.com/jkroes/slick themes/slick
# commit
# Add example content from theme
# commit
hugo server -D
# View http://localhost:1313/
hub create slick-website
# git config --list
## Note that the remote is added by hub as ssh instead of https
## Check out git config --global hub.protocol https
git remote set-url origin https://github.com/jkroes/slick-website 
git push -u origin master
# Add repository to Netlify
# Set baseURL to Netlify URL
# Continue making and pushing changes
```