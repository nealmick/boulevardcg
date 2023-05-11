# boulevardcg
Technical Interview 

```Bash

git clone https://github.com/nealmick/boulevardcg.git
cd boulevardcg
pip3 install -r requirements.txt

python3 manage.py migrate
python3 manage.py test
python3 manage.py createsuperuser
python3 manage.py runserver 

http://localhost:8000/api/articles/

#note: this does use token based authentication and you must be authoried via the admin panel.
http://localhost:8000/admin/


```
