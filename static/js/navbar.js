window.addEventListener('DOMContentLoaded', (event) => {
    $('#burger-icon').click(function(){$('#navbar-container-small').toggle('medium')});
    $('#x-icon').click(function(){$('#navbar-container-small').toggle('medium')});
    const mediaQuery = window.matchMedia('(min-width: 992px)')
    // https://css-tricks.com/working-with-javascript-media-queries/

    function handleTabletChange(e) {
  // Check if the media query is true
  if (e.matches) {
    // Then log the following message to the console
    console.log('Media Query Matched!')
    let smallScreenNavbar=document.getElementById('navbar-container-small');
        if(smallScreenNavbar.style.display != 'none'){
            smallScreenNavbar.style.display = 'none';
        }
    }
  }
  // Register event listener
mediaQuery.addEventListener('change', handleTabletChange)

});


