window.addEventListener('DOMContentLoaded', (event) => {
    for(country in countries){
        document.getElementsByClassName("country-selector")[0].innerHTML += `<option value="${countries[country].name}">${countries[country].name}</option>`
    }});