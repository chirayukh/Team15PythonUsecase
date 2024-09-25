# Team15PythonUsecase
Python Use Case Repository of Team15

1. Create a new database:
CREATE DATABASE bank_management;

2. Create a user and grant privileges (optional but recommended):
CREATE USER bms_user WITH ENCRYPTED PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE bank_management TO bms_user;

3. Once your database is created, go to VS code and for each service, you will see requirements.txt file. Open a terminal, go inside the folder of each service and execute below command:
   ls (to show all folders)
   cd user_service (or any other service)
   pip install -r requirements.txt (This will install all the libraries the service requires.)

4. Set Up a Virtual Environment
    A virtual environment helps to manage dependencies for your project. To create and activate a virtual environment, run:
    # Create a virtual environment
    python -m venv bank_management_env

    # Activate the virtual environment
    # On Windows
    bank_management_env\Scripts\activate
  **Note:- See the file "Errors and Resolutions" if you are stuck with an error related to "cannot be loaded because running scripts are disabled on this system."**
   
5. Run and Test the Services
  a.	Run Each Microservice:
  o	User Service: uvicorn user_service.main:app --port 8001 --reload 
  o	Loan Service: uvicorn loan_service.main:app --port 8002 --reload
  o	Account Service: uvicorn account_service.main:app --port 8003 --reload
  b.	Run the API Gateway:
  o	API Gateway: uvicorn api_gateway.main:app --port 8000 --reload
  c.	Test the Application:
  o	Use Postman or Swagger UI to test endpoints via the API Gateway at http://127.0.0.1:8000.
**Note:- You can run each microservice individually and see their swagger page by hitting their respective localhost in browser (http://localhost:{port})**

