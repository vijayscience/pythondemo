## Task 1 ##
Find top 3 most popular hotels between couples. (treat hotel as composite key of continent, country and market). Implement using  pyspark. Create a separate application. Copy the application to the archive. Make screenshots of results: before and after execution.

## Task 2 ##
Find the most popular country where hotels are booked and searched from the same country. Implement using pyspark. Create a separate application. Copy the application to the archive. Make screenshots of results: before and after execution.

## Task 3 ##
Find top 3 hotels where people with children are interested but not booked in the end. Implement using pyspark. Create a separate application. Copy the application to the archive. Make screenshots of results: before and after execution.


### Expected results ###

* ZIP-ed folder with your screenshots.
* ZIP-ed folder with your src.

Please upload here ZIP-ed folder with your screenshots and ZIP-ed folder with your src. as one ZIP Archive.

# Data fields
*train/test.csv*


| Column name                 | Description                                                                                                               | Data type |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------- |
| date\_time                  | Timestamp                                                                                                                 | string    |
| site\_name                  | ID of the Expedia point of sale (i.e. Expedia.com, Expedia.co.uk, Expedia.co.jp, ...)                                     | int       |
| posa\_continent             | ID of continent associated with site\_name                                                                                | int       |
| user\_location\_country     | The ID of the country the customer is located                                                                             | int       |
| user\_location\_region      | The ID of the region the customer is located                                                                              | int       |
| user\_location\_city        | The ID of the city the customer is located                                                                                | int       |
| orig\_destination\_distance | Physical distance between a hotel and a customer at the time of search. A null means the distance could not be calculated | double    |
| user\_id                    | ID of user                                                                                                                | int       |
| is\_mobile                  | 1 when a user connected from a mobile device, 0 otherwise                                                                 | tinyint   |
| is\_package                 | 1 if the click/booking was generated as a part of a package (i.e. combined with a flight), 0 otherwise                    | int       |
| channel                     | ID of a marketing channel                                                                                                 | int       |
| srch\_ci                    | Checkin date                                                                                                              | string    |
| srch\_co                    | Checkout date                                                                                                             | string    |
| srch\_adults\_cnt           | The number of adults specified in the hotel room                                                                          | int       |
| srch\_children\_cnt         | The number of (extra occupancy) children specified in the hotel room                                                      | int       |
| srch\_rm\_cnt               | The number of hotel rooms specified in the search                                                                         | int       |
| srch\_destination\_id       | ID of the destination where the hotel search was performed                                                                | int       |
| srch\_destination\_type\_id | Type of destination                                                                                                       | int       |
| hotel\_continent            | Hotel continent                                                                                                           | int       |
| hotel\_country              | Hotel country                                                                                                             | int       |
| hotel\_market               | Hotel market                                                                                                              | int       |
| is\_booking                 | 1 if a booking, 0 if a click                                                                                              | tinyint   |
| cnt                         | Numer of similar events in the context of the same user session                                                           | bigint    |
| hotel\_cluster              | ID of a hotel cluster                                                                                                     | int       |
| destinations.csv            |                                                                                                                           |           |
| Column name                 | Description                                                                                                               | Data type |
| srch\_destination\_id       | ID of the destination where the hotel search was performed                                                                | int       |
| d1-d149                     | latent description of search regions                                                                                      | double    |
