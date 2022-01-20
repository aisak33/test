# test


Take home excercise python file
plus test file in python

I do not have docker application on my laptop, so I included an extra endpoint which could improve efficiency by specifying which account id is of interest, but compared to the original endpoint, this endpoint would return multiple accounts at once.
Add a lot more error handling
Use the response code to return a user-friendly explanation as to why an error occurred. For example, error code 400 indicates a user error, with input values. In these messages specify the datatypes, length of input anything specific that needs to be mentioned in order to resilve the error. I would include an example of correct and incorrect input values
Add headers. For data security it is always useful to add customised headers which limits the access to designated users only
Incorporate partial responses to deal with large resources, especially with applications designated only for get responses. This helps to reduce the requests traffic and makes the get operation more efficient
Filters
Include more filters in the endpoints to reduce the amount of data returned and only get the required data. These filters can be added into the path parameter and the query parameter


