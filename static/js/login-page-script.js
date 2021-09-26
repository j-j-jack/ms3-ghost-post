window.addEventListener("DOMContentLoaded", (event) => {
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
