document.querySelectorAll('.team-member').forEach(member => {
    member.addEventListener('mouseover', () => {
      member.querySelector('.social-icons').style.display = 'flex';
    });
  
    member.addEventListener('mouseout', () => {
      member.querySelector('.social-icons').style.display = 'none';
    });
  });

  window.addEventListener("message", (event) => {
    if (event.data.toggleDarkMode) {
      document.body.classList.toggle("dark");
    }
  });