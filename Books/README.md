Assignment: Books
Create a new Django project and add a books model. Complete the below functionality.

1. Create Books model
Your model should contain the following fields: title, author, published date, category.

2. Migrate
Make your migrations and activate shell.

3. Create and show Books
Make 5 new books and retrieve them all, as before.

4. Add a new field
Add a field to your table called in_print. This should be a boolean field.

What should you do to see your changes reflected in your database table? You'll have to makemigrations and migrate again. Once you do, a prompt will walk you through filling in values for the existing entries. Why is this? Discuss with your cohort-mates. Ask an instructor if you and your friends can't work it out.

==
Optional Assignment: Books and Authors
Build on your previous assignment. Make a new table for authors with the assumption that each book can have only one author. How will your book table change? Be sure you can add a book and an author and the relationship between them.

To Do:
1. Create your new database model and make any needed changes to your Book model.

2. Migrate!

3. Open shell.

4. Create 5 new books.

5. Create 5 new authors.

6. Assign author #1 to the first 2 books.

7. Assign author #4 to the rest of the books.

==
Optional Assignment: Anthologies
Modify your Books and Authors assignment to follow these guidelines.

An anthology is a collection of poetry or short stories, often by different authors. That means that some of these collections may have more than one author.

To Do:
1. change your Book's and Author's table relationships to many-to-many

2. in shell create 3 new books and 3 new authors.

3. now create a connection between an existing book and an existing author

4. connect another author to the same book

5. now use the authors attribute in your books model to retrieve all the authors of that book