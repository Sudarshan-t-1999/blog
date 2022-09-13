# A blog page
![blog demo](https://user-images.githubusercontent.com/76962685/189488190-5379cf92-cdd1-47c4-861e-6aa47809e688.jpeg)

This blog page allows anyone to write a blog for others to see. It also allows for the blog to be either edited and deleted.

The backend of this project is made using the **Flask** library of python and the frontend with **HTML** and **Bootstrap**.

## How to run this project in local machine?
* First, download the contents of this repository to your local machine. You can do this by cloning the repository using the `git clone <repository url>` in Command Prompt(if you do not have git installed, download and install it from the git website) or click on the code button and then on 'Download ZIP' button and extract the files.
* Make sure you have installed python in your machine. If not, download and install it from the official python website.
* If not installed, open command prompt or powershell and install `virtualenv` python library using the command `pip install virtualenv` and then create a virtual environment using the command `virtualenv <environment name>` to run the program in. 
* After creating the virtual environment, change the directory to the root folder of the virtual environment using the `cd` command, then activate the environment using `Scritps\activate` command. You can confirm the activation, when the name of the environment appears within paranthesis before every command like `(environment name) C:/path to the environment`.
* Then copy the downloaded files inside the virtual environment directory.
* Then install the dependencies listed in the requirements.txt file on the virtual environment using the command `pip install -r requirements.txt`.
* To run the file type, `python FLASK.PY`. This will start the application, to use the application you can either copy the ip address appearing next to `* Running on` and paste it on a browser search bar or open a browser and type `localhost:5000` in the search bar.
* This will load a page identical to the one shown in the image above.

## How to use the Blog?
* Enter your Name, Title and Content of the blog then click on submit.
* After that the warning box will disappear and your blog will be added in its place.
* You can delete the blog from the page if you want by clicking on the `Delete` button.
* If you want to edit anything about the blog,  click the `Edit` button which will open the edit page with the same text boxes which are prefilled with the details that you entered. Make the changes that you need and click on the `Submit` button which will update the blog displayed in the Home page. 

## Credits
This project was made by referencing and changing upon the concepts learnt from [this vedio](https://www.youtube.com/watch?v=oA8brF3w5XQ) on [codewithharry's](https://github.com/CodeWithHarry) [YouTube channel](https://www.youtube.com/c/CodeWithHarry)
