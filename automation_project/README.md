## 1. alert system
This project is used to alert.  
The script contains a crawler that crawl all the website that our company want to monitor. If the spider find our company's name on these websited, then it will send email to my colleagues. The spider run every two hours automatically on our server, which is deployed by IT department colleagues.

## 2. parse JSON
This project is used to automatically convert json data which is retrieved from the third party to txt file.  
The code will run everyday so that it can automatically parse the json data and turn the data into a txt format and save on Hadoop.  

The project can be split into the following parts:  
1. get json file path
2. parse json file, convert it to txt file and save the result
3. upload the parsed file to server

I participated in step 1 and 2, writing code to locate all the data and converting json data into txt format.
