# Run all the other create- scripts.
# Build the database
source create-db.sql;
# Add example client data
source create-clients.sql;
# Add example lawyer data
source create-lawyers.sql;
# Add example review data
source create-reviews.sql;

# Display all added data
SELECT * FROM clients;
SELECT * FROM lawyers;
SELECT * FROM reviews;
