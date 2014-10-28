# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.contrib.console import confirm
from fabric.colors import red, green, yellow
import os.path

env.user = "root"
env.parallel=False
env.timeout=1
env.warn_only=True

# Get if deployed
deployed = os.path.isfile('deployed')

'''
Check if the project has already deployed
If there is a file called "deployed" then:
- Abort if the parameter "abortifdeployed" is True
If there is not a file called "deployed" then:
- Abort if the parameter "abortifdeployed" is False
'''
def checkdeploystatus(abortifdeployed = True):
    global deployed
    if deployed:
        if abortifdeployed:
            abort("El proyecto ya se ha desplegado")
    else:
        if not abortifdeployed:
            abort("Todavía no se ha hecho el despliegue inicial del proyecto")

'''
Initial deploy
This task can only exec once
'''
@task
def initialdeploy():
    checkdeploystatus()
    if confirm("Vas a realizar el despliegue inicial. Esta tarea sólo se puede ejecutar una vez\n¿Estás seguro?"):
    	print("Desplegando...")

        # Create file
        f = open('deployed','w')
        f.close()
        local('chattr +i deployed')
        print yellow('Despliegue inicial realizado')
        print yellow('ESTA TAREA NO SE VA A EJECUTAR DE NUEVO')
