# djangoproject

Django powered responsive project used for my site:

http://brooklyndelta.com/

This is an attempt to create a very basic responsive blog site powered by **[Django](https://www.djangoproject.com/)**
and make it as easy as possible to get installed and running on an MAC OSX Environment.

### Caveats

Keep in mind this is a simple project. It does however require basic knowledge of python **[virtualenv](http://www.virtualenv.org/en/latest/)**,
Ruby **[Compass](https://rubygems.org/gems/compass)** and command line knowledge.

The instructions that follow are far from complete but should get you up and running.

### Local setup - sqlite3 & MAC OS X
**!!!Not to be used on production environments!!!**

### Dependencies

**[virtualenv](http://www.virtualenv.org/en/latest/)**
**[Compass](https://rubygems.org/gems/compass)**

### Instructions

1. Clone the repo:

    `git clone https://github.com/weeksghost/djangoproject.git`

    `cd djangoproject`

2.  Create and install the project dependcies in a **[virtualenv](http://www.virtualenv.org/en/latest/virtualenv.html#installation)**

    `pip install -r requirements.txt`

3.  This project uses compass to compile its css so you must also install Ruby **[Compass](https://rubygems.org/gems/compass)**

4. Generate project css:

    `cd compass`

    `compass compile`

5. Map your settings (database):

    You can see results faster by symlinking the example settings:

    `ln -s djangoproject/settings/example/settings.py djangoproject/settings/__init__.py`

    Or you can create your own. I would suggest copying and renaming the example directory
    just remember to symlink your settings.py file in the djangoproject/settings directory.


6. Sync the database:

    `./manage.py syncdb`

    `./manage.py migrate`

7. Use pre-configured fabfile to run server:

    `fab fresh0`

    or

    `./manage.py runserver 127.0.0.1:8000`

8. (Optional)

    I've included some fixtures to preload data from my site to be used as examples:

    `./manage.py loaddata homepage/fixtures/homepage.json`
    `./manage.py loaddata blog/fixtures/entries.json`

9. Visit the local site:

    **[http://localhost:8000/](http://localhost:8000/)**

10. Visit the admin:

    **[http://localhost:8000/admin/](http://localhost:8000/admin/)**
