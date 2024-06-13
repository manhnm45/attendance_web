# RUN PROJECT

### Run project(without docker):

- install project

- pip install -r requirement.txt

- turn on db(config parameter db on setting)

- cd manage_staff

- python manage.py makemigrations

- python manage.py migrate

- python manage.py createsuperuser(create user)
- python manage.py runserver

### Run project with docker
- turn on docker

- cd manage_staff

- docker compose up -d --build

- docker compose run web python manage.py makemigrations

- docker compose run web python manage.py migrate

- docker compose run web python manage.py createsuperuser

- docker compose run web python manage.py runserver

# Using postman to call api get information about staff

- step1: create post api take current token `url = http://127.0.0.1:8000/token/`, choose Body and create Key (username, password)and Value (admin,1) that you created for supperuser

- step2: After receiving the accesstoken, create a Get list info api with ` url = http://127.0.0.1:8000/api-list/ `. Select Authorization, select 'bear token' and paste accesstoken. Click get to take list of staff information

- step3: Use the photo name obtained from step 2 to call the employee photo api. Create a Get image api with `url = http://127.0.0.1:8000/images/imagename.jpg/`, paste acesstoken and click Get

# postman test attendance feature

- Create a post attendance api with `url = http://127.0.0.1:8000/api-attendance` , paste access token, create key-value in Body field. Key includes(id, time, location check) Value example includes(4, 2024-05-27T18:11:00, gate 1). Click POST to let the web take attendance on the web

# Code sample to get list of employee information from the web to the camera 

> import requests
>
> #headers={'User-Agent': 'Mozilla/5.0'}
>
> payload={'username':'admin','password':'1'}
>
> session=requests.Session()
>
> token=session.post('http://127.0.0.1:8000/token/',data=payload)
>
> print("session",token)
>
> if token.status_code == 200:
>
>     response_data=json.loads(token.content)
>     print(response_data['access'])
>     access_token = response_data['access'] 
>     headers = {
>     "Authorization": f"Bearer {access_token}","Content-Type": "application/json"}
>     response=requests.get("http://127.0.0.1:8000/api-list/", headers=headers)
>     list_data = json.loads(response.content)
>     print("list_data",list_data)
> img_response=requests.get("http://127.0.0.1:8000/images/avata2.jpg/")
> 
> print("img_response",type(img_response.content))
>
> image_array=np.frombuffer(img_response.content,dtype=np.uint8)
>
> image=cv2.imdecode(image_array,cv2.IMREAD_COLOR)
>
> cv2.imshow('Image', image)
>
> cv2.waitKey(0)
