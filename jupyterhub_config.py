c = get_config()

c.JupyterHub.authenticator_class = 'dummy'
c.JupyterHub.spawner_class = 'simple'

c.DummyAuthenticator.password = "password123"
c.DummyAuthenticator.admin_users = {'admin'}

c.SimpleSpawner.cmd = ['jupyter', 'notebook']
# now things get stored in /tmp/username