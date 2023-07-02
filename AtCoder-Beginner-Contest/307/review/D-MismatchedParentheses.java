import java.util.Scanner;
import java.util.regex.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        String s = scanner.next();

        String r = deleteBrackets(s);
        System.out.println(r);
    }

    public static String deleteBrackets(String s) {
        s = s.replaceAll("\\([^\\(|^\\)]*\\)", "");
        if (s.matches(".*\\([^\\(|^\\)]*\\).*")) {
            return deleteBrackets(s);
        } else {
            return s;
        }
    }
}
