from ray import serve

@serve.deployment(num_replicas=1, ray_actor_options={"num_cpus": 0.2, "num_gpus": 0})
class helloWorld:
    def __init__(self):
        self.text = "hello "

    async def __call__(self, http_request) -> str:
        name = await http_request.json()
        return self.text + name

deployment_graph = helloWorld.bind()
