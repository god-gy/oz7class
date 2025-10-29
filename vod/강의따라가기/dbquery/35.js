use testmongodb;

db;

show dbs;

db.createCollection("users", { capped:false });

db.users.renameCollection("customers");

db.customers.drop();

db.dropDatabase();

db;