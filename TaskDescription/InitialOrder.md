## General requirements:

In your solution use all the techniques what you have learnt before: Classes, Tests, Git repository
Your solution should be in a grithub repository
Your solution should contain enough unit tests which are validating the correct functionality. All the test should pass.
Try to think in object oriented way. So the closely linked data should be in classes.
Your application should contain a main file which is runnable
Code should be correctly commented
Take care of error handling. Program should be working as a stabalized one for any cases. (e.g. incorrect input)
So the task is create an application which suitable for handling blood donation (maybe it is familiar a bit ;)):

----------------------------------------------------------------------
----------------------------------------------------------------------

## Donor registration

### Getting data from user:

* Name,
* Weight,
* Gender,
* Date of Birth,
* Last donation date,
* Was he/she sick in the last month?
* Unique identifier
* Blood type
* Expiration of ID
* email address
* Mobil number

### Functions:

* Parse name, store it in a separated object
* Suitable for donation:  
  weight > 50
* last donation was more than 3 months ago  
  age > 18 years
* How old is the donor in years based on date of birth?
* ID is not expired.
* Define type of personal document based on its identifier:
  * 6digit + 2letter (123456AB) is identity card
  * 6letter + 2digit (ASDFGH12) is passport
* Email address validation (contains @ and ends with .hu/.com)
* Mobil number validation (starts with +36/06 + 2 digit(provider identifier - 20/30/70) ending with 7 digits)
* Write out data in a table form eg.:
```
  Attila, Molnár
  90kg [using of str function]
  1989.05.06 - 26 years old
  asd@test.hu
```
* Generate random number: Hemogblobin level between 80-200, write out is the donor suitable or not (value is greather than 110)?

----------------------------------------

## Donation event registration:

### Getting data from user:

* Date of event
* Start time of donation
* End time of donation
  (You can use [datetime.strptime](https://docs.python.org/3.4/library/datetime.html#strftime-and-strptime-behavior) to convert the string into datetime type.)
* Zip code (only 4 digit positive integers allowed)
* City (See below)
* Address
* How many bed will be available? (Only positive integers allowed)
* Planned donor number (Only positive integers allowed)

### Functions:

* Registration should occur before the event at least 10 days
* Datetime can be only on weekdays
* you can use [datetime.isoweekday](https://docs.python.org/3.4/library/datetime.html#datetime.date.isoweekday) function to determine it
* Address validation
* ZIP is valid only when it contains exactly 4 digit and the first one is not 0,
* Streetname maximum length is 25,
* City is in this list: Miskolc, Kazincbarcika, Szerencs, Sarospatak
* Calculate duration in minutes based on start and endtime
* You can use [datetime.strptime](https://docs.python.org/3.4/library/datetime.html#strftime-and-strptime-behavior) and [timedelta.total_seconds](https://docs.python.org/3.4/library/datetime.html#datetime.timedelta.total_seconds) functions  
  max_donor_number = ((event_duration_in_minutes - preparation_time) / donation_time) * number_of_beds  
  preparation_time = 30  
  donation_time = 30

At the end of the event registration ask the user about how many successfull donation was on the event and store it as an integer!

### How the donation was successfull? The realized donation number:

* is below 20% of planned: "Unsuccessfull, not worths to organise there again"
* is between 20-75% of planned: "Normal event"
* is between 75-110% of planned: "Successfull"
* is above 110% of planned: "Outstanding"

--------------------------------------------------------
--------------------------------------------------------

tags: error handling, git, OOP, python, SCRUM

[Next: Week5](OrdersWeek5.md)  
[Back to README](../README.md)
