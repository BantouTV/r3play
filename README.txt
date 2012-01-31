####################################### instrucoes:

- Controle do NGINX:

$ /etc/init.d/nginx restart
$ /etc/init.d/nginx start
$ /etc/init.d/nginx stop

- Verificar se o python está executando via fastcgi:

$ ps -ef | grep python

obs.: matar o processo: $ kill 1234

- Copiar arquivos via SCP:

$ scp -ri r3play.pem r3play/r3playapp/admin.py ec2-user@177.71.186.15:/home/ec2-user/r3play/r3playapp

obs.: scp -ri autenticacao quem-esta-sendo-copiado para-onde-se-esta-copiando

- Conectar na instancia da amazon ec2

$ ssh -i r3play.pem ec2-user@177.71.186.15

obs.: se tornar usuário root: sudo su

- Iniciar o django com o fastcgi e as configuações de produção:

$ python manage.py runfcgi host=ec2-177-71-186-15.sa-east-1.compute.amazonaws.com port=8080 --settings=settings-production


#########################

path local para os arquivos css do django

cd /Library/Python/2.7/site-packages/django/contrib/admin/media/css/

#########################

- exportar os dados do banco de dados e carregar novamente

1 - Export your data to a fixture using the dumpdata management command
2 - Drop the table
3 - Run syncdb
4 - Reload your data from the fixture using the loaddata management command