public class Main {
    public static void main(String[] args) {
        // Using the Builder pattern to create a Book object
        Book book1 = Book.builder()
                .title("Effective Java")
                .author("Joshua Bloch")
                .price(45.99)
                .build();

        // Using the generated toString() method
        System.out.println(book1.toString());

        // Creating another Book instance
        Book book2 = new Book("Clean Code", "Robert C. Martin", 35.50);

        // Using the generated equals() and hashCode() methods
        System.out.println(book1.equals(book2)); // false
    }
}
