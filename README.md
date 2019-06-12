# IAP_project-hq-backend

## Development
Build a docker image:
```
./tasks docker_build
```

Deploy the application locally (2 docker containers):
```
./tasks up
```

Verify that API Server listens and answers:
```
curl -i -L localhost:8000/branch_offices
curl -i -L localhost:8000/employees
```

Delete the local application:
```
./tasks down
```
