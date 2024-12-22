# backend-assignment

- The code can be run locally serving two endpoints /orders and /products, follow Makefile.
- It can also be run as a docker container, follow Makefile for building and running it as a container.
     - make build to build the image.
     - make run to run the application
     - make logs can be used to see running application logs
- Tests are in the /app/tests folder and can be run using pytest commands. example: pytest test_orders.py
