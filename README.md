# Readit-Social-App Project

#### - A Fullstack simple social platform where users can join communities consisting of people with same interests.
#### - This projects backend is implemented using Python Django Framework and Frontend implemented using HTML (with Django template language) and Bootstrap CSS.
#### - The projects main idea is to enable users to join some community or multiple communities and only see posts from members of these communities (Community Posts).
#### - Once a user is signed up he can Create posts, Create a new community, Comment on community posts, Join/Leave Communities and filter posts based on tags.

##### - Signup Page
- This page includes fields that are required for registering the user into the site.
- Once a user is registered he can Add profile image and edit his data too.
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/signup.png" alt="drawing" width="900" height="500"/>

##### - User Profile and User Model
- Once a user is signed-up or logged in he is redirected to User profile page where he can edit his data and also add an image.
- Django built-in User Model was used but some fields were added, this was to make use of built-in password hashers that django admin uses and also other built-in functions such as check_password, login and logout
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/profile1.png" alt="drawing" width="900" height="500"/><br>
User Model showing password hashed in Django Admin Panel
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/user_admin.png" alt="drawing" width="900" height="500"/><br>
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/profile2.png" alt="drawing" width="900" height="500"/>

##### - Site Communities
- This page includes all communities on the website, each community has a name, description and an image.
- Usefull data is fetched from database like community total member count.
- User is able to join any community by clicking on Join Community button.
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/communities.png" alt="drawing" width="900" height="500"/>

##### - Users joined Communities
- In My Communities tab the user can leave any community of his joined communities.
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/user_communities.png" alt="drawing" width="900" height="500"/>

##### - Home Page
- This page shows posts from all communities that the user has joined.
- Each post has a comments sections, comments counter, community related post, content, image, and Author info including his profile picture on top.
- Side panel show options to create Post/Community and Filter posts based on tags.
- Side panel tags are rendered dynamically which means adding new tags will reflect on the panel and also posts will be filtered base on them easly.
<br>
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/home.png" alt="drawing" width="900" height="500"/><br>
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/home_view.png" alt="drawing" width="900" height="500"/><br>
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/tag_filters.png" alt="drawing" width="900" height="500"/><br>

##### - Creating a Post
- This form take required info to create a new post, User can assign multiple Tags and should choose one community.
<br>
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/create_post.png" alt="drawing" width="900" height="500"/><br>

##### - Posts Comments section
- Each post has comments section with comments fetched from database comments table where each comments is assigned a foreign key to post id on posts table.
<br>
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/post_comments.png" alt="drawing" width="900" height="500"/><br>
<br>
##### - Footer
<br>
<img src="https://github.com/OmarKhaledm21/Readit-Social-App/blob/main/SS/footer.png" alt="drawing" width="900" height="500"/>


