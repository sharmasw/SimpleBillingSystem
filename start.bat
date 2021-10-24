echo "Starting Billing App"


start cmd.exe  "" /C "activate py36 && python manage.py makemigrations && python manage.py migrate && python manage.py migrate --run-syncdb  && python manage.py runserver" 



start "" C:\"Program Files"\Google\Chrome\Application\chrome.exe "http://127.0.0.1:8000/"





