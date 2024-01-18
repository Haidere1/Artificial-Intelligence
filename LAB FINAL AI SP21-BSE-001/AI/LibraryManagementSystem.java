import java.util.ArrayList;
import java.util.List;

public class LibraryManagementSystem {
public static void main(String[] args) {
Book book1 = new Book("To Kill a Mockingbird", "Harper Lee", 1960);
Book book2 = new Book("1984", "George Orwell", 1949);

    User user1 = new User("John Smith", 30);
    User user2 = new User("Mary Johnson", 25);

    user1.borrowBook(book1);
    user2.borrowBook(book2);

    List<Book> books1 = user1.getBooks();
    List<Book> books2 = user2.getBooks();

    System.out.println(user1.getName() + " has borrowed the following books:");
    for (Book book : books1) {
        System.out.println(book.getTitle() + " by " + book.getAuthor() + " (" + book.getYear() + ")");
    }

    System.out.println(user2.getName() + " has borrowed the following books:");
    for (Book book : books2) {
        System.out.println(book.getTitle() + " by " + book.getAuthor() + " (" + book.getYear() + ")");
    }
}
}

