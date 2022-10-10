.PHONY: build destroy db-init refreeze run-task1 run-task2 run-task3


build:
	docker-compose build
	
refreeze:
	bash bin/refreeze.sh

destroy:
	docker-compose down

db-init:
	docker-compose run db_data_init 

run-task1:
	docker-compose run cars_service_task_1 
		
run-task2:
	docker-compose run cars_service_task_2

run-task3:
	docker-compose run cars_service_task_3 