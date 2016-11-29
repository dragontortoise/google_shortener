# google_shortener

Originally this code is totally created by http://stackoverflow.com/a/1
7357552/1401639 ( https://goo.gl/PJbo90 ).

This program is tested with Python 3.

We need Google URL Shortener API Key in order to run this program.

We use only API Key without OAuth 2.0 authentication as we don't need
to access individual's private data.

Steps to acquire Google URL Shortener API Key are as follows:
  - Go to https://console.developers.google.com/apis/api/urlshortener/
    overview ( https://goo.gl/E7oUw7 ).
  - Click 'Create project'.
  - Click 'Create a project'.  Set 'Project name' to be anything you
    want.  For me, I set it to be 'google-shortener'.
  - Click 'Enable'.  Click 'Go to Credentails'.
  - Which API are you using?
    Answer: URL Shortener API
  - Where will you be calling the API from?
    Answer: Other non-UI (e.g. cron job, daemon)
  - What data will you be accessing?
    Answer: Public data
  - Click 'What credentials do I need?'.
  - Copy your API Key!
  - Click 'Done'.

You can set the API Key you get above in the file /config.py at the
variable API_KEY.

References
  - https://developers.google.com/url-shortener/

# How To Run This Program

- Acquire Google URL Shortener API Key per instructions above
  (Steps to acquire Google URL Shortener API Key).

- Assuming your current directory is the project root directory.

- `$ mv config.orig.py config.py`

- Set your API Key to variable API_KEY inside the file 'config.py'.

- Make sure you use Python 3 to run it.  I use virtualenv as below.

  Create virtualenv (for Python 3) and activate it.

  ~~~
  $ virtualenv venv
  $ source ./venv/bin/activate
  ~~~

- Run it (You might want to `chmod +x shortener.py` first.)

  ~~~
  $ ./shortener.py SOME_URL
  ~~~

  Example

  ~~~
  $ ./shortener.py "https://developers.google.com/url-shortener/"

  # OUTPUT

  https://goo.gl/pZbaF
  ~~~

