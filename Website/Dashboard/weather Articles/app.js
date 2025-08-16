const articlesContainer = document.getElementById('articles');

function sortArticlesByDate(articles) {
  return articles.sort((a, b) => {
    const dateA = new Date(a.publishedAt);
    const dateB = new Date(b.publishedAt);
    return dateB - dateA;
  });
}

function saveArticleForLater(article) {
  const savedArticles = JSON.parse(localStorage.getItem('savedArticles')) || [];
  if (!savedArticles.some((saved) => saved.url === article.url)) {
    savedArticles.push(article);
    localStorage.setItem('savedArticles', JSON.stringify(savedArticles));
    alert('Article saved for later reading!');
  } else {
    alert('This article is already saved for later reading.');
  }
}

fetch(
  'https://newsapi.org/v2/everything?q=weather&apiKey=6717596a90294dd5acdde04c0880dd41'
)
  .then((response) => response.json())
  .then((data) => {
    const sortedArticles = sortArticlesByDate(data.articles);
    sortedArticles.forEach((article) => {
      const articleElement = document.createElement('div');
      articleElement.className = 'article';

      const articleImage = document.createElement('div');
      articleImage.className = 'article-image';

      const img = document.createElement('img');
      img.src = article.urlToImage;
      articleImage.appendChild(img);

      const articleContent = document.createElement('div');
      articleContent.className = 'article-content';

      const articleTitle = document.createElement('h2');
      articleTitle.className = 'article-title';

      const titleLink = document.createElement('a');
      titleLink.href = article.url;
      titleLink.target = '_blank';
      titleLink.textContent = article.title;
      articleTitle.appendChild(titleLink);

      const articleDescription = document.createElement('p');
      articleDescription.className = 'article-description';
      articleDescription.textContent = article.description;

      const descriptionLink = document.createElement('a');
      descriptionLink.href = article.url;
      descriptionLink.target = '_blank';
      descriptionLink.appendChild(articleDescription);

      const articleDate = document.createElement('p');
      articleDate.className = 'article-date';
      const formattedDate = new Date(article.publishedAt).toLocaleString('en-US', {
        month: 'long',
        day: 'numeric',
        year: 'numeric'
      });
      articleDate.textContent = `Published on: ${formattedDate}`;

      // Add the Save for Later button
      const saveButton = document.createElement('button');
      saveButton.className = 'save-button';
      saveButton.textContent = 'Save for Later';
      saveButton.onclick = () => saveArticleForLater(article);
      articleContent.appendChild(saveButton);

      articleContent.appendChild(articleTitle);
      articleContent.appendChild(descriptionLink);
      articleContent.appendChild(articleDate);

      // Add the social sharing buttons
      const socialSharing = document.createElement('div');
      socialSharing.className = 'social-sharing';

      const facebookButton = document.createElement('a');
      facebookButton.className = 'share-button facebook';
      facebookButton.href = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(article.url)}&t=${encodeURIComponent(article.title)}`;
      facebookButton.target = '_blank';
      facebookButton.rel = 'noopener noreferrer';
      facebookButton.innerHTML = '<i class="fab fa-facebook-f"></i>';

      const twitterButton = document.createElement('a');
      twitterButton.className = 'share-button twitter';
      twitterButton.href = `https://twitter.com/intent/tweet?text=${encodeURIComponent(article.title)}&url=${encodeURIComponent(article.url)}&hashtags=news,articles`;
      twitterButton.target = '_blank';
      twitterButton.rel = 'noopener noreferrer';
      twitterButton.innerHTML = '<i class="fab fa-twitter"></i>';

      const linkedinButton = document.createElement('a');
      linkedinButton.className = 'share-button linkedin';
      linkedinButton.href = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(article.url)}`;
      linkedinButton.target = '_blank';
      linkedinButton.rel = 'noopener noreferrer';
      linkedinButton.innerHTML = '<i class="fab fa-linkedin-in"></i>';
      // Create the <img> elements for the icons
      const facebookIcon = document.createElement('img');
      facebookIcon.src = 'icons/f.png';
      const twitterIcon = document.createElement('img');
      twitterIcon.src = 'icons/T.png';
      const linkedinIcon = document.createElement('img');
      linkedinIcon.src = 'icons/in.png';

      // Append the created <i> elements to the buttons
      facebookButton.appendChild(facebookIcon);
      twitterButton.appendChild(twitterIcon);
      linkedinButton.appendChild(linkedinIcon);

      socialSharing.appendChild(facebookButton);
      socialSharing.appendChild(twitterButton);
      socialSharing.appendChild(linkedinButton);

      articleContent.appendChild(socialSharing);

      articleElement.appendChild(articleImage);
      articleElement.appendChild(articleContent);

      articlesContainer.appendChild(articleElement);
    });
  });



// Add this function to your existing app.js file
function displaySavedArticles() {
  const savedArticles = JSON.parse(localStorage.getItem('savedArticles')) || [];
  articlesContainer.innerHTML = '';

  if (savedArticles.length === 0) {
    const noSavedArticles = document.createElement('p');
    noSavedArticles.className = 'no-saved-articles';
    noSavedArticles.textContent = 'No saved articles found.';
    articlesContainer.appendChild(noSavedArticles);
  } else {
    savedArticles.forEach((article) => {
      // Reuse the existing code to display the articles
      const articleElement = document.createElement('div');
      articleElement.className = 'article';

      const articleImage = document.createElement('div');
      articleImage.className = 'article-image';

      const img = document.createElement('img');
      img.src = article.urlToImage;
      articleImage.appendChild(img);

      const articleContent = document.createElement('div');
      articleContent.className = 'article-content';

      const articleTitle = document.createElement('h2');
      articleTitle.className = 'article-title';

      const titleLink = document.createElement('a');
      titleLink.href = article.url;
      titleLink.target = '_blank';
      titleLink.textContent = article.title;
      articleTitle.appendChild(titleLink);

      const articleDescription = document.createElement('p');
      articleDescription.className = 'article-description';
      articleDescription.textContent = article.description;

      const descriptionLink = document.createElement('a');
      descriptionLink.href = article.url;
      descriptionLink.target = '_blank';
      descriptionLink.appendChild(articleDescription);

      const articleDate = document.createElement('p');
      articleDate.className = 'article-date';
      const formattedDate = new Date(article.publishedAt).toLocaleString('en-US', {
        month: 'long',
        day: 'numeric',
        year: 'numeric'
      });
      articleDate.textContent = `Published on: ${formattedDate}`;

      const saveButton = document.createElement('button');
      saveButton.className = 'save-button';
      saveButton.textContent = 'Save for Later';
      saveButton.onclick = () => saveArticleForLater(article);
      articleContent.appendChild(saveButton);

      articleContent.appendChild(articleTitle);
      articleContent.appendChild(descriptionLink);
      articleContent.appendChild(articleDate);

      articleElement.appendChild(articleImage);
      articleElement.appendChild(articleContent);

      articlesContainer.appendChild(articleElement);
    });
  }
}

// Add the event listener for the "Show Saved Articles" button
document.getElementById('show-saved-button').onclick = displaySavedArticles;
window.addEventListener("message", (event) => {
  if (event.data.toggleDarkMode) {
    document.body.classList.toggle("dark");
  }
});
