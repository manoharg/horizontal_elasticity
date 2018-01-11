import docker
import logging

def GetDockerClient(env):
    cli = None

    if (env == 'local'): #local mode
        cli = docker.DockerClient(base_url='unix://var/run/docker.sock',
                                  version='17.05')
    elif (env == 'swarm'): # swarm mode
        tls_config = docker.tls.TLSConfig(
            ca_cert='/home/manohar/ca.pem',
            client_cert=('/home/manohar/cert.pem', '/home/manohar/key.pem'),
            verify=True
        )
        cli = docker.DockerClient(base_url='https://ape-swarm-manager:3376',
                                  tls=tls_config,
                                  version='1.23')
    return  cli


def TestDockerClient(env):
    cli = GetDockerClient(env)

    conlist = cli.containers.list()
    logging.info('List of container running') #list of containers running
    for con in conlist:
        logging.info(con.name)

    logging.info('Docker info') 
    logging.info(cli.info())
