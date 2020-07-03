In the file "master996.csv" you will find name of 996 books with these columns:
Book_Name, book_id, guten_genre, Author_Name
Author name follows this format: Lastname | FirstName 
The column "book_id" is the key, if you want to locate the content of the book in the directory "Gutenberg_19th_century_English_Fiction" with this id.
For example, the book_id = "pg98DickensTaleCities.epub" in "master996.csv", has the actual book content in the file "pg98DickensTaleCities-content.html" in "Gutenberg_19th_century_English_Fiction"
The 996 books here is a subset of 19th Century English fiction books by a single author (short-stories or books with multiple authors are not considered) from Gutenberg corpus located at https://www.gutenberg.org/

In the directory "Gutenberg_19th_century_English_Fiction" you will each book as a html file. There are 1079 html files representing 1079 books.
There may be a few extra html files in "Gutenberg_19th_century_English_Fiction" than present in "master996.csv". You can ignore the extra html files (1079-996=83 extra books as html).