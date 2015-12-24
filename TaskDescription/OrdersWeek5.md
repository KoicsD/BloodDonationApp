# Persist donor

## Description:

After the user typed in the data of a donor, the program should store the data in a file. The file format should be CSV (Comma Separated Value), where the values are separated with a comma. If a field contains comma then field should be bounded with quotation marks.
For more information click on the link at the bottom.
Take care of storing EVERY field of the donor, because the program should be able to restore the previously stored fields!
When a field is empty, store an empty field.
Something like this:
Kandisz Nóra,1990.09.10.,123456AB,,,"Régiposta u. 9. , Fsz/1",,

## Acceptance criteria:

* Add donor is available from main menu
* After enter all necessary data that is appended to the previous stored **donors.csv**
* The **donors.csv** file should be in a separated folder named: "**Data**"

Order: 1

---------------------------------------
---------------------------------------

# Persist donation

## Description:

After the user typed in the data of a donation event, the program should store the data in a file. The file format should be CSV (Comma Separated Value), where the values are separated with a comma. If a field contains comma then field should be bounded with quotation marks.
For more information click on the link at the bottom.
Take care of storing EVERY field of the donation event, because the program should be able to restore the previously stored fields !
When a field is empty, store an empty field.
Something like this:
Miskolc,2015.12.01,,,,"Régiposta u. 9. , Fsz/1",,

## Acceptance criteria:

* Add doantion is available from main menu
* After enter all necessary data that is appended to the previous stored **donations.csv**
* The **donations.csv** file should be in a separated folder named: "**Data**"

Order: 2

----------------------------------------
----------------------------------------

# Basic menu

## Description:

As a user I want to able to choose my next action from a menu. The menu should look like this:

1. Add new donor
2. Add new donation event
3. Delete a donor
4. Delete a donation event
5. List donors or donation events
6. Search
7. Exit

![](mainmenu.jpg)

When the user types in a number (1-7) and presses enter the screen should be cleared and chosen function should run.

* Add new donor: the program should get the neccessary data from user via console. If the donor is ready for donation, the program should store the given values. When persistence is done the program should return to the main menu screen.
* Add new donation event: the program should get the neccessary data from user via console. After all values are given the program should store the given values. When persistence is done the program should return to the main menu screen.
* Delete a donor: the program should get the unique identifier or passport number of the donor. After the program deleted the donor with the given identifier, it should return to the main menu screen.
* Delete a donation event: the program should get the unique identifier of the donation event. After the program deleted the donation event with the given identifier, it should return to the main menu screen.
* List donors or donation events: chosing this menu item a new menu screen should be appeared where the user can choose if he/she would like to list donors (1) or donation events (2) or can cancel (0) the operation and return to the main menu screen. When user chose list donors the program should list all the previously stored donors. It is similar to list donation events.

## Acceptance criteria:

* add new donor
* add new donation event
* delete a donor
* delete a donation event
* list donors or donation events
* search in donors or donations
* in the sub menu there is a possibility to go back to the main menu
* after add/delete actions the system go back to the main menu
* after list and search actions there is a possibility to go back to the main menu

Order: 3

--------------------------------------
--------------------------------------

# Delete donor

## Description:

As a user I want to have a menu item in the application to be able to delete any donor. I want to use the attribute to delete the selected one that handled as a unique identifier. In case of missing or wrong ID I want to know I have to correct the given input to search. In that case the corresponding error message is visible. I want to have a feedback about the executed deletion. If it was possible then a notification is necesseary. Please keep in mind the storage file do not store the deleted data after the deletion.

## Acceptance criteria:

* The donor with given ID is deleted when I chose the corresponding menuitem and type the ID to delete.
* The storage file is up-to-date.
* I have feedback message to be sure the state of the execution of the deletion.
* When I can not delete because of any reason I want to get back to the main menu.

Order: 4

---------------------------------------
---------------------------------------

# Delete donation

## Description:

As a user I want to have a menu item in the application to be able to delete any donation. I want to use the attribute to delet the selected one that handled as a unique identifier. In case of missing or wrong ID I want to know I have to correct the given input to search. In that case the corresponding error message is visible. I want to have a feedback about the executed deletion. If it was possible then a notification is necesseary. Please keep in mind the storage file do not store the deleted data after the deletion.

## Acceptance criteria:

* The donation with given ID is deleted when I chose the corresponding menuitem and type the ID to delete.
* The storage file is up-to-date.
* I have feedback message to be sure the state of the execution of the deletion.
* When I can not delete because of any reason I want to get back to the main menu.

Order: 5

---------------------------------------
---------------------------------------

# List donor / donation

## Description:

As a user I want to have a List menu in the application. When the list menu is selected I want to have a question to select the "DONOR" or "DONATION" to list. Every donor or donation is listed to the console. Please keep in mind print only the amount of donor or donation that is readable in the screen. Add the opportunity to page to next page.

```
-------------------------------------------
Bela, Kiss
90kg
1995.01.01 - 20 years old
[email protected]
-------------------------------------------
```

## Acceptance criteria:

I can succesfully list the donors or donations from the storage file to the screen.
I can page the donors or donations if cannot be listed out in one screen alltogether.
If the list is empty the user should be informed.
The printing should be structured in the given form.

Order: 6

-------------------------------------------
-------------------------------------------

# Search

## Description:

As a user I want to have a **Search** menu in the application. When the search menu is selected I want to have a question to select the "DONOR" or "DONATION" to search. Every donor or donation from the result is listed to the console. Search should be like search everywhere so in every field of the items (name, email, age). Please keep in mind print only the amount of donor or donation that is readable in the screen. Add the opportunity to page to next page.

![](search_menu.jpg)

## Acceptance criteria:

* Entering into the search menu the screen should be cleared (see attachment)
* I can succesfully search the donors or donations from the storage file to the screen.
* All the donors or donations should be listed which contain the term in any field.
* I can page the donors or donations of the result if cannot be listed out in one screen alltogether.
* If the result list is empty the user should be informed.
* The printing should be structured in the given form.
* The result items should start with an order
* All result item should be separated with a line

Order: 7

---------------------------------------------
---------------------------------------------

# Extend list with order by

## Description:

As a user I want to be able to give a field as an order by clause when I choose **list** menu item. After I type it from an option list the result should be sorted ascendantly according to the choosen field. If I didn't choose any field (only hit ENTER) the result should be sorted by

* Name in case of Donors
* Date of event in case of Donation
  by default.

## Acceptance criteria:

* The option list appeared after chose List
* By default the result sorted by Name in case of Donors
* By default the result sorted by Date of event in case of Donations
* If I chose a concrete field the result should be sorted according to that

Order: 8

---------------------------------------------
---------------------------------------------

# Actual menu item background color

## Description:

As a user I want to see more visualization in the menu. I don't want to enter a number for select a menu item. I want it to be more comfortable just stepping between menu items with the up/down cursor keys. I want to see which menu item is selected before I choose it so the current menu item should has white background and black font color.

## Acceptance criteria:

* Menu is still funcational
* If I press up key the menu item above becomes selected 
* When I stand on the first item than the selection doesn't change on pressing up
* If I press down key the menu item below becomes selected
* When I stand on the last item than the selection doesn't change on pressing down
* By default the first menu item is selected

Order: 9

----------------------------------------------
----------------------------------------------

[Next: Week6](OrdersWeek6.md)  
[Previous: General](InitialOrder.md)  
[Back to README](../README.md)
