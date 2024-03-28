import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class phoneBook {

    public static void main(String[] args) {
        phoneBook phoneBook = new phoneBook();

        phoneBook.addPerson("Иванов", "+1234567890");
        phoneBook.addPerson("Иванов", "+0987654321");
        phoneBook.addPerson("Петров", "+1111222233");

        System.out.println("Телефоны Иванова: " + phoneBook.getPerson("Иванов"));
        System.out.println("Телефоны Петрова: " + phoneBook.getPerson("Петров"));
    }

    private final Map<String, List<String>> phoneBook;

    public phoneBook() {
        this.phoneBook = new HashMap<>();
    }


    public void addPerson(String name, String phoneNumber) {
        phoneBook.computeIfAbsent(name, k -> new ArrayList<>()).add(phoneNumber);
    }


    public List<String> getPerson(String name) {
        return phoneBook.getOrDefault(name, new ArrayList<>());
    }


}