window.addEventListener('DOMContentLoaded', (event) => {
    let userCountry = document.getElementsByClassName("country-receiver-div")[0].innerHTML;
    console.log(userCountry)
    for(country in countries){
        if(userCountry == countries[country].name){
            document.getElementsByClassName(
            "country-selector")[0].innerHTML 
            += `<option value="${countries[country].name}" selected>${countries[country].name}</option>`
        }
        else{
        document.getElementsByClassName(
            "country-selector")[0].innerHTML 
            += `<option value="${countries[country].name}">${countries[country].name}</option>`
        }
    }
    });