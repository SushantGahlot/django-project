## Django Project

---

### Endpoints

This project consists of two endpoints:

1. **GET** `verify/<str:company_name>/`
  
   This endpoint is responsible for verifying if a company is a user of the platform using solely its name

   **Response:**
   
   - **200** if a company is a user of the platform
   - **404** if a company is not a user of the platform

2. **GET** `relationship/<str:first_company>/<str:second_company>`

   This endpoint is responsible for assessing how frequent 2 companies can be confirmed to be transacting with one another

   **Response:**
   
   - json response with "frequency" of how many times these companies have transacted with each other

No other methods are allowed.

---

### Project structure

The project is built using Django and Docker. There are four primary services that can be found in the dockerfile:

1. PostgreSQL database service
2. Django webapp service
3. Nginx server serving Django
4. Memcached service

---

### Installation 

#### Requirements
- github: Installtion [instructions](https://github.com/git-guides/install-git)
- docker: Download from [here](https://docs.docker.com/get-docker/)


#### How to run
1. Git clone this repo
2. Open terminal/shell and change directory to cloned directory
3. Make sure docker is running
4. Run `docker-compose up --build`

The docker will download images and build containers. Once it has completed, endpoints can be accessed on http://localhost:1337/

---

### Observations/Design choices

1. Because the verification endpoint would potentially be accessed frequently, index field is added on `company_name`
2. When database grows bigger, filtering on `company_name`s can potentially get slower. Therefore, the results of this endpoints are cached. This can save database calls significantly.
3. Currently, the relationship is checked using `company_name`s. This approach is not scalable:
  
   - Two companies can have same names
   - As company names are used to create cache keys, it can lead to wrong keys being overwritten in the cache
   
   A better way to deal with this would be to send UUIDs of the companies than their names.

---

> Thank you for going through the project :)