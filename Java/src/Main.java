public class Main {
    public static void main(String[] args) {
        Stock stock1 = new Stock("일반주A", 10000);
        Stock stock2 = new PreferredStock("우선주A", 15000, 5.0);


        stock1.printInfo();
        stock2.printInfo();
    }
}

