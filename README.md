# odoo_challenge

This is a challenge given me as part of technical skills interview.
This repo contains two custom odoo module: Supply and Request

##Supply:
A prototype of suppliers management system: it allows to add suppliers to postgres Database and associate them with product categories

##Request:
This module integrates chatGPT in order to generate sample quote requests to suppliers

##How to install:
1) You need a running odoo server (the modules were developed in odoo16). Simple installation script can be found here:
    https://github.com/Yenthe666/InstallScript
2) Beyound standard odoo dependencies, request module calls openai, which can be installed manually or from requirements.txt file 
3) Add addon folders to the path accessible for odoo and indicate it in odoo.conf file as
   addons_path = /odoo/addons,/path/to/your/custom/module
