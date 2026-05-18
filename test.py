import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

static byte[] createDigest(byte[] input) {
    try {
        MessageDigest messageDigest = MessageDigest.getInstance("SHA-1");
        return messageDigest.digest(input);
    } catch (NoSuchAlgorithmException e) {
        throw new RuntimeException(
                "Cannot instantiate the message digest algorithm SHA-1", e);
    }
}
