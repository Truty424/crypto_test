import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Main {

    static byte[] createDigest(byte[] input) throws NoSuchAlgorithmException {
        MessageDigest messageDigest = MessageDigest.getInstance("SHA-1");
        return messageDigest.digest(input);
    }

    public static void main(String[] args) throws NoSuchAlgorithmException {
        byte[] result = createDigest("tekst".getBytes());

        for (byte b : result) {
            System.out.printf("%02x", b);
        }
    }
}
