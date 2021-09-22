window.addEventListener('DOMContentLoaded', (event) => {
    let logoutBox=document.getElementsByClassName("logout-box")[0];
    logoutBox.addEventListener("click", function(){
        let logoutButton = document.getElementById("logout-button");
        logoutButton.click();
    });

    let logoutBoxSmall=document.getElementsByClassName("logout-box-small")[0];
    logoutBoxSmall.addEventListener("click", function(){
        let logoutButtonSmall = document.getElementById("logout-button-small");
        logoutButtonSmall.click();
    });

    let searchIconOne = document.getElementsByClassName('search-icon')[0];
    searchIconOne.addEventListener('click', function(){
      let searchSubmissionOne=document.getElementsByClassName('search-submission')[0];
      searchSubmissionOne.click();
    })

    let searchIconTwo = document.getElementsByClassName('search-icon')[1];
    searchIconTwo.addEventListener('click', function(){
      let searchSubmissionTwo=document.getElementsByClassName('search-submission')[1];
      searchSubmissionTwo.click();
    })
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


