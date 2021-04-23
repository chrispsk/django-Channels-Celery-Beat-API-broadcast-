# djangoChannels
<p>This program, read a webservice every 3 seconds and broadcast the content to all clients asynchronously.</p>
<p>I am using: django channels, websocket and celery beat</p>
<p>Installation:</p>
<ul>
  <li>pip install Django</li>
  <li>pip install celery</li>
  <li>pip install redis</li>
 </ul>

########### GET JOKES LIVE EVERY 3 SECONDS #########
1) Start Django server
2) Start Redis
3) Go to http://127.0.0.1:8000/
4) Start celery worker
(If in windows: ~ celery -A setari worker -l info -P gevent)
(If in Linux: ~ celery -A setari worker -l info)
5) Start celery beat
~ celery -A setari beat -l info
