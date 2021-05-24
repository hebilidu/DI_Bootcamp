### Steps to start a virtual environment/project/application

<!-- Create new virtual environment in current directory -->
python -m venv school_venv

<!-- Activate new environment -->
source school_venv/bin/activate

<!-- Update pip and setuptools in new virtual environment -->
python -m pip install --upgrade pip setuptools wheel

<!-- Install Django -->
pip install django

