window.addEventListener("DOMContentLoaded", (event) => {
  /* The location of the story that the user previously set is passed from the app to 
  a hidden div in the html */
  let userCountry = document.getElementsByClassName("country-receiver-div")[0]
    .innerHTML;
  /* The dropdown is populated using the variable in the countries.js script */
  for (let country in countries) {
    if (userCountry == countries[country].name) {
      /* if the location matches the contents of the hidden div the selected attribute is given */
      document.getElementsByClassName(
        "country-selector"
      )[0].innerHTML += `<option value="${countries[country].name}" selected>${countries[country].name}</option>`;
    } else {
      document.getElementsByClassName(
        "country-selector"
      )[0].innerHTML += `<option value="${countries[country].name}">${countries[country].name}</option>`;
    }
  }
});
