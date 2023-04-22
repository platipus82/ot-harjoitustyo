Kun yritän asentaa Poetrya ohjeistuksen mukaan virtuaaliympäristössä (Linux Cubbli) niin se asennus näyttäisi menevän läpi. Kuitenkin sen jälkeen poetry ei toimi halutulla tavalla vaan antaa virheen
. Esim. jo pelkkä "poetry --version" antaa virheen: """ Traceback (most recent call last):
  File "/usr/bin/poetry", line 5, in <module> 
    from poetry.console import main
  File "/usr/lib/python3/dist-packages/poetry/console/init.py", line 1, in <module>
    from .application import Application
  File "/usr/lib/python3/dist-packages/poetry/console/application.py", line 3, in <module>
    from cleo import Application as BaseApplication
ImportError: cannot import name 'Application' from 'cleo' (/home/userX/.local/lib/python3.10/site-packages/cleo/init.py)
""" 
  
Samantyyppinen virhe on kuvattu myös muualla - esim. [tässä](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1025025)
Ratkaisua tähän en ole toistaiseksi onnistunut löytämään. 
  
  
