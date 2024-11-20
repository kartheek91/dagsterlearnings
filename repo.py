from dagster import FilesystemIOManager, graph, op, repository
from dagster_docker import docker_executor

# New op for the "Welcome to Data Engineering" message
@op
def welcome_message():
    return "Welcome to Data Engineering!"

# New graph for welcome message job
@graph
def welcome_graph():
    return welcome_message()

# New job for welcome message
welcome_job = welcome_graph.to_job(name="welcome_job")


# Define the repository to include the new job
@repository
def deploy_dagster_repository():
    return [welcome_job]
