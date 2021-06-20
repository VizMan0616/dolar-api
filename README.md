<div align="center">
  <img src="https://i.ibb.co/jrqYQBq/dolar-api-logo.png" alt="dolar-api-logo" width=320 height=120>
  <h2>Simple but yet experimental USD to VES conversion API</h2>
</div>

<!-- TABLE OF CONTENT -->
<details open="open">
  <summary>
    <p><i>Table of content</i></p>
  </summary>
  
  <ol>
    <li>
      <a href="#about-the-api">About the API</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#api-usage">API Usage</a></li>
  </ol>
</details>

## About the API

This is an experimental API, wich means is still in development. Any contributions are welcome! 

It was built with a simple purpose, be used to easily fetch the value of the US Dollar in VES and viceversa. So it can simplify many a tedious and common task handled in many kind of softwares and applications. 

### Built With
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## API Usage

The basic URL to handle the API are:
1. To see the value of US Dollar in VES:
  ```sh 
    https://usd-to-ves.herokuapp.com/dollar
  ```
  
  
2. To convert a specific quantity of US Dollars in VES, give it the paramenter ``` usd=FLOAT_VALUE ```
   ```sh 
     https://usd-to-ves.herokuapp.com/dollar?usd=FLOAT_VALUE 
   ```
   - or simply using json notation to send the parameter:
   ```json 
   {
      "usd": "FLOAT_VALUE"
   }
   ```
3. To convert a specific quantity of VES in US Dollars, give it the parameter ``` ves=FLOAT_VALUE ```
   ```sh 
    https://usd-to-ves.herokuapp.com/bolivar?ves=FLOAT_VALUE 
   ```
   - or simply using json notation to send the parameter:
   ```json 
   {
      "ves": "FLOAT_VALUE"
   }
   ```
  > Note: The ``` ves ``` argument is mandatory, if you don't provide it, I'll throw an error.
