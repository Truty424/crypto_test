import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

static byte[] createDigest(byte[] input) throws NoSuchAlgorithmException {
    MessageDigest messageDigest = MessageDigest.getInstance("SHA-1");
    return messageDigest.digest(input);
}
