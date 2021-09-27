/* This page is used to prompt the user with a confirmation that they want to delete a story
when they click the delete button */
function deleteStory(story) {
  if (window.confirm("Are you sure you want to delete this story?")) {
    window.location.href = story;
  }
}
