window.addEventListener("DOMContentLoaded", (event) => {
  let checkBoxFilter = document.getElementsByClassName("checkbox-filter")[0];
  allCheckbox = document.getElementById("allCheckbox");
  /* The following if/else statement either enables or disables the user from using the checkboxes
  if the all checkbox is checked the user cannot click on the other checkboxes. A dark filter is 
  placed over the checkboxes and the cursor is changed to not-allowed to communicate this to the 
  user */
  if (allCheckBox.checked == false) {
    checkBoxFilter.style.background = "rgba(183, 216, 209, 0)";
    checkBoxFilter.style.width = "0%";
    checkBoxFilter.style.height = "0%";
    checkBoxFilter.style.cursor = "auto";
  } else {
    checkBoxFilter.style.background = "rgba(0, 0, 0, .3)";
    checkBoxFilter.style.width = "100%";
    checkBoxFilter.style.height = "100%";
    checkBoxFilter.style.cursor = "not-allowed";
  }
  document.getElementById("allCheckBox").addEventListener("click", function () {
    if (allCheckBox.checked == false) {
      checkBoxFilter.style.background = "rgba(183, 216, 209, 0)";
      checkBoxFilter.style.width = "0%";
      checkBoxFilter.style.height = "0%";
      checkBoxFilter.style.cursor = "auto";
    } else {
      checkBoxFilter.style.background = "rgba(0, 0, 0, .3)";
      checkBoxFilter.style.width = "100%";
      checkBoxFilter.style.height = "100%";
      checkBoxFilter.style.cursor = "not-allowed";
    }
  });

  /* jquery toggle function is used to toggle the filter open and closed on smaller screens */
  $("#filter-opener").click(function () {
    $("#filter-div").toggle("medium");
  });
});
