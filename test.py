import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

static byte[] createDigest(byte[] input) {
    try {
        MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");
        return messageDigest.digest(input);
    } catch (NoSuchAlgorithmException e) {
        throw new RuntimeException(
                "Cannot instantiate the message digest algorithm SHA-1", e);
    }
}

private String generateUniqueFileKey(String prefix, String hashString) {
            MessageDigest messageDigest;
            try {
                messageDigest = MessageDigest.getInstance("SHA-1");
            } catch (NoSuchAlgorithmException e) {
                throw new RuntimeException(e);
            }
            messageDigest.update(hashString.getBytes(StandardCharsets.UTF_8));

            return String.format(
                    "%s_%s", prefix, StringUtils.byteToHexString(messageDigest.digest()));
        }
