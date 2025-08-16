const body = document.querySelector("body")
sidebar = body.querySelector(".sidebar")
toggle = body.querySelector(".toggle")
searchBtn = body.querySelector(".searchbox")
modeSwitch = body.querySelector(".toggle-switch")
modeText = body.querySelector(".mode-text")
const iframe1 = document.getElementById("my-iframe-1"); // Reference to the first iframe
const iframe2 = document.getElementById("my-iframe-2"); // Reference to the second iframe
const iframe3 = document.getElementById("my-iframe-3"); // Reference to the second iframe
const mainForm = document.getElementById('main-form');
const mainSearch = document.getElementById('main-search');
const searchIframe = document.getElementById('my-iframe-1');
const navLinks = document.querySelectorAll('.sidebar ul li');





function updateActiveNavLink(targetId) {
  navLinks.forEach((link) => {
    if (link.dataset.target === targetId) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}
mainForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent the default form submission behavior

  // Access the iframe's contentWindow, search bar, and form
  const iframeWindow = searchIframe.contentWindow;
  const iframeSearchBar = iframeWindow.document.getElementById('query');
  const iframeForm = iframeWindow.document.getElementById('search');

  // Set the value of the search bar within the iframe and submit the form
  if (iframeSearchBar && iframeForm) {
    iframeSearchBar.value = mainSearch.value;
    iframeForm.dispatchEvent(new Event('submit')); // Trigger the submit event
  }
    // Scroll to the home-section element
    const homeSection = document.getElementById('home');
    if (homeSection) {
      homeSection.scrollIntoView({ behavior: 'smooth' }); // Smooth scrolling
      updateActiveNavLink('home');    
    }  
});

toggle.addEventListener("click", () => {
  sidebar.classList.toggle("close")

});
modeSwitch.addEventListener("click", () => {
  body.classList.toggle("dark")
  
  if (body.classList.contains("dark")) {
    modeText.innerText = "Light Mode"
  } else {
    modeText.innerText = "Dark Mode"
  }
  
  // Post message to iframe
  iframe1.contentWindow.postMessage({ toggleDarkMode: true }, '*');
  iframe2.contentWindow.postMessage({ toggleDarkMode: true }, "*");
  iframe3.contentWindow.postMessage({ toggleDarkMode: true }, "*");   
});

// iframe can receive this message and toggle styling
window.addEventListener("message", (e) => {
  if (e.data.toggleDarkMode) {
    document.body.classList.toggle("dark");
  }
}); 
const list = document.querySelectorAll('.nav-link');

function activelink() {
  list.forEach((item) =>
    item.classList.remove('active'));
  this.classList.add('active');
}
list.forEach((item) =>
  item.addEventListener('click', activelink));