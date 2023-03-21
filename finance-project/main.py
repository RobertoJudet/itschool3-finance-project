from fastapi import FastAPI
from api.users import users_router

app = FastAPI(
    debug=True,
    title="Fintech Portfolio API",
    description="A webserver with a REST API for keeping track off your different financial assets,"
    " stocks & crypto, and see/compare their evolution",
    version="0.1.0",
)
app.include_router(users_router)

if __name__ == "__main__":
    import subprocess

    subprocess.run(["uvicorn", "main:app", "--reload"])

# Homework 1 for Project
# implement get, create and delete user in domain too (user repo & user factory)
# also create api models
# create tests for repo & factory
# username should be at least 6 chars and max 20 chars, it can only contain letter, numbers & -
# save the user list in a file
