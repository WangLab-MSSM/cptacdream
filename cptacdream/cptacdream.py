import docker


client = docker.from_env()
images_local = client.images.list()
# boop = client.containers.run('alpine', 'echo hello world')

# TODO: write check for existing image?
client.images.pull('nginx')
print(images_local)
