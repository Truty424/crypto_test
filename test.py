import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

static MessageDigest createMessageDigest() {
    try {
        return MessageDigest.getInstance("SHA-1");
    } catch (NoSuchAlgorithmException e) {
        throw new RuntimeException(
                "Cannot instantiate the message digest algorithm " + "SHA-1", e);
    }
}
