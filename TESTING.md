# Testing Instructions

## Table of Contents

- [Navigation](#navigation)

- [Filter Option](#filter-option)

- [CRUD](#crud)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)

- [Login](#login)

- [Sign Up](#sign-up)

- [Logout](#logout)

- [Commenting](#commenting)

- [Liking](#liking)

- [Social Links](#social-links)

## Navigation

All navigation links, including home icon, can be found in navbar or on small to medium screens in the burger drop-down menu.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Home Link Icon** | While not on homepage, click icon. | Icon shrinks and expands. User is redirected back to homepage. |
| **"Browse" Link** | While not on homepage, click "Browse". | User is redirected back to homepage. |
| **"Login" Link** | While not authenticated, click "Login". | User is directed to Login form. |
| **"Sign Up" Link** | While not authenticated, click "Sign Up". | User is directed to Sign Up form. |
| **"My Haikus" Link** | While authenticated, click "My Haikus". | Renders list view of authenticated user's haikus. |
| **"Create" Link** | While authenticated, click "Create". | User is directed to haiku submit form with instructions on how to write a haiku. |
| **"Logout" Link** | While authenticated, click "Logout". | User is directed to page with Sign Out button. |

## Filter Option

All existing tagnames are listed as a button group on the home page.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **"All haikus"-Btn** | Click on button called "All haikus". | Renders list view of all submitted haikus. Button acts as "remove filter" function. |
| **Tagname-Btn** | Click any button of the tag list. | Renders list view only of haikus with the same tagname. In case of no submitted haikus with chosen tag, generic message displays to the user. |

## CRUD

The full CRUD functionality is only available to authenticated users.

### Create

Write and submit a haiku via haiku submit form (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Title field** | Select field with placeholder "Enter a title" and start typing. | Placeholder disappears, title shows instead. Typing is disabled after 100 characters. |
| **Tag drop-down** | Click "Tag your haiku" drop-down menu and select tagname. | Shows all available tag options. Placeholder is not selectable. Selected options displays after closing drop-down. |
| **Content field** | Select field with placeholder "Write haiku here" and start typing. | Placeholder disappears, written text displays. |
| **Submit** | After completing haiku form, click submit button. | User is re-directed to homepage with the newly submitted haiku showing top of the list. |
| **Incomplete form** | Failing to fill out all form fields, click submit button. | User remains on "Create" page and is prompted to complete missing fields. |

### Read

Read submitted haikus, including tanka extensions (available to all users).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Haiku panel link** | On homepage, click on any haiku panel. | New view opens displaying haiku body, title, author and tagname. |
| **Tankas** | Scroll down below haiku body. | If available, tanka extensions render below haiku, listing body and author. If no tankas available, generic message dispalys. |

### Update

Option to edit existing haikus via haiku detail view (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **User match** | On homepage, click haiku submitted by different user. | Haiku detail view does not show edit button to ensure users can only update their own haikus. |
| **Edit-Btn** | From haiku detail view, click edit button below haiku body. Button is only visible after loggin. | Renders haiku edit form with title and content field pre-populated by original post. |
| **Cancel** | Below edit form, click "Cancel". | User is redirected to homepage with no action taken. |
| **Submit** | Alter form input according to desired update. Click edit button below form. | User is re-directed to homepage with the newly edited haiku showing top of the list. |
| **Incomplete form** | Failing to fill out all form fields, click edit button. | User remains on edit form view and is prompted to complete missing fields. |

### Delete

Option to delete existing haikus via haiku detail view (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **User match** | On homepage, click haiku submitted by different user. | Haiku detail view does not show delete button to ensure users can only delete their own haikus. |
| **Delete-Btn** | From haiku detail view, click delete button below haiku body. Button is only visible after loggin. | User is directed to delete page which prompts user to confirm delete action. |
| **Confirm Delete** | On delete page, click "Delete". | User is re-directed to homepage, selected haiku has been deleted. |
| **Cancel** | On delete page, click "Cancel". | User is re-directed to homepage with no delete action taken. |

## Login

## Sign Up

## Logout

## Commenting

## Liking

## Social Links

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Link Icons in Footer** | Click on any of the social media icons | New tab opens with respective social media site |