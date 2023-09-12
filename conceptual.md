### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  - Syntax.
  - JS has full browser support in the terminal, while Python requires one to utilize the terminal and other frameworks to debug and interact.
  - JS is used for front-end and back-end web developement, Python can be used in back-end web developement and a wide range of applicaions:
    - Analyzing RNA sequencing data
    - Data Science Applications
    - Etc.

<br>

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  - You can use the get() method, which will search for a key's value in a dictionary and either return with the value or None.
  - You can use try and except blocks to search for a key's value and if an error is raised then your whole application won't stop.

<br>

- What is a unit test?
  - A unit test is the smallest form of testing, an isolated test that focuses on individual functionalities would count as a unit test.

<br>

- What is an integration test?
  - An integration test is when a programmer tests the interactions of multiple functionalities within an application at once.

<br>

- What is the role of web application framework, like Flask?
  - A web application framework like Flask simplifies the code required to establish routes, manage requests, render HTML, etc. Overall, it makes web developement with Python more truncated and readable for programmers. There are also many tools that make the testing of web applications smoother, such as the server deployment included in standard Flask applications.

<br>

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - One consideration might be if its a parameter that you want to include a universal functionality, such as rendering the same base template for all users. But if you have funcitionalities that would include dynamic variables then using a query parameter would be better because it would not require explicitly creating new routes in your application.

<br>

- How do you collect data from a URL placeholder parameter using Flask?
  - When declaring a URL placeholder parameter one must include a variable name within <>, this gives a programmer to call on the declared variable name within a route's view functions. 

<br>

- How do you collect data from the query string using Flask?
  - By accessing the request object (an importable Flask object), A programmer is able to grab query data with the .args property and the .get() method. 

  > request.args.get('example')

<br>

- How do you collect data from the body of the request using Flask?
  - Access to data found in a request's body is dependant on the content type of the request:
    - **Form Data**: uses request.form
    - **JSON Data**: uses request.json
    - **Other Data**: uses request.data (_Access raw binary data_)

<br>

- What is a cookie and what kinds of things are they commonly used for?
  - Cookies are small pieces of data that are sent back and forth between a server and user's browser everytime they interact. They are excellent at:
    - Authenticating Users
    - Remembering User States
    - Protecting Against CSRF (_Cross-Site Request Forgery_) Attacks 
    - Etc.

<br>

- What is the session object in Flask?
  - The session object in Flask is a built-in tool that lets one store unique data across multiple requests and responses. It is typically used in remembering specific user states on a Flask Application.

<br>

- What does Flask's `jsonify()` do?
  - A function that serializes data structures into a JSON format and labels it with the proper content type header in the HTTP response to indicate that the response contains JSON.
