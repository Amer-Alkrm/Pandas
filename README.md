# Pandas Project


**Perquisites:**

* Docker

## Running Project Locally

1. Clone the repository to your local machine.
2. Run the terminal on the directory of this project.
3. Build the service by running the following command `make build` in terminal.
4. Run db-init container using `make db-init` to seed the database from the csv file.
5. To execute the first task, use `make run-task1` to run the cars_service_task_1 container.
6. To execute the second task, use `make run-task2` to run the cars_service_task_2 container.
7. To execute the third task, use `make run-task3` to run the cars_service_task_3 container.


#### Database Container Configurations

* You can use the following configuration after running the service locally to connect to mysql database.

| Key | Value |
| --- | --- |
| `Container Name` | `car-service-mysql` (MYSQL) |
| `Port` | `3333` |
| `DB_NAME` | `cars` |
| `DB_USER` | `user` |
| `DB_PASSWORD` | `password` |

#### `make` Commands

Commands for local development are available via `make`:

* `make build` - build service and dependencies using `docker-compose`.
* `make destroy` - remove Docker resources created by `docker-compose`.
* `make refreeze` - run refreeze script after making changes on dependencies in `requirements.top`.
* `make db-init` - spins up service and seeds the database from the csv file using `docker-compose`.
* `make run-task1` - spins up service and executes the first task using `docker-compose`.
* `make run-task2` - spins up service and executes the second task using `docker-compose`.
* `make run-task3` - spins up service and executes the third task using `docker-compose`.
