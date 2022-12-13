# xblock_development

# XBlockTestTask
Test task for the candidate



1. Clone a repository::
```console
https://github.com/ruslan-kornich/xblock_development.git
```

2. Create and activate a virtual environment:
```console
python3 -m venv venv

source venv/bin/activate
```
3. Clone the SDK:
```console
git clone https://github.com/openedx/xblock-sdk.git
cd xblock-sdk
pip install -r requirements/base.txt
```
4. Make migrations
```console
python manage.py migrate
cd ..
```
5. Inslall collapsible
```console
pip install -e collapsible
```
6. Run server
```console
cd xblock-sdk
make install 
python manage.py runserver
```
