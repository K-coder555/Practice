import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
            String[] history = new String[100];
            int historyIndex = 0;

        do {
            Scanner scanner = new Scanner(System.in);
            System.out.println("첫 번째 숫자 : ");
            // Read a line of input from the user
            String firstNumber = scanner.nextLine();
            System.out.println("연산자(+-*/) : ");
            String operator = scanner.nextLine();
            System.out.println("두 번째 숫자 : ");
            String secondNumber = scanner.nextLine();

            switch (operator) {
                case "+":
                    history[historyIndex++] = firstNumber + " " + operator + " " + secondNumber + " = " + (Integer.parseInt(firstNumber) + Integer.parseInt(secondNumber));
                    System.out.println("계산결과: " + (Integer.parseInt(firstNumber) + Integer.parseInt(secondNumber)));
                    break;
                case "-":
                    history[historyIndex++] = firstNumber + " " + operator + " " + secondNumber + " = " + (Integer.parseInt(firstNumber) - Integer.parseInt(secondNumber));
                    System.out.println("계산결과: " + (Integer.parseInt(firstNumber) - Integer.parseInt(secondNumber)));
                    break;
                case "*":
                    history[historyIndex++] = firstNumber + " " + operator + " " + secondNumber + " = " + (Integer.parseInt(firstNumber) * Integer.parseInt(secondNumber));
                    System.out.println("계산결과: " + (Integer.parseInt(firstNumber) * Integer.parseInt(secondNumber)));
                    break;
                case "/":
                try {
                    if (Integer.parseInt(secondNumber) == 0) {
                        throw new ArithmeticException("0으로 나눌 수 없습니다.");
                    }
                } catch (ArithmeticException e) {
                    System.out.println(e.getMessage());
                    break;
                }
                    history[historyIndex++] = firstNumber + " " + operator + " " + secondNumber + " = " + (Integer.parseInt(firstNumber) / Integer.parseInt(secondNumber));
                    System.out.println("계산결과: " + (Integer.parseInt(firstNumber) / Integer.parseInt(secondNumber)));
                    break;
                default:
                    break;
            }

            System.out.println("계속하려면 c, 종료하려면 q를 입력하세요.");
            String continueInput = scanner.nextLine();
            if (continueInput.equals("q")) {
                System.out.println("프로그램을 종료합니다.");
                scanner.close();
                break;
            } else if (continueInput.equals("c")) {
                System.out.println("계속 진행합니다.");
            }
            
        } while (true);

        //scanner.close();
        System.out.println("계산 기록:");
        for (int i = 0; i < historyIndex; i++) {
            System.out.println(history[i]);
        }
    }
}
