# A basic **Real Estate website** 

It contains 3 main modules:
1. **Profile** (Dealer/Buyer)
2. **Catalogue**
3. **Enquiries**

**Profile** module is for User related operations.

**Catalogue** module is the core module which displays postings of properties.

**Enquiries** module to post enquiry for the property by the buyer.


## Installation

### Dependencies:

1. Python needs to installed in the system, supports Python 3.5, 3.6, and 3.7
2. A virtual env is need, check: https://docs.python.org/3/library/venv.html

Steps:
1. Create a Virtual Env, activate it: `source <env_name>/bin/activate` --> for Linux or `<env_name>/Scripts/activate.bat` --> for Windows
2. Install requirements using requirements.txt by going to squaremetres subfolder.  
  `pip install -r requirements.txt`
3. Create a sqlite database with no tables. Awkward right? Use any database as per your need, this is a basic application.
4. run migrate command to create tables in database  
  `python manage.py migrate`
5. Tada. All done. Run Django Server:  
  `python manage.py runserver`

Check your running portal at: 127.0.0.1
If above not working try: 127.0.0.1:8000 or localhost:8000
