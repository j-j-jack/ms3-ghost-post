window.addEventListener('DOMContentLoaded', (event) => {
    document.getElementsByClassName("login-title-box")[0].addEventListener('click', function(){
        let loginBox = document.getElementsByClassName('login-box-small')[0];
        loginBox.style.display = 'block';
        let registerBox = document.getElementsByClassName('register-box-small')[0];
        registerBox.style.display = 'none';
    })

    document.getElementsByClassName("register-title-box")[0].addEventListener('click', function(){
        let loginBox = document.getElementsByClassName('login-box-small')[0];
        loginBox.style.display = 'none';
        let registerBox = document.getElementsByClassName('register-box-small')[0];
        registerBox.style.display = 'block';
    })
});