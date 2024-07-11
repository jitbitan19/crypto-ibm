#include <bits/stdc++.h>
#include <openssl/rsa.h>
#include <openssl/pem.h>
#include <stdexcept>

using namespace std;

void rsa_gen_key(const string &key_name)
{
    int key_length = 2048;
    unsigned long exponent = RSA_F4;

    unique_ptr<BIGNUM, decltype(&BN_free)> bn(BN_new(), BN_free);
    if (!BN_set_word(bn.get(), exponent))
        throw runtime_error("Failed to set BIGNUM word");

    unique_ptr<RSA, decltype(&RSA_free)> rsa(RSA_new(), RSA_free);
    if (RSA_generate_key_ex(rsa.get(), key_length, bn.get(), nullptr) != 1)
        throw runtime_error("Failed to generate RSA key");

    string pvt_key = key_name + "__rsa_pvt_key.pem";
    string pub_key = key_name + "__rsa_pub_key.pem";

    unique_ptr<BIO, decltype(&BIO_free_all)> pvt_bio(BIO_new_file(pvt_key.c_str(), "w"), BIO_free_all);
    if (PEM_write_bio_RSAPrivateKey(pvt_bio.get(), rsa.get(), nullptr, nullptr, 0, nullptr, nullptr) != 1)
        throw runtime_error("Failed to write private key");

    unique_ptr<BIO, decltype(&BIO_free_all)> pub_bio(BIO_new_file(pub_key.c_str(), "w"), BIO_free_all);
    if (PEM_write_bio_RSAPublicKey(pub_bio.get(), rsa.get()) != 1)
        throw runtime_error("Failed to write public key");
}

unique_ptr<RSA, decltype(&RSA_free)> read_pvt_key(const string &key_name)
{
    string pvt_key = key_name + "__rsa_pvt_key.pem";
    unique_ptr<BIO, decltype(&BIO_free_all)> bio(BIO_new_file(pvt_key.c_str(), "r"), BIO_free_all);
    RSA *rsa = PEM_read_bio_RSAPrivateKey(bio.get(), nullptr, nullptr, nullptr);
    return unique_ptr<RSA, decltype(&RSA_free)>(rsa, RSA_free);
}

unique_ptr<RSA, decltype(&RSA_free)> read_pub_key(const string &key_name)
{
    string pub_key = key_name + "__rsa_pub_key.pem";
    unique_ptr<BIO, decltype(&BIO_free_all)> bio(BIO_new_file(pub_key.c_str(), "r"), BIO_free_all);
    RSA *rsa = PEM_read_bio_RSAPublicKey(bio.get(), nullptr, nullptr, nullptr);
    return unique_ptr<RSA, decltype(&RSA_free)>(rsa, RSA_free);
}

string rsa_encrypt(const string &msg, RSA *rsa)
{
    string encrypted(RSA_size(rsa), '\0');
    int result = RSA_public_encrypt(
        msg.size(), reinterpret_cast<const unsigned char *>(msg.c_str()),
        reinterpret_cast<unsigned char *>(&encrypted[0]), rsa, RSA_PKCS1_OAEP_PADDING);
    return encrypted;
}

string rsa_decrypt(const string &cipher, RSA *rsa)
{
    string decrypted(RSA_size(rsa), '\0');
    int result = RSA_private_decrypt(
        cipher.size(), reinterpret_cast<const unsigned char *>(cipher.c_str()),
        reinterpret_cast<unsigned char *>(&decrypted[0]), rsa, RSA_PKCS1_OAEP_PADDING);
    decrypted.resize(result);
    return decrypted;
}

string in_hex(string &s)
{
    stringstream ss;
    for (int i = 0; i < s.size(); i++)
        ss << hex << setw(2) << setfill('0') << (int)s[i];
    return ss.str();
}

int main()
{
    string key_name = "user";
    rsa_gen_key(key_name);
    auto pvt_key = read_pvt_key(key_name);
    auto pub_key = read_pub_key(key_name);

    string message = "1234567Jitbitan Baroi";
    string ct = rsa_encrypt(message, pub_key.get());
    string pt = rsa_decrypt(ct, pvt_key.get());

    cout << "Original message: " << message << endl;
    cout << "Encrypted message: " << in_hex(ct) << endl;
    cout << "Decrypted message: " << pt << endl;

    return 0;
}
