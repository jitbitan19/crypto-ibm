#include <iostream>
#include <vector>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/core_names.h>
#include <openssl/param_build.h>

using namespace std;

class ECC
{
public:
    static EVP_PKEY *generate_keypair()
    {
        EVP_PKEY *pkey = NULL;
        EVP_PKEY_CTX *pctx = EVP_PKEY_CTX_new_from_name(NULL, "EC", NULL);
        if (!pctx || EVP_PKEY_keygen_init(pctx) <= 0)
        {
            cerr << "Error initializing the key generation context." << endl;
            exit(-1);
        }

        OSSL_PARAM params[] = {
            OSSL_PARAM_utf8_string("group", (char *)"secp256k1", 0),
            OSSL_PARAM_END};

        if (EVP_PKEY_CTX_set_params(pctx, params) <= 0)
        {
            cerr << "Error setting key generation parameters." << endl;
            exit(-1);
        }

        if (EVP_PKEY_keygen(pctx, &pkey) <= 0)
        {
            cerr << "Error generating the ECC key." << endl;
            exit(-1);
        }

        EVP_PKEY_CTX_free(pctx);
        return pkey;
    }

    // Sign a message using the private key
    static vector<unsigned char> sign_message(EVP_PKEY *pkey, const string &msg)
    {
        EVP_MD_CTX *mctx = EVP_MD_CTX_new();
        EVP_PKEY_CTX *sctx = NULL;

        if (EVP_DigestSignInit(mctx, &sctx, EVP_sha256(), NULL, pkey) <= 0)
        {
            cerr << "Error initializing DigestSign." << endl;
            exit(-1);
        }

        size_t sig_len;
        if (EVP_DigestSign(mctx, NULL, &sig_len, (const unsigned char *)msg.c_str(), msg.length()) <= 0)
        {
            cerr << "Error calculating the signature length." << endl;
            exit(-1);
        }

        vector<unsigned char> signature(sig_len);
        if (EVP_DigestSign(mctx, signature.data(), &sig_len, (const unsigned char *)msg.c_str(), msg.length()) <= 0)
        {
            cerr << "Error generating the signature." << endl;
            exit(-1);
        }

        signature.resize(sig_len);
        EVP_MD_CTX_free(mctx);
        return signature;
    }

    // Verify a signature using the public key
    static bool verify_signature(EVP_PKEY *pkey, const string &msg, const vector<unsigned char> &signature)
    {
        EVP_MD_CTX *mctx = EVP_MD_CTX_new();

        if (EVP_DigestVerifyInit(mctx, NULL, EVP_sha256(), NULL, pkey) <= 0)
        {
            cerr << "Error initializing DigestVerify." << endl;
            return false;
        }

        if (EVP_DigestVerify(mctx, signature.data(), signature.size(), (const unsigned char *)msg.c_str(), msg.length()) <= 0)
        {
            EVP_MD_CTX_free(mctx);
            return false;
        }

        EVP_MD_CTX_free(mctx);
        return true;
    }
};

int main()
{
    EVP_PKEY *pkey = ECC::generate_keypair();

    string message = "This is a message to sign";
    vector<unsigned char> signature = ECC::sign_message(pkey, message);

    cout << "Signature: ";
    for (auto c : signature)
    {
        cout << hex << (int)c;
    }
    cout << endl;

    bool valid = ECC::verify_signature(pkey, message, signature);
    cout << "Signature valid: " << (valid ? "Yes" : "No") << endl;

    EVP_PKEY_free(pkey);

    return 0;
}
