/* This script is used to simply change the background color of the flashMessage container if
there is a flash message being displayed */
window.addEventListener("DOMContentLoaded", (event) => {
  let flashMessage = document.getElementsByClassName("flash-message")[0];
  if (flashMessage.innerHTML == "") {
  } else {
    flashMessage.style.background = "rgb(153, 125, 189)";
  }
});
