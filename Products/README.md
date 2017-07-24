Assignment: Products
Using a new Django project, create in your app folder a model for a single table, Product. Complete the below functionality.

1. Build a new project
Refer back to the Setup Cheatsheet supplied in Django Intro if needed.

2. Create a new model called Product
The models file is found in your app's automatically generated files. If you need a refresher, look back at the last several tabs, especially the models tab.

3. Add the following fields to the Product class 
A product should have a name, description, weight, price, cost (to seller), and category. Figure out what type should be assigned to each field.

Once all the previous steps are complete, test your code by adding 3 new products. Retrieve all rows from your table and print each to the console.

==
Optional Assignment: Stores and Products
You'll be adding a new table to your products assignment. Add a store table. If you need help figuring out the relationship between product and store, try drawing out an ERD on a whiteboard or in workbench.

Follow the same procedure you did in the previous assignment. Add to your models, migrate, and activate shell.

To Do:
• create 5 stores

• create 5 products

• the first 2 stores you created should both carry products 1,2 and 3

• stores number 3 and 4 should carry products 3,4, and 5

• the last store should carry all 5 products