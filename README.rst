=========================
Prefixed ``test`` command
=========================

``manage.py test`` command that accepts ``--app_prefix`` argument and if given test only apps with names starting with this prefix. App names are got from ``INSTALLED_APPS``. This is suitable to test only apps from your project (which are usually prefixed with poreject name), not third-party apps.

Usage
______

Let's set ``INSTALLED_APPS`` as::

    INSTALLED_APPS = (
        'my_project.apps.blog',
        'my_project.apps.news',
        'south',
        'registration',
        'my_project.apps.catalog',
        'sorl.thumbnail',
    )
    
Then after ``python manage.py test --app_prefix=my_project.apps`` only ``blog``, ``news`` and ``catalog`` will be tested.

You can (thougn it doesn't make a lot of sense) list apps and then filter them with ``--app_prefix``. For example, ``python manage.py test blog news south registration --app_prefix=my_project.apps`` will test only ``blog`` and ``news``.