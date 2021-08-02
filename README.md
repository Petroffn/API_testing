# [Swagger Petstore](https://petstore.swagger.io/v2) API_testing 

## Prequisities
1. Python3 is installed and added to the PATH;
2. PyTest is installed;
3. Allure is installed;
4. Faker is installed;
5. jsonpath-ng is installed;
6. curlify  is installed;
7. jsonschema is installed;
8. pytest-pythonpath is installed;

## Steps:
1. Clone the repository;
2. Use `pip install -r .\requiremants.txt` command;
3. Open in browse [Swagger Petstore](http://petstore.swagger.io )
4. Click on the "Authorize" button 
5. Enter any value in the Value field in the api_key (apiKey) block (e.g. 123456)
6. Click the "Authorize" button
7. And when sending requests, add the created api key to the header: api_key: 123456
8. To run all tests please execute `pytest --alluredir=allure-result`, `allure serve allure-result`
