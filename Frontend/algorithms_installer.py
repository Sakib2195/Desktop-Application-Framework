import json
import docker


if __name__ == "__main__":
    client = docker.from_env()
    with open('config.json', 'r') as f:
        config = json.load(f)  
    
    # Run Local Registry
    container = client.containers.run('registry:2', detach=True, name='Desktop_Framework_Registry',ports={'5000':'5000'}, restart_policy={"Name": "always"})
    print(container.logs())

    for algo in config['ALGORITHMS']:
        try:
            algo = algo.lower()
            
            #Building docker image.
            for line in client.api.build(path=config['PATHS']['IMAGE_BUILD_PATH_MAC']+algo, tag=algo):
                print (line)
            
            #Tagging docker image(Required to push image to local registry).
            print(client.api.tag(algo, "localhost:5000/{algo}".format(algo=algo), force=True))
            
            for line in client.api.push("localhost:5000/{algo}".format(algo=algo), stream=True, decode=True):
                print (line)
        except Exception as e:
            print (e)
    
