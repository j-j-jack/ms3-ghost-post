![Ghost Post](resources/project-on-different-screens.PNG)

# **Ghost Post Social Media Website**
[View the live project here](https://ghost-post.herokuapp.com/) <br>
This is the documentation for the Ghost Post social media website project. Ghost Post is a social Media website where users can post stories about their paranormal encounters. Users may also interact with the site in various ways such as following  other users, display information about themselves on their profile page and favorite stories they particularly like. The primary goals of the website are to create a forum for those interested in paranormal activity, to generate a large amount of site users in order to have advertising opportunities and possibly to gather the best stories from the site and put them into a book.

## **Table of Contents**
*  **[Technologies Used](#technologies-used)**
    * [Code](#code)
    * [Languages](#languages)
    * [Frameworks and Libraries](#frameworks-and-libraries)
    * [Validators](#validators)
    * [Other Technologies Used]
*  **[UX Design](#ux-design)**
    * [Strategy Plane](#strategy-plane)
        * [Value Provided to the Business](#value-provided-to-the-business)
        * [Value Provided to the Users](#value-provided-to-the-users)
        * [B2C Considerations](#b2c-considerations)
        * [Cultural Considerations](#cultural-considerations)
        * [Business Objectives](#business-objectives)
        * [User Needs](#user-needs)
        * [Opportunities Table](#opportunities-table)
## Technologies used

### **Code**

* VSCode - to write the code for the project
* Git - used for version control 
* Github - software used to store project remotely

### **Languages**

* HTML
* CSS
* JavaScript
* Python

### **External Libraries**

* [Iconify.design](https://iconify.design/)
* JQuery
* Google Fonts
* Flask
* Pymongo
* Werkzeug.security

### **Databases**
* [MongoDB](https://www.mongodb.com/)

### **Validators**
 * [W3Schools HTML validator](https://validator.w3.org/) 
 * [W3Schools Jigsaw CSS validator](http://jigsaw.w3.org/css-validator/validator) 
 * [JSHint JavaScript validator](https://www.jshint.com/)  - The code was validated in using the jshint extension for vscode with the esversion set to esversion 6.

 ### **Other Technologies Used**

 * [Balsamiq](https://balsamiq.com/) - for creating wireframes
 * Chrome developer tools - for testing and inspecting code
 * Lighthouse - for testing performance rating of deployed site
 * [Boxy SVG Editor](https://boxy-svg.com) - for creating brand logo
 * [GIMP](https://www.gimp.org/) - for resizing images
 * responsivedesignchecker.com - for testing site responsivity

[back to contents](#table-of-contents)

## **UX Design**

### **Strategy plane**

The strategy upon which the site is built is based on the business objectives and the user needs.

#### **Value Provided to the Business**

The site provides value to the business in several ways. It allows the business the opportunity to accumulate a large amount of site users. These users can then be targeted with ads relating to paranormal activity such as ads for books, clothes and tv shows. There is also an opportunity for the site owner to curate the best stories that are posted by users on the site and place them into one or more volumes of books.

#### **Value Provided to the Users**

The site as it is currently built provides value to customers in several ways that are detailed below. The site allows users to participate and interact with others with a similar interest in the paranormal and those who claim to have had paranormal encounters. It allows users to upload and share acounts of supernatural encounters they claim to have had.

#### **B2C Considerations**

As the site is a business dealing with customers it is modeled with B2C considerations taken into account. The site uses strong branding with catchy and compelling minimal content to trigger positive emotions in the consumers that would lead them to making a 'purchase'. A purchase in this case can be considered as one of a few actions; those being signing up for the site, making a post and following other users. The branding of this site is both warm and bold to promote the spirit of the community. The images on the site are large and the content is minimal in order. Efforts have been made to ensure that the site navigation is simple and direct. These contribute to the mood of the user while using the site. This is intended to keep the users coming back to the site as well as promoting the site to their friends.

#### **Cultural Considerations**

The site is designed to be used by those in the paranormal community. This means that the site should be very user friendly with large writing and good contrast as some of the members in the community are old.

#### **Business Objectives**

When completing the strategy section of the UX design for the site the business outlined several objectives. The objectives are as follows:

* To amass site users in order to create advertising opportunities on the site in the future
* To create a collection of stories about paranormal encounters.
* To create a means of grading the popularity of the stories with the possibity of collecting the most popular stories into one or more book volumes.
* To register users for the site with a means of informing them about the books existence if it is to be released.
* Create a strong site branding so that users would recommend the site to their friends.
* Develop smaller communities for those interested in particular types of paranormal activity.
* Create a means of contacting individual members of the site
* Add a live messaging feature on the site so that users can communicate directly to one another.
* Display stories in categories

#### **User Needs**

When completing the strategy section of the UX design for the site, several user needs were identified. The needs are as follows:

* To read stories of paranormal encounters.
* To post own accounts of such stories.
* To interact with other members of the community. 
* To save favorite stories.
* To message others in the community.
* To taylor the main feed to personal preference.
* To search for particular types of encounters.
* To create a custom profile to show interests and personality
* To start groups with like minded individuals. 
* To message other users in real time.
* To sort the feed by most popular.
* To edit and delete previous posts. 
* To search for specific posts.
* To follow other users.
* To see a collection of stories from a users profile/have a record of all the posts they themselves have posted.

Using the business goals and user needs a table of opportunities was created and their importance was compared with their viability to decide which opportunities should be pursued.

#### **Opportunities Table**

| **Opportunity**                                                                    | **I** | **V** | **Y/N** | **Reasoning**                                                                                                                                                  |
|------------------------------------------------------------------------------------|-------|-------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create a method for users to register and log into the site                        | 5     | 5     | Y       | This is absolutely necessary and cannot be omitted.                                                                                                            |
| Create a method for users to upload their stories                                  | 5     | 5     | Y       | This is is part of the site's core funtionality and must be completed.                                                                                         |
| To create a method for users to edit/delete their stories                          | 5     | 5     | Y       | This is once again part of the core functionality.                                                                                                             |
| To create a main 'feed' page.                                                      | 5     | 5     | Y       | This is regarded as being part of the minimal viable product and must be pursued.                                                                              |
| Allow the users to filter the feed by the most popular/oldest and newest stories.  | 5     | 5     | Y       | This is also part of the minimal viable product                                                                                                                |
| Create a method for users to customise their feed.                                 | 3     | 2     | N       | This is somewhat important. However it could be too time consuming to complete in the initial build.                                                           |
| Allow users to save their favorite stories.                                        | 4     | 5     | Y       | This is easily achievable and should be followed through with.                                                                                                 |
| To create a method for users to search for specific posts                          | 5     | 5     | Y       | This is simple to achieve and very important for creating a good user experience.                                                                              |
| Allow users to interact with each other via comments                               | 4     | 1     | N       | Although this is a desirable feature and must be completed in a future build, it is too complicated a feature to complete for the minimal viable product.      |
| To create a means for users to customise their profiles                            | 3     | 4     | Y       | This is not as important as other features in the minimal viable product but should be achievable.                                                             |
| Add a live messaging feature                                                       | 4     | 1     | N       | This is a very difficult feature to implement and should be left out for the current build.                                                                    |
| To create a means for users to follow/unfollow other users                         | 3     | 4     | Y       | This is somewhat important but very easily implemented                                                                                                         |
| Develop a strongt and eye catching branding for the site.                          | 5     | 5     | Y       | This is crucial and should be thought carefully about in order to keep users returning to the site as well as having them recommend the site to their friends. |
| Create a method for users to start groups with other users.                        | 2     | 1     | N       | This is not very important at this stage of development and as it is very difficult to implement it should not be pursued.                                     |
| Collect users emails so that they can be contacted when the book is to be released | 5     | 5     | Y       | This is extremely simple to implement as it can be done when the users are signing up for the site.                                                            |
| **Total**                                                                          | 58    | 53    |         |                                                                                                                                                                |
| **Adjusted total disregarding opportunities to be traded off**                     | 45    | 48    |         |                                                                                                                                                                |

[back to contents](#table-of-contents)

### **Scope Plane**

#### **Site Features**

The features to be included in the site based on the tradeoffs from the strategy plane. They are as follows:

Login and register forms - These will allow the users to register for the site and to log in once they are registered.

A profile creation page - This will allow the users to finish the creation of their profile. The user should not be permitted into the site without completing the tasks from this page. 

A main feed - This will act as home page for the user and they will be presented with the stories that other users have posted.

Feed filter - This feature will be present on any page that displays stories. The filter should allow the user to filter the stories by category and to sort them from newest to oldest and by the number of favorites.

User profile pages - These pages will display the information that users have provided about themselves. It will also contain links to the users followers, following, stories and favorites.

Favorites pages - These pages will contain the favorite stories of a particular user. They will have the same layout as the feed page. 

User stories pages - These pages will contain a list of the stories written by a particular user. They will have the same layout as the feed page. 

Add story page - This page will provide the user to add a story. The form will include details such as title, category, location and content.

Edit profile page - This page will allow the user to edit any previously supplied information that they have given and has been used to create their profile.

Edit story page - This page will allow the user to edit any story that they have written.

Edit/Delete buttons - These buttons should be presented to the user on any story that they have written. The edit button should navigate the user to the edit story page and the delete button should prompt the user if they want to delete the story.

Edit profile button - This button should be present on the user's profile page and should take them to the edit profile page.

Main navigation - The main navigation will contain links to the main feed, the users profile and the add story page. It should also contain a logout button and a search bar.

Navigation for smaller screens - This feature should contain the same functionality as the main navigation but should be hidden in a dropdown accessible on smaller screens. The menu should be accessible through a dropdown icon.

Logout button - This button will be present in the navigation and should log the user out of the site. 

Search bar and search results page - A search bar should be present in the navigation and should return the results of the user's query. These results should be displayed on a search results page. This page should have the same layout as the feed page.

#### **User Stories**

User stories were created to aid in the designing of the site and in testing later on. They are as follows:

* As a new user of the site I want to be able to register and create a profile.
* As a ghosthunter I want to be able to filter the feed to only include stories about ghosts
* As somebody from Albania I want to be able to search for instance of paranormal activity in that country
* As a security conscious individual I want to ensure that I have logged out of the site after pressing the logout button
* As a witness of an angel I want to be able to write an account of this story on the site.
* As a magazine editor I want to be able to read the most popular stories on the site with the possiblity of adding one of them to my magazine.
* As a site user who has recently moved country I want to be able to edit my site profile to reflect this.
* As a sociable individual I want to be able to follow other individuals on the site.
* As a person suffering from amnesia I want to be able to edit a previous post to include newly remember details. 
* As a regular site user I want to be able to favorite any new stories that I read and enjoy.
* As somebody who has recently discovered their encounter was just a practical joke I want to be able to remove the encounter.
* As a new user I want to register for the site. 
* As a long time user of the site I want to be able to view the oldest posts on the site.

[back to contents](#table-of-contents)

### **Structure Plane** 

#### **Interaction Design**

1. Consistency - The site should remain consitant across all pages. This includes the following.
    * The navbar will remain at the top of the page and the footer at the bottom. 
    * There will be a burger icon on all pages instead of a nav-bar on smaller screen sizes. 
    * Styling will also remain consitant across all pages.
2. Predictablity -
    * All links will take the user to expected locations.
    * Clicking on the logo will take the user back to the home page as is convention. 
3. Learnability -
    * There will be active links on the navbar so that the user will know what page they are on. 
    * Pages with the same function will have the same layout to provide the user with a better sense of place and navigational possibilities. 
4. Visibility -
    * When possible as much page content for each page will be visible on each page. 
    * In situations where the content exceeds that of the screen size content hinting will be used. 
5. Feedback - There will be clear and consistant feedback given to site users -
    * Buttons that link the user to other locations will highlight when the mouse is over them.
    * For links and other clickable items the cursor will change to a pointer. 
    * Flash messages will appear to inform the user that their actions were successful

#### **Information Architecture**

The site operates using a traditional navigational system with a navbar at the top of the page. The main pages of the site are the feed, profile and add story page. The links to other pages on the stie branch out from these pages. The site also uses a search function so that the user may search for particular stories that they are interested in. Finally there is a number navigation system such as that seen on the bottom of search engines pages that the user can click to take them to the desired page of results.

[back to contents](#table-of-contents)

### **Skeleton Plane**

The site uses icons as metaphors. Examples of these include the left and right arrows as well as the burger icon which represents represents a menu dropping down for the navbar on small screens. The information on the site will be displayed in order of importance. An example of this is the feed page on smaller screens. The filter is not seen unless the user clicks on the button. This is because the stories in the feed are more important. Content on the site will be well spaced and will be easy to read with good colour contrast. This is good information design.

#### **Project Wireframes**

[Add/edit story page on mobile](resources/wireframes/add-story-page-small-screen.png) <br>
[Add/edit story page on tablet](resources/wireframes/add-story-page-medium-screen.png) <br>
[Add/edit story page on desktop](resources/wireframes/add-story-page-large-screen.png) <br>
[Feed/user stories/favorites/search results page on mobile](resources/wireframes/feed-page-small-screen.png) <br>
[Feed/user stories/favorites/search results  page on tablet](resources/wireframes/feed-page-medium-screen.png) <br>
[Feed/user stories/favorites/search results  page on desktop](resources/wireframes/feed-page-large-screen.png) <br>
[Following page on mobile](resources/wireframes/following-page-small-screen.png) <br>
[Following on tablet](resources/wireframes/following-page-medium-screen.png) <br>
[Following on desktop](resources/wireframes/following-page-large-screen.png) <br>
[Login page on mobile](resources/wireframes/login-page-small-screen.png) <br>
[Login on tablet](resources/wireframes/login-page-medium-screen.png) <br>
[Login on desktop](resources/wireframes/login-page-large-screen.png) <br>
[Finish/edit profile page on mobile](resources/wireframes/profile-creation-page-small-screen.png) <br>
[Finish/edit profile page on tablet](resources/wireframes/profile-creation-page-medium-screen.png) <br>
[Finish/edit profile page on desktop](resources/wireframes/profile-page-large-screen.png) <br>
[Profile page on mobile](resources/wireframes/profile-page-small-screen.png) <br>
[Profile page on tablet](resources/wireframes/profile-page-medium-screen.png) <br>
[Profile page on desktop](resources/wireframes/profile-creation-page-large-screen.png) <br>





[back to contents](#table-of-contents)


### **Surface Plane**

<br>

Below are the surface plane considerations that were made for the site
<br><br>

#### **Colour**

The colours chosen for the site are minimal. Only the three main colours from the site logo are used. Otherwise shades of black and white are applied.This is to give the site a modern feel.<br><br>

#### **Layout**

The site  attempts to create elements from the same sections aligned linearly to help in defining where sections begin and end for the user. The site uses changes of color in the navbar and footer to define sections. The site also uses borders and boxes to define which elements belong to particular sections. <br><br>

#### **Fonts**

The fonts chosen for the site are the fonts 'Modern Antiqua' and 'Lacquer'. 'Modern Antiqua' is a clean font and is inspired by the font sometimes used in old story books. Lacquer is part of the site branding and appears in the logo. It is a creepier font used to compliment the site's theme of the paranormal<br><br>

#### **Images**

The icons used on the site will be chosen according to how recognisable they are. The profile pictures were chosen due to how eye catching they were. The logo is created to be memorable yet simple. <br><br>

#### **Order and Sequence**

The most important elements on the site are the most easily recognized. An example of this is the navbar which seems to trail out of the sites eye-catching logo at the top of the page. The first link in the navbar is the to the add story page. This design is intentional and is to encourage users to post stories. <br><br>

#### **Identity**

The surface plane decisions in this site combine to create a clean modern look which incorporates elements of the paranormal seen through the fonts and colours for example. This combination is intended to portray the brand as being openminded to both the world as is known as well as unknown. <br><br>

---