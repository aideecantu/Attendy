# Attendy
IEOR 171 Class Project
## Face 'n Class Ver 2.0 - by 6S

Face 'n Class is a revolutionary way of taking class attendance for IEOR 171! First, all students in the class are invited to the class Facebook group. During a designated time in class, students take selfies of their groups and upload group selfies to Lecture events on the FB Group. All groups must tag each member in the photo. 

  At a later time, the GSI (or designated student) can run the Python script in this repo. It will automatically pull all the tags from all photos to create a CSV spreadsheet for attendance. The process to run the script should take about 15 minutes in total. 

## Part 1: How to Set Up Facebook Group

1. GSI must possess a Facebook account. 
  <br><i>Option A: Use personal Facebook account. Option B: Create a separate Facebook account.</i>
2. Students must possess a Facebook account. 
3. GSI creates a group on Facebook. 

    ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/creategroup.png "FB 3")
    
4. GSI names the group: IEOR 171. GSI adds students in IEOR 171 to this group. Lastly, GSI selects the closed group option. 

    ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/closedgroup.png "FB 4")
    
5. Congratulations! Your IEOR 171 closed group has successfully been created. To fully utilize all of Facebook’s tools, feel free to upload the following: a cover photo, a description depicting the objectives of this course, or a few descriptive tags to the group to raise awareness about this course for future students. 

    ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/personalizepic.png "FB 6")

6. To take attendance, the GSI then creates an event for every lecture. 
 <br><i>For example, for lecture on 9/21/16, the GSI would create an event for that lecture.</i>
  
  ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/createevent2.png "FB 7")
  
7.	During lecture, Professor announces that it’s time to take attendance. 
8.	Students take their group selfie, and one student from their group uploads it to the designated event. 
    
    ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/tagurself.png "FB 8")

9.	Students must then tag themselves in the selfie.
   
   ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/tagurself2.png "FB 9")

10. Congratulations! You have successfully created an environment that fosters collaboration and student engagement while reducing time spent taking class attendance. Read below to install the necessary packages that enable the script to run properly. This is a one-time installation and is estimated to take about 15 minutes.


## Part two: Running facenclass.py 

## User Authentication

The GSI (or designated student helper) must first log into Facebook and generate a user access token. A user access token communicates to Facebook that this script can access the events and photos on your Facebook group. Creating a user access token is necessary because of Facebook’s privacy settings. To do so, visit:
<https://developers.facebook.com/tools/explorer/>, login, and generate a 2 hour user access token for user events and user managed groups. 

  ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/fb1.png "FB 1")
  ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/fb2.png "FB 2")

## Package Installation 

Make sure Python and pip are installed. In your terminal, run the following commands to install the Facebook SDK for Python: 

```$ pip install requests```

```$ pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk```

## Running the Script

Download facenclass.py to a desired location on your system. In the terminal, go to the directory where facenclass.py is located with the 'cd' command. 

```$ cd path/to/file```

  Run facenclass.py with the following command in the terminal:

```$ python facenclass.py```

Paste the access token and Facebook group ID (a number which you can find in the Facebook group's page URL) into the terminal when asked. The script should generate 171_attendy.csv in the same location. We've included a sample 171_attendy.csv you can look at in this repo. 
  Run facenclass.py again later if you want to update the attendance spreadsheet with new lecture photos. 
