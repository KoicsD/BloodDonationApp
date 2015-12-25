# Centralized data storage

As a user I want to store my saved data in a centralized storage. I have a MySQL server so I want to use it as a storage.

-------------

## Acceptance:

* I can configure in a config file that which way I want to store my data (See attachment)
* Mode can be (only one at a time):
  * csv
  * db
* I can connect to any available DB source by configuring the connection string
* The csv store is working as well by configuration
* All previous requirements still satisfied

------------

[app.config](app.config)

-------------------------------------------------------
-------------------------------------------------------

[Previous: Week6](OrdersWeek6.md)  
[Back to README](../README.md)
