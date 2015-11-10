from hendrix.deploy.base import HendrixDeploy
from mysite.wsgi import application

deployer = HendrixDeploy(options={'wsgi': application,
                          'loud':True,
                          'http_port': 8080,
                          })

# 1. Add websocket listener
# 2. deployer.services.append(someTwistedService)
# 3. reactor.callWhenRunning(my_func)

deployer.run()

