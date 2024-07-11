#include <bits/stdc++.h>
using namespace std;
#include <openssl/rsa.h>
#include <openssl/pem.h>

#define vc vector<unsigned char>

void rsa_gen_key(const string &key_name)
{
    int key_length = 2048;
    unsigned long exponent = RSA_F4;

    unique_ptr<BIGNUM, decltype(&BN_free)> bn(BN_new(), BN_free);
    BN_set_word(bn.get(), exponent);

    unique_ptr<RSA, decltype(&RSA_free)> rsa(RSA_new(), RSA_free);
    RSA_generate_key_ex(rsa.get(), key_length, bn.get(), nullptr);

    string pvt_key = key_name + "__rsa_pvt_key.pem";
    string pub_key = key_name + "__rsa_pub_key.pem";

    unique_ptr<BIO, decltype(&BIO_free_all)> pvt_bio(BIO_new_file(pvt_key.c_str(), "w"), BIO_free_all);
    PEM_write_bio_RSAPrivateKey(pvt_bio.get(), rsa.get(), nullptr, nullptr, 0, nullptr, nullptr);

    unique_ptr<BIO, decltype(&BIO_free_all)> pub_bio(BIO_new_file(pub_key.c_str(), "w"), BIO_free_all);
    PEM_write_bio_RSAPublicKey(pub_bio.get(), rsa.get());
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

vc rsa_sign(const vector<unsigned char> &msg, RSA *rsa)
{
    size_t sign_len;
    vc signature(RSA_size(rsa));

    unique_ptr<EVP_PKEY, decltype(&EVP_PKEY_free)> pkey(EVP_PKEY_new(), EVP_PKEY_free);
    EVP_PKEY_set1_RSA(pkey.get(), rsa);

    unique_ptr<EVP_MD_CTX, decltype(&EVP_MD_CTX_free)> md_ctx(EVP_MD_CTX_new(), EVP_MD_CTX_free);
    EVP_DigestSignInit(md_ctx.get(), nullptr, EVP_sha256(), nullptr, pkey.get());
    EVP_DigestSignUpdate(md_ctx.get(), msg.data(), msg.size());
    EVP_DigestSignFinal(md_ctx.get(), signature.data(), &sign_len);

    signature.resize(sign_len);
    return signature;
}

bool rsa_verify(const vector<unsigned char> &msg, const vc &signature, RSA *rsa)
{
    unique_ptr<EVP_PKEY, decltype(&EVP_PKEY_free)> pkey(EVP_PKEY_new(), EVP_PKEY_free);
    EVP_PKEY_set1_RSA(pkey.get(), rsa);

    unique_ptr<EVP_MD_CTX, decltype(&EVP_MD_CTX_free)> md_ctx(EVP_MD_CTX_new(), EVP_MD_CTX_free);
    EVP_DigestVerifyInit(md_ctx.get(), nullptr, EVP_sha256(), nullptr, pkey.get());
    EVP_DigestVerifyUpdate(md_ctx.get(), msg.data(), msg.size());
    if (EVP_DigestVerifyFinal(md_ctx.get(), signature.data(), signature.size()) != 1)
        return false;
    return true;
}

int main()
{

    string key_name = "user";
    rsa_gen_key(key_name);

    auto pvt_key = read_pvt_key(key_name);
    auto pub_key = read_pub_key(key_name);

    string msg1 = "Rivest Shamir Adleman";
    string msg2 = "Something else";

    vc msg_bytes1(msg1.begin(), msg1.end());
    vc msg_bytes2(msg2.begin(), msg2.end());

    vc sign1 = rsa_sign(msg_bytes1, pvt_key.get());
    vc sign2 = rsa_sign(msg_bytes2, pvt_key.get());

    cout << "Verifying msg1 with sign1: " << (rsa_verify(msg_bytes1, sign1, pub_key.get()) ? "valid" : "invalid") << '\n';
    cout << "Verifying msg2 with sign2: " << (rsa_verify(msg_bytes2, sign2, pub_key.get()) ? "valid" : "invalid") << '\n';
    cout << "Verifying msg1 with sign2: " << (rsa_verify(msg_bytes1, sign2, pub_key.get()) ? "valid" : "invalid") << '\n';
    cout << "Verifying msg2 with sign1: " << (rsa_verify(msg_bytes2, sign1, pub_key.get()) ? "valid" : "invalid") << '\n';

    return 0;
}
