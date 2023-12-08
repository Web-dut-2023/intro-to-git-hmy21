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



> 
>
> 下面是2099年铁路系统的相关车次信息
>
> 第一列是序号，第二列是终点点火车站，第三列是火车中途时间，第四列是起点火车站，第五列是火车票价，第六列是火车车次号，第七列是剩余票的数量    
>
> 1,上海南,330,起点：大连北,100,G1,0
> 2,终点：哈尔滨西站,435,起点：大连北,100,G2,3
> 3,终点：上海南,808,起点：沈阳北,100,K1,1
> 4,终点：重庆西,400,起点：上海南,210,G5,20
> 5,终点：沈阳北,700,起点：自贡,310,K4,5
> 6,终点：大连北,1300,起点：邯郸东,200,G8,9
>
> 上述信息都记住了么 下面我要根据这些信息问你一些问题 你不要自己设问 你必须根据我给你的铁路信息回答我提供给你的所有问题而不是实际情况回答 如果记住了 回答：根据我给你的信息 
>
> 
>
> 都那些地方可以坐火车到上海南 那些地方可以坐火车直达到上海南

## 2023/12/6

#### Problem I solved 

Before today, my Python translator was used by 3.9.10 in default. But in fact, there is some limit to it which leads that every time I want to install some software package,  it blocks me from installing them. I adjust some order in the environment path. Finally, I changed the default translator to Python 3.11.

#### AI Model

Ultimately, I think that makes an AI model from openai API.  I found the guides from GitHub.

The first example API is:

[first API](https://github.com/acheong08/ChatGPT)

It is a reversed engine. I installed a Node.js for it. When I run https://chat.openai.com/api/auth/session, there is a difference from what it showed. I failed.

The second I found is:

[second API](https://github.com/PawanOsman/ChatGPT#use-our-hosted-api-reverse-proxy)

For it, I downloaded a WSL and Ubuntu in my Windows operator system. It told me I should be in a Linux or Mac atmosphere to use the "migrate".

I bought a GPT API in Taobao, nevertheless, the problems come successively.  'object is not subscriptable' occurred. I found out how to solve this problem.

```python
result = response['choices'][0]['text'].strip()
```

#### GUI

In order to forbid opening the Python file in the terminal, I made up a GUI.

Change url.py and views.py and make a hypertext transfer link to connect the Django project.

```bash
root1@MrHequipment:~$ cd /mnt/c/Users/Administrator/Desktop/railway\ operator
root1@MrHequipment:~$ grit apply openai
```



#### 2023/12/8

due to transmitting the API key to the properties, I had to buy another API key...
