![image](http://www.pixelstalk.net/wp-content/uploads/2016/08/Beautiful-Milky-Way-Galaxy-Wallpaper.jpg)

# Image Contrast Adjustment and Enhancement
Color Retinal image enhancement project deals with enhancing the quality of the image of an eye. So basically retinal imaging is a process of capturing retinal images of an eye which are very complicated and requires a lot of processing and sophisticated machines are used to capture those images. Now when we look at one of those images we might see that the images might be kind of little blur or brightness might be low or high. So here we have applied some techniques, such as contrast adjustment and increasing the luminosity of the images to enhance the quality of an eye which might help the doctors or professional working on this domain to get a clear view of the project/image they are looking for.

# _**Base Paper**_
+https://www.academia.edu/51841498/Analytical_Adjustment_of_Image_Contrast

# _**Project Methodology**_
So, in order to get the contrast adjustment and enhancement unlike traditional  Image Enhance library, we have gone with Equalization histogram where we have converted our image in the form of a histogram and wherever we found that the bins are clustered around, the equilize_hist(), that we are going to use, what it does is it will stretch out that portion of image making the specific object in that image to be highlighted than usual. Apart from this technique we have also used some basic OpenCV filters to enhance the quality of an image such as Adjusting the brightness using filters, threshold adjustment, sharpening the image.

_**Reference Link**_
+ https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html
+ https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html

# _**How to Execute?**_
So, before execution we have some pre-requisites that we need to download or install i.e., anaconda environment, python and a code editor.
**Anaconda**: Anaconda is like a package of libraries and offers a great deal of information which allows a data engineer to create multiple environments and install required libraries easy and neat.

**Download link:**

![Anaconda](http://img1.wikia.nocookie.net/__cb20100310215806/mafiawars/images/e/e0/Huge_item_anaconda_02.gif)

https://www.anaconda.com/

**Python**: Python is a most popular interpreter programming language, which is used in almost every field. Its syntax is very similar to English language and even children and learning it nowadays, due to its readability and easy syntax and large community of users to help you whenever you face any issues.

**Download link:**

![Python](http://animated.name/uploads/posts/2016-08/1470308776_240.gif)

https://www.python.org/downloads/

**Code editor**: Code editor is like a notepad for a programming language which allows user to write, run and execute program which we have written. Along with these some code editors also allows us to debug, which usually allows users to execute the code line by line and allows them to see where and how to solve the errors. But I personally feel visual code is very good to work with any programming language and makes a great deal of attachment with user.

**Download links:**

![Vs code](https://schwabencode.com/contents/logos/VS2019-Badge.png) ![Pycharm](https://i0.wp.com/scracked.com/wp-content/uploads/2020/01/PyCharm-2019.3.4-Crack.png?fit=200%2C200&ssl=1)

+ https://code.visualstudio.com/Download, 
+ https://www.jetbrains.com/pycharm/download/#section=windows

# _**How to create a new environment and configure jupyter notebook with it.**_
Let us define an environment and why we need different environments. An environment is a collection of libraries that are required to run our project. When we already have an environment with the necessary libraries, why do we need a new environment?
To avoid version mismatches, we create a new environment for each project. For example, in your previous project, you used "tf env" with tensorflow 2.4 and keras 2.4, but in your current project, you must use tensorflow 2.6 and keras 2.6. If you continue your project in the "tf env" environment, there will be a version mismatch and you will need to update tensorflow and keras, but this will cause problems with the previous project's execution. To avoid this, we create a new environment with tensorflow 2.6 and keras 2.6 and resume our project.

Let us now see how to create an environment in anaconda.
+ Type “conda create –n <<name_of_your_env>>”
example: conda create -n env
+ It will ask to proceed with the environment location, type ‘y’ and press enter.
+ When you press ‘y’, the environment will be created. To activate your environment type conda activate <<your_env_name>> . E.g., conda activate myenv.
+ You can see that the environment got changed after conda activate myenv line. It changed from “base” to “myenv” which means you are now working in “myenv” environment.
+ To install a library in your virtual environment type pip install <library_name>.
e.g., pip install pandas
+ Instead of installing libraries one by one you can even install by bunch, i.e., we have a txt file called requirements.tx which consists of all the libraries required to proceed with the project, so we can use it.
+ so, before installing requirements.txt, make sure you are in the specific path where your requirements.txt is located, basically this file is located in the folder where our executable files are located, so we need to move to that directory by following command.
**cd A:\folder_name**
+ Here A -> drive, folder name -> path where your executable file is saved
+ I go to that file path in anaconda using cd command 
1.	Go to drive where your project file is.
2.	Go to the path of your project using cd <path>
3.	Type pip install –r requirements.txt 
+ And all your required libraries will be downloaded and you can start your project.
+ But if you want to use jupyter notebook on the new environment you have to set it up for the new environment.
+ After you have installed all the libraries and created an environment, you need an editor to run the code, that is starting jupyter notebook, as soon as you enter jupyter notebook in the terminal you will definitely get this error. “Jupiter” is not recognized as an internal or external command.
So, to solve it it we have 2 commands.
1.	conda install –c conda-forge jupyterlab
2.	conda install –c anaconda python
Now you are ready to use jupyter on this environment and start with your project!

![thanks](https://media.giphy.com/media/3oEjHTsP47u1BTgY24/giphy.gif)
  
### _**Credits to my friend who gave detailed explanation of installation procedure.**_
+ https://github.com/PaVaNTrIpAtHi
+ https://www.linkedin.com/in/pavan-tripathi-3993641a1/
  
# _**Steps to execute**_
**Note:** Make sure you have added path while installing the software’s.
1. Install the prerequisites mentioned above.
2. open anaconda prompt and create a new environment.
  - conda create -n "env_name"
  - conda activate "env_name"
**If you face any issue while setting up, please feel free to read the How to create a new environemnt in anaconda and you can click on the below link given at the end to get more detailed explanation.
3. Install necessary libraries from requirements.txt file provided.
4. Run pip install -r requirements.txt or conda install requirements.txt (Requirements.txt is a text file consisting of all the necessary libraries required for executing this python file. If it gives any error while installing libraries, you might need to install them individually.)
5. Run main.py "path of image to test" in your anaconda terminal, ex: main.py test_data/01.jpg, and make sure to change the path where you executablee fiels are located, please follow the link on how to set up anaconda environemtn to execute files.
https://techieyantechnologies.com/2022/06/get-started-with-creating-new-environment-in-anaconda-configuring-jupyter-notebook-and-installing-libraries-using-requirements-txt-2/

# _**Data Description**_
Specifically, We didn't use any kind of dataset since we are trying to load the images manually aand applying filters on top of it, so we havent used any datsets.

 # _**Issues Faced.**_
1. We might face an issue while installing specific libraries.
2. Make sure you have the latest version of python, since sometimes it might cause version mismatch.
3. Adding path to environment variables in order to run python files and anaconda environment in code editor, specifically in visual studio code.
4. Refer to the Below link to get more details on installing python and anaconda and how to configure it.
+ https://techieyantechnologies.com/2022/06/get-started-with-creating-new-environment-in-anaconda-configuring-jupyter-notebook-and-installing-libraries-using-requirements-txt-2/

# _**Note:**_
**All the required data has been provided over here. Please feel free to contact me for any issues.**

### _**Let’s Connect**_
https://www.linkedin.com/in/abhinay-lingala-5a3ab7205/

![Connect](https://media.giphy.com/media/d9WRhx9qErqCY/giphy.gif)

# _**Yes, you now have more knowledge than yesterday, Keep Going.**_
![Happy](https://media.giphy.com/media/n5VaQoW39Z9S0/giphy.gif)
  
  
