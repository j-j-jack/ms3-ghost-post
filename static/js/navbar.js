window.addEventListener("DOMContentLoaded", (event) => {
  /* The code below is used to underline the correct link in the nav
  based on the page title of the page the user is currently viewing */
  let pageTitle = document.getElementsByTagName("title")[0].innerHTML;
  let addStoryBox = document.getElementsByClassName("add-story-box")[0];
  let addStoryBoxSmall = document.getElementsByClassName(
    "add-story-box-small"
  )[0];
  let feedBox = document.getElementsByClassName("feed-box")[0];
  let feedBoxSmall = document.getElementsByClassName("feed-box-small")[0];
  let profileBox = document.getElementsByClassName("profile-box")[0];
  let profileBoxSmall = document.getElementsByClassName("profile-box-small")[0];

  if (pageTitle == "Add Story") {
    addStoryBox.style.textDecoration = "underline";
    addStoryBoxSmall.style.textDecoration = "underline";
  } else if (pageTitle == "Feed") {
    feedBox.style.textDecoration = "underline";
    feedBoxSmall.style.textDecoration = "underline";
  } else if (pageTitle == "Profile") {
    profileBox.style.textDecoration = "underline";
    profileBoxSmall.style.textDecoration = "underline";
  }

  /* This code is used to click the logout button which is hidden from view  */
  let logoutBox = document.getElementsByClassName("logout-box")[0];
  logoutBox.addEventListener("click", function () {
    let logoutButton = document.getElementById("logout-button");
    logoutButton.click();
  });
  /* ditto for the small screen navbar */
  let logoutBoxSmall = document.getElementsByClassName("logout-box-small")[0];
  logoutBoxSmall.addEventListener("click", function () {
    let logoutButtonSmall = document.getElementById("logout-button-small");
    logoutButtonSmall.click();
  });

  /* The code below is used to click the hidden search button when the user clicks the 
  search icon */
  let searchIconOne = document.getElementsByClassName("search-icon")[0];
  searchIconOne.addEventListener("click", function () {
    let searchSubmissionOne =
      document.getElementsByClassName("search-submission")[0];
    searchSubmissionOne.click();
  });

  /* ditto for the small screen navbar */
  let searchIconTwo = document.getElementsByClassName("search-icon")[1];
  searchIconTwo.addEventListener("click", function () {
    let searchSubmissionTwo =
      document.getElementsByClassName("search-submission")[1];
    searchSubmissionTwo.click();
  });

  /* both the burger icon and the x icon are used to toggle the small screen
  navbar dropdown open and closed using the jquery toggle function */
  $("#burger-icon").click(function () {
    $("#navbar-container-small").toggle("medium");
  });
  $("#x-icon").click(function () {
    $("#navbar-container-small").toggle("medium");
  });

  /* The mediaquery is used inside javascript as it is necessary to check if the menu is
  open or not. The menu display is set to none if it is open and the screen size changes
  to being too large */
  const mediaQuery = window.matchMedia("(min-width: 992px)");
  // https://css-tricks.com/working-with-javascript-media-queries/

  function handleTabletChange(e) {
    // Check if the media query is true
    if (e.matches) {
      let smallScreenNavbar = document.getElementById("navbar-container-small");
      if (smallScreenNavbar.style.display != "none") {
        smallScreenNavbar.style.display = "none";
      }
    }
  }
  // Register event listener
  mediaQuery.addEventListener("change", handleTabletChange);
});
