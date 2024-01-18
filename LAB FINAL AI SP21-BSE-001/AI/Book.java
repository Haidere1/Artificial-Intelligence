import java.util.ArrayList;
import java.util.List;

class Book {
private String title;
private String author;
private int year;

public Book(String title, String author, int year) {
    this.title = title;
    this.author = author;
    this.year = year;
}

public String getTitle() {
    return title;
}

public String getAuthor() {
    return author;
}

public int getYear() {
    return year;
}
}

class Library {
private List<Book> books;

  
public void addBook(Book book) {
    if (books == nu ll) {
        books = new ArrayList<>();
    }
    books.add(book);
}

public synchronized void removeBook(Book book) {
    books.remove(book);
}

public List<Book> getBooks() {
    return books;
}
}

class User {
private String name;
private int age;
private Library library;
public User(String name, int age) {
    this.name = name;
    this.age = age;
}

public void borrowBook(Book book) {
    library.addBook(book);
}

public void returnBook(Book book) {
    library.removeBook(book);
}

public List<Book> getBooks() {
    return library.getBooks();
}
}

