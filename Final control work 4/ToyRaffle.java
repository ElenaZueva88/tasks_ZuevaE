public class ToyRaffle {
    public static void main(String[] args) {
        ToyStore store = new ToyStore();

        Toy toy1 = new Toy(1, "Cat smoll", 10, 20);
        Toy toy2 = new Toy(2, "Dog Smoll", 200, 40);
        Toy toy3 = new Toy(3, "Car Blue", 200, 90);
        Toy toy4 = new Toy(4, "Car Green", 50, 30);
        Toy toy5 = new Toy(5, "Lego", 200, 90);
        Toy toy6 = new Toy(6, "Super Mario", 10, 10);

        store.addToy(toy1);
        store.addToy(toy2);
        store.addToy(toy3);
        store.addToy(toy4);
        store.addToy(toy5);
        store.addToy(toy6);


        store.changeToyFrequency(1, 30);

        store.organizeRaffle();

        Toy prizeToy = store.getPrizeToy();
        if (prizeToy != null) {
            System.out.println("Win toy: " + prizeToy.getName());
        }
    }
}

