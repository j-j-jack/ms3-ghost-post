let profilePictures = [
    "static/images/profile-1.jpg",
    "static/images/profile-2.jpg",
    "static/images/profile-3.jpg",
    "static/images/profile-4.jpg",
    "static/images/profile-5.jpg",
    "static/images/profile-6.jpg",
    "static/images/profile-7.jpg",
    "static/images/profile-8.jpg",
    "static/images/profile-9.jpg",
    "static/images/profile-10.jpg",
    "static/images/profile-11.jpg",
    "static/images/profile-12.jpg"]
   
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
    in various parts of the picture they can be seen chewing their hands and crying out in agony`
]

let currentPictureSelected = 0;
window.addEventListener('DOMContentLoaded', (event) => {
    userCountry = document.getElementsById('country-receiver-div').innerHTML;
    console.log(userCountry)
    for(country in countries){
        document.getElementsByClassName("country-selector")[0].innerHTML += `<option value="${countries[country].name}">${countries[country].name}</option>`
    }

    document.getElementsByClassName("picture-right-arrow")[0].addEventListener('click', function(){
        currentPictureSelected += 1;
        document.getElementsByClassName("picture-left-arrow")[0].style.visibility = "visible";
        document.getElementsByClassName("picture-left-arrow")[0].style.pointerEvents = "auto";
        if(currentPictureSelected >=11){
            currentPictureSelected = 11;
            document.getElementsByClassName("picture-right-arrow")[0].style.visibility = "hidden";
            document.getElementsByClassName("picture-right-arrow")[0].style.pointerEvents = "none";
        }
        document.getElementsByClassName("selected-picture")[0].src 
            = profilePictures[currentPictureSelected];
            let radioButton = 'profile-radio-' + (currentPictureSelected + 1);
            document.getElementById(radioButton).checked = true;
    })

    document.getElementsByClassName("picture-left-arrow")[0].addEventListener('click', function(){
        currentPictureSelected -= 1;
        document.getElementsByClassName("picture-right-arrow")[0].style.visibility = "visible";
        document.getElementsByClassName("picture-right-arrow")[0].style.pointerEvents = "auto";
        if(currentPictureSelected <=0){
            currentPictureSelected = 0;
            document.getElementsByClassName("picture-left-arrow")[0].style.visibility = "hidden";
            document.getElementsByClassName("picture-left-arrow")[0].style.pointerEvents = "none";
        }
        document.getElementsByClassName("selected-picture")[0].src 
            = profilePictures[currentPictureSelected];
            let radioButton = 'profile-radio-' + (currentPictureSelected + 1);
            document.getElementById(radioButton).checked = true;
    })
});