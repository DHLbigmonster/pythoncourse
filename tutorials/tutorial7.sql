/* ============================================================
   Tutorial 7 – SQL (music.db)

   Exercise 1–2: DQL (Data Query Language)
      - SELECT with WHERE, LIKE, IN, BETWEEN, DISTINCT
      - JOINs, GROUP BY, HAVING, ORDER BY, LIMIT
      - Subqueries, CTEs

   Exercise 3–5: Non-DQL (DDL, DML, TCL)
      - DDL: CREATE TABLE, CREATE VIEW, DROP
      - DML: INSERT, UPDATE, DELETE
      - TCL: BEGIN TRANSACTION, COMMIT, ROLLBACK
   ============================================================ */


/* ============================================================
   Exercise 1 (DQL – Basic Filtering)
   ============================================================ */

-- Q1: List all customers who live in Brazil, showing their name, city and country.

-- Q2: Find all tracks with the word 'Love' in their name.

-- Q3: Find all albums whose name consists of more than one word.

-- Q4: List all distinct billing countries on invoices (alphabetically).

-- Q5: List all tracks whose media type is either MPEG audio file or AAC audio file.

-- Q6: List all invoices issued in the year 2011 (inclusive), using BETWEEN.



/* ============================================================
   Exercise 2 (DQL – Joins, Aggregation, Subqueries/CTEs)
   ============================================================ */

-- Q1: Find the 10 albums with the highest number of tracks, listing album title and track count.

-- Q2: For each sales support agent, determine how many customers they support.

-- Q3: Find the five tracks with the highest number of play history events.

-- Q4: For each playlist, determine how many distinct artists appear via their tracks in that playlist.

-- Q5: List the top 5 customers who have spent the most money on music.

-- Q6: List all customers whose total spending is higher than the average total spending
-- across all customers (computed via a subquery).

-- Q7: Find the most popular genre in terms of total sales using a CTE.

-- Q8: Find “cross-platform hits”: tracks that were played on at least 2 different device types
-- and purchased at least 2 times. Show track name, number of devices, play count and purchase count.



/* ============================================================
   Exercise 3 (DDL – Table and View Definitions)
   ============================================================ */

-- Q1: Create a table (genre_ratings) to store how much employees like different genres (using a composite primary key).

-- Q2: Create a view that shows all Rock tracks (track name, album title, artist name).



/* ============================================================
   Exercise 4 (DML – Insert, Update, Delete)
   ============================================================ */

-- Q1: Insert three example ratings for an employee into genre_ratings.

-- Q2: Change the rating for the employee and the third genre to 4.

-- Q3: Delete the rating of the employee for the second genre from genre_ratings.

-- Q4: Remove all rows from genre_ratings, but keep the table definition.

-- Q5: Drop the genre_ratings table completely.



/* ============================================================
   Exercise 5 (TCL – Transactions)
   ============================================================ */

-- Q1: Start a transaction that inserts two tracks of your choice and then commits.

-- Q2: Start a transaction that inserts a new customer, then roll it back.
