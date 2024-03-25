Скачивание образа mattermost - docker pull mattermost/mattermost-preview
Создание контейнера  - docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview
Документация mattermost - https://docs.mattermost.com/install/install-docker.html


Добавить в пункте разработчик подсеть куда будут идти запросы.
так же нужно(на всякий) добавить в строке AllowedUntrustedInternalConnections в файле config.json в docker контейнере.




Полезные ссылки

https://developers.mattermost.com/integrate/plugins/interactive-messages/

https://developers.mattermost.com/integrate/webhooks/incoming/

https://pypi.org/project/requests/

https://habr.com/ru/articles/783574/


https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-ru

https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data

https://docs.mattermost.com/configure/configuration-settings.html#allow-untrusted-internal-connections-to

https://developers.mattermost.com/integrate/reference/bot-accounts/

