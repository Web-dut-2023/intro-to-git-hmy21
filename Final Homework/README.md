# Railway Ticket System

## 2023/11/23

#### Think that what I should write by Django and HTML, JS.

I have no idea initially. I only create a file names "final Homework" and put it in the repositories. When I have created a Django project and app, I used the terminal but finally the error occurred one by one. I found my app in a false position, so I began to think what should I do calmly. Finally, I thought I should write a railway system as my final homework.

... How to design a database? I think it for a long time. At that time the "airline system" in the web class suddenly come into my mind. 

***Thinking: VS <<<<<<<< PyCharm!  JetBrains is my god!!!***



## 2023/11/24

#### Modify the database model

ah... The database should have some essential change... Import "cost", "train number" column in order to let the passenger feel more convenient.

#### Create a new user

Create a new user but finally I found that it is forbidden to access any website...

#### Design CSS file

Why the CSS file can not import as a template... This problem should be solved by asking for Mr. Lu.

#### Add ticket number

By using "if" sentence, control how to show in the index page.

#### Solution:

Every time I want to submit a new people, it may refresh to a result "there is no passenger", Django always lost these context. So I use Session to bank my message. The code below:

```python

request.session['selected_passengers'] = [passenger.id for passenger in selected_passengers]

selected_passenger_ids = request.session.get('selected_passengers', [])
selected_passengers = Passenger.objects.filter(id__in=selected_passenger_ids)

```

##### Problems already in second day:

How to use JavaScript in my Django project? 

Should I make a page like "user"? (Now it is only a administration)

The first page is sooooo ugly. I should put in some "/words" to navigate to the page I eager to view.***（Do it Tomorrow）***

I write the "users.url" but now I really do not know my session how to connect to the /admin. When I submit, the passenger page have not any change. 

##### Thinking

I think the meaning of the "user.url" is only when I submit, contrast to the session(selected passengers) and put their data to the administration system.

***That's how it should be！***



## 2023/11/25

#### First Page

It is a navigation page. IF you want  to inspect all the trains or you are an administrator, you would be satisfied in this page. Find a picture from internet as its background picture, write a single CSS file.

Oh shit. I forgot my password...

#### Database

passenger add column: contact.

#### Add different ticket shows

The quantity of tickets: >5 ?  green; >0 <5? red; =0?  grey. 

#### Add search function

Although I have wrote the function and JS file, it didn't have  any reaction... 

#### Thinking and Problems

The "group" in the Django administration is useless? What is its function?

In the administration page, the first name and the last name is in a long distance.

Why it not change to what I set in my CSS file?

Administration connect to the "submit"



## 2023/11/27

#### Upgrade the page design

The structure of the html page. Change the show form to a table. 

#### Some Problem's Solution

CSS: Layout have not any usage.

Fix the html which would make the JavaScript code cannot run successfully. 

#### Create a sort function

