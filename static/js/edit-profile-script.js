/* This array is used as the src of the profile picture options when the user clicks
the left and right arrows */
let profilePictures = [
  "/static/images/profile-1.jpg",
  "/static/images/profile-2.jpg",
  "/static/images/profile-3.jpg",
  "/static/images/profile-4.jpg",
  "/static/images/profile-5.jpg",
  "/static/images/profile-6.jpg",
  "/static/images/profile-7.jpg",
  "/static/images/profile-8.jpg",
  "/static/images/profile-9.jpg",
  "/static/images/profile-10.jpg",
  "/static/images/profile-11.jpg",
  "/static/images/profile-12.jpg",
];

/* The following array is a list of alt attributes which are changed as the user cycles 
through the profile picture options */
let altTags = [
  "a spooky ghost-like figure standing in a dimly lit area",
  "a fairy woman standing in the forest wrapped in leaves",
  "a female vampire with blood dripping from her lips",
  "a statue of an angel in a graveyard shrouded in mist",
  "a white eyed demon completely covered in long brown hair with the horns of a goat",
  `a depiction of an alien creature with a large cranium 
    causing a metallic sphere to float above his hand in mid air`,
  "a female demon looking upwards with goat horns and a feathered head dress",
  `a hooded wizard holding his hand so as to conceal his face. 
    smoke is streaming from his hand to add a further layer of concealment`,
  `a demon like creature coverdd in mud. 
    there are chains around his neck and he is holding the lock in his hand`,
  "a zombie with blood dripping from its mouth down onto its shirt",
  "a mysterious hooded entity standing outside in orange light",
  `a picture of a time laspe of a person in turmoil. 
    in various parts of the picture they can be seen chewing their hands and crying out in agony`,
];

window.addEventListener("DOMContentLoaded", () => {
  /* This variable passed to the html page from the app and contained in a hidden div
  it is used to preselect their current avatar in the carousel */
  let avatarNumber = parseInt(
    document.getElementsByClassName("avatar-receiver-div")[0].innerHTML
  );
  /* 1-12 = 0-11 index in array */
  avatarNumber = avatarNumber - 1;
  let currentPictureSelected = avatarNumber;
  /* Again the currently selected country is passed from the app to the html and contained
  in a hidden div */
  let userCountry = document.getElementsByClassName("country-receiver-div")[0]
    .innerHTML;

  /* Populating the location dropdown using the countries variable in the  */
  for (let country in countries) {
    if (userCountry == countries[country].name) {
      document.getElementsByClassName(
        "country-selector"
      )[0].innerHTML += `<option value="${countries[country].name}" selected>${countries[country].name}</option>`;
    } else {
      document.getElementsByClassName(
        "country-selector"
      )[0].innerHTML += `<option value="${countries[country].name}">${countries[country].name}</option>`;
    }
  }

  /* currentPictureSelected is used to hide the left and right arrows if the user reaches either end
  of the options. It is also used to set the src and alt attributes on the page */
  if (currentPictureSelected > 0) {
    document.getElementsByClassName("picture-left-arrow")[0].style.visibility =
      "visible";
    document.getElementsByClassName(
      "picture-left-arrow"
    )[0].style.pointerEvents = "auto";
  } else {
    document.getElementsByClassName("picture-left-arrow")[0].style.visibility =
      "hidden";
    document.getElementsByClassName(
      "picture-left-arrow"
    )[0].style.pointerEvents = "none";
  }

  if (currentPictureSelected < 11) {
    document.getElementsByClassName("picture-right-arrow")[0].style.visibility =
      "visible";
    document.getElementsByClassName(
      "picture-right-arrow"
    )[0].style.pointerEvents = "auto";
  } else {
    document.getElementsByClassName("picture-right-arrow")[0].style.visibility =
      "hidden";
    document.getElementsByClassName(
      "picture-left-arrow"
    )[0].style.pointerEvents = "none";
  }

  document.getElementsByClassName("selected-picture")[0].src =
    profilePictures[currentPictureSelected];
  document.getElementsByClassName("selected-picture")[0].alt =
    altTags[currentPictureSelected];
  /* The hidden radio buttons must also be changed so that when the form is posted the app can
  read the user's profile picture choice */
  let radioButton = "profile-radio-" + (currentPictureSelected + 1);
  document.getElementById(radioButton).checked = true;

  document
    .getElementsByClassName("picture-right-arrow")[0]
    .addEventListener("click", function () {
      currentPictureSelected += 1;
      document.getElementsByClassName(
        "picture-left-arrow"
      )[0].style.visibility = "visible";
      document.getElementsByClassName(
        "picture-left-arrow"
      )[0].style.pointerEvents = "auto";
      if (currentPictureSelected >= 11) {
        currentPictureSelected = 11;
        document.getElementsByClassName(
          "picture-right-arrow"
        )[0].style.visibility = "hidden";
        document.getElementsByClassName(
          "picture-right-arrow"
        )[0].style.pointerEvents = "none";
      }
      document.getElementsByClassName("selected-picture")[0].src =
        profilePictures[currentPictureSelected];
      let radioButton = "profile-radio-" + (currentPictureSelected + 1);
      document.getElementById(radioButton).checked = true;
    });

  document
    .getElementsByClassName("picture-left-arrow")[0]
    .addEventListener("click", function () {
      currentPictureSelected -= 1;
      document.getElementsByClassName(
        "picture-right-arrow"
      )[0].style.visibility = "visible";
      document.getElementsByClassName(
        "picture-right-arrow"
      )[0].style.pointerEvents = "auto";
      if (currentPictureSelected <= 0) {
        currentPictureSelected = 0;
        document.getElementsByClassName(
          "picture-left-arrow"
        )[0].style.visibility = "hidden";
        document.getElementsByClassName(
          "picture-left-arrow"
        )[0].style.pointerEvents = "none";
      }
      document.getElementsByClassName("selected-picture")[0].src =
        profilePictures[currentPictureSelected];
      let radioButton = "profile-radio-" + (currentPictureSelected + 1);
      document.getElementById(radioButton).checked = true;
    });
});
