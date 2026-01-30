# My Hypothesis: < Correct Hypothesis>
SELECT name AS Customers
FROM Customers c
WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE c.id=o.customerId)


# More performatic Query
SELECT c.name AS Customers
FROM Customers c
WHERE id NOT IN (SELECT customerId FROM Orders)

