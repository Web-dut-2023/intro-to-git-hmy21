# Railway Ticket System

## 2023/11/23

#### Think about what I should write by Django and HTML, JS.

I have no idea initially. I only created a file named "final Homework" and put it in the repositories. When I created a Django project and app, I used the terminal but finally, the error occurred one by one. I found my app in a false position, so I began to think about what should I do calmly. Finally, I thought I should write a railway system as my final homework.

... How to design a database? I have thought about it for a long time. At that time the "airline system" in the web class suddenly came into my mind. 

***Thinking: VS <<<<<<<< PyCharm!  JetBrains is my god!!!***



## 2023/11/24

#### Modify the database model

ah... The database should have some essential changes... Import the "cost", and "train number" columns in order to let the passenger feel more convenient.

#### Create a new user

Created a new user but finally, I found that it is forbidden to access any website...

#### Design CSS file

Why the CSS file can not be imported as a template... This problem should be solved by asking for Mr. Lu.

#### Add ticket number

By using the "if" sentence, control how to show on the index page.

#### Solution:

Every time I want to submit a new person, it may refresh to the result "there is no passenger", Django always lost this context. So I use Session to bank my message. The code below:

```python

request.session['selected_passengers'] = [passenger.id for passenger in selected_passengers]

selected_passenger_ids = request.session.get('selected_passengers', [])
selected_passengers = Passenger.objects.filter(id__in=selected_passenger_ids)

```

##### Problems already in the second day:

How to use JavaScript in my Django project? 

Should I make a page like "user"? (Now it is only an administration)

The first page is sooooo ugly. I should put in some "/words" to navigate to the page I am eager to view. ***（Do it Tomorrow）***

I wrote the "users. URL" but now I do not know my session how to connect to the /admin. When I submitted it, the passenger page did not change. 

##### Thinking

I think the meaning of the "user. URL" is only when I submit, contrast to the session(selected passengers) and put their data into the administration system.

***That's how it should be！***



## 2023/11/25

#### First Page

It is a navigation page. If you want to inspect all the trains or you are an administrator, you will be satisfied on this page. Find a picture from the internet as its background picture, and write a single CSS file.

Oh shit. I forgot my password...

#### Database

passenger adds a column: contact.

#### Add different ticket shows

The number of tickets: >5 ?  green; >0 <5? red; =0?  grey. 

#### Add search function

Although I have written the function and JS file, it didn't have any reaction... 

#### Thinking and Problems

The "group" in the Django administration is useless? What is its function?

On the administration page, the first name and the last name are in a long distance.

Why did it not change to what I set in my CSS file?

Administration connects to the "submit"



## 2023/11/27

#### Upgrade the page design

The structure of the HTML page. Change the show form to a table. 

#### Some Problem's Solution

CSS: Layout does not have any usage.

Fix the html which would make the JavaScript code cannot run successfully. 

#### Create a sort function

You could find the trains by some order.

 

## A week

My teacher told me that I should innovate. But... he said for example you could create a GPT model, I think it is extremely challenging to me, a senior student. I guess that I can find some inspiration from GitHub, I knew that it should use NLP and GAN etc. But the truth is, I do have not any experience with them. So what I can do is learn them from ahead. 



Nevertheless, there is no CSV file which could help me to train my railway model. I have no data! (Although I have already prohibited the process of building an AI model )



## 2023/12/3

#### Fix the error

Fix that I cannot update the message in the list, connect to the database, and once you refresh the website, you could get a new list.

#### What is INNOVATION?

The big data model has been banned. How to innovate? In my system, there are some easy Django projects.
