1. (0.5p) Complete README. Write a description about the project, what technologies are used in the project, 
how to install & start the project, what things you can do.
2. (0.5p) Branch organization. Delete all the branches with names. Create a branch `dev`, it should have the latest stuff. 
As you progress, create different versions(branches) of your project (git checkout -b v0.3). Also update the version 
where we initialize FastAPi (currently version 0.3.0).
3. (1p) We should decide the type of persistence, json file or sqlite, in a config file. Create a file `config.json` 
where you (or another user) can specify the type of persistence. When we create the object UserRepo we should inject the 
dependency based on the value from that file.
4. (0.5p) The model AssetInfoPrice should have the fields today_low_price, today_high_price, open_price uncommented. Add 
description to each one of them.
5. (0.5p) In the model class we should not have duplicate code, orm_mode = True. Refactor to eliminate the duplicate code.
6. (0.5p) I can query all the users, from file or sqlite.
7. (0.5p) I can query a specific user with its additional info.
8. (1p) Unit tests for UserPersistenceSqlite.
9. (1p) Unit tests for UserPersistenceFile.
10. (0.5p) I can add a user, in file or sqlite. Log the action at all layers.
11. (0.5p) Complete username validations on add. Username should be at least 6 chars and max 20 chars, 
it can only contain letters, numbers & -. Log the error & return a nice error message on API with 4xx response code.
12. (0.5p) Add unit tests for username validation & the whole user factory.
13. (1p) I can delete a user, from file or sqlite. Log the actions. Return 404 not found if the user does not exist.
14. (0.5p) I can add an asset to an user. Log the actions. Return nice error messages if something goes wrong.
15. (0.5p) I can delete an asset of an user. Log the actions. Return nice error messages if something goes wrong.
16. (1p) I can edit a user. I can change its username or the unit number of the assets. Log the actions. 
Support file & sqlite persistence. 
17. (0.5p) Add unit tests for user repo.
18. (0.5p) Property in asset to determine the current growth. Add unit tests for it. Add it to the api query.
19. (0.5p) Have the code to save the assets in sqlite in the persistence layer.
20. (0.5p) Have the code to save the assets in a file in the persistence layer.
21. (1p) Add unit tests for assets sqlite persistence code.
22. (1p) Add unit tests for assets file persistence code.