/* Mimic behavior of position: sticky */
window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

/*
https://vincenttam.gitlab.io/post/2018-09-17-fix-hugo-table-of-contents/
Note that the output index.html files will have the same extraneous top-level
ul and li elements, but differ in terms of whether the script code is included, 
when alternately commenting and uncommenting the script below. Open the
files in a browser to see that extraneous bullets/indentation have been 
stripped by the script when it's included.
*/
(function() {
  var toc = document.getElementById('TableOfContents');
  if (!toc) return;
  do {
    var li, ul = toc.querySelector('ul');
    if (ul.childElementCount !== 1) break;
    li = ul.firstElementChild;
    if (li.tagName !== 'LI') break;
    // remove <ul><li></li></ul> where only <ul> only contains one <li>
    ul.outerHTML = li.innerHTML;
  } while (toc.childElementCount >= 1);
})();