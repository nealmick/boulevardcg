# boulevardcg
#### Technical Interview 
includes:
Article list with pagination, Detail, Create, Update, and Delete endoints.  All endpints secured with authentication classes and tested thoroughly using api/tests.py
```Bash

git clone https://github.com/nealmick/boulevardcg.git
cd boulevardcg
pip3 install -r requirements.txt

python3 manage.py migrate
python3 manage.py test
python3 manage.py createsuperuser
python3 manage.py runserver 


#note: this does use session and token based authentication.
#I recommend authorizing via the admin panel then checking out endoints.
http://localhost:8000/admin/

http://localhost:8000/api/articles/



```


```
Test input for post/put
{
    "title": "test",
    "content": "test"
}
```
