# class_student_management
create a python3 virtual environment using command "virtualenv -p python3 "(on linux)

activate the environment using command "source /bin/activate"(on linux)

install requirements from requirements.txt using command "pip install -r requirements.txt".

go to the folder which has manage.py.

run command "python manage.py runserver" http://localhost:8000/students(get,post)- to get all students list and by using this api can add student all information.We an add total marks of sudent per yesr,exam related marks and subjectwise marks.

http://localhost:8000/students/search_student_by_roll_no/?roll_no=(value of roll no)(get)- to search a particular student by its roll_no
http://localhost:8000/students/search_students_by_subject/?sub_code=(value of roll no)(get)- To search students by subject
