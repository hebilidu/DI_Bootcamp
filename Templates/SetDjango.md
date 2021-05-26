### Steps to start a virtual environment/project/application

<!-- Create new virtual environment in current directory -->
python -m venv school_venv

<!-- Activate new environment -->
source school_venv/bin/activate

<!-- Check version of packages installed by venv  -->
pip list

<!-- Update pip and setuptools in new virtual environment -->
pip install --upgrade pip setuptools wheel

<!-- Install Django -->
pip install django

<!-- Eventuellement: Pillow (for pictures) -->
pip install Pillow

<!-- Eventuellement: phonenumber-field  -->
pip install django-phonenumber-field[phonenumbers]
<!-- pip install django-phonenumber-field[phonenumberslite] -->
<!-- and add phonenumber_field to the list of the installed apps in your settings.py file: 
INSTALLED_APPS = [..., 'phonenumber_field',...] -->

<!-- Create new project -->
django-admin startproject <project>
<!-- Create an app (apps may belong to many projects) -->
django-admin startapp <app>
<!-- Update project settings.py with new app -->
<!-- Initialize database -->
python manage.py makemigrations
python manage.py migrate
<!-- After the first migrate, add superuser to database -->
python manage.py createsuperuser
