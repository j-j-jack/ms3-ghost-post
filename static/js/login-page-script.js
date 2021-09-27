/* This script is used to set which of the register or login box is displayed on the screen
when the user clicks the relevant div on the screen. It is only relevant on smaller screens */
window.addEventListener("DOMContentLoaded", (event) => {
  /* if the user clicks the login-title-box div the login form is displayed */
  document
    .getElementsByClassName("login-title-box")[0]
    .addEventListener("click", function () {
      let loginBox = document.getElementsByClassName("login-box-small")[0];
      loginBox.style.display = "block";
      let registerBox =
        document.getElementsByClassName("register-box-small")[0];
      registerBox.style.display = "none";
      let registerTitleBox =
        document.getElementsByClassName("register-title-box")[0];
      registerTitleBox.style.borderBottom = "2px outset black";
      this.style.borderBottom = "none";
    });
  /* if the user clicks the register-title-box div the register form is displayed */
  document
    .getElementsByClassName("register-title-box")[0]
    .addEventListener("click", function () {
      let loginBox = document.getElementsByClassName("login-box-small")[0];
      loginBox.style.display = "none";
      let registerBox =
        document.getElementsByClassName("register-box-small")[0];
      registerBox.style.display = "block";
      let loginTitleBox = document.getElementsByClassName("login-title-box")[0];
      loginTitleBox.style.borderBottom = "2px outset black";
      this.style.borderBottom = "none";
    });
});
