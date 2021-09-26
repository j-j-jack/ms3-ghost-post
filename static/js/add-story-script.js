window.addEventListener("DOMContentLoaded", (event) => {
  for (let country in countries) {
    document.getElementsByClassName(
      "country-selector"
    )[0].innerHTML += `<option value="${countries[country].name}">${countries[country].name}</option>`;
  }
});
