window.addEventListener('DOMContentLoaded', (event) => {
    let flashMessage = document.getElementsByClassName("flash-message")[0];
    if(flashMessage.innerHTML == ""){
        console.log('flash');
    }
    else{
        flashMessage.style.background = "rgb(153, 125, 189)";
    }
});