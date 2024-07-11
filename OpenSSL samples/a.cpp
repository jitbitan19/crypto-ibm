#include <bits/stdc++.h>
#include <openssl/sha.h>
#include <openssl/evp.h>

using namespace std;

string sha3_256(string &s)
{
    EVP_MD_CTX *mdctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(mdctx, EVP_sha3_256(), nullptr);
    EVP_DigestUpdate(mdctx, s.c_str(), s.size());

    unsigned char hash[SHA256_DIGEST_LENGTH];
    unsigned int hash_len = 0;
    EVP_DigestFinal_ex(mdctx, hash, &hash_len);

    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
        cout << hex << setw(2) << (int)hash[i];
    cout << '\n';

    stringstream ss;
    for (int i = 0; i < hash_len; i++)
        ss << hex << setw(2) << (int)hash[i];
    return ss.str();
}

string sha3_512(string &s)
{
    EVP_MD_CTX *mdctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(mdctx, EVP_sha3_512(), nullptr);
    EVP_DigestUpdate(mdctx, s.c_str(), s.size());

    unsigned char hash[SHA512_DIGEST_LENGTH];
    unsigned int hash_len = 0;
    EVP_DigestFinal_ex(mdctx, hash, &hash_len);

    // for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
    //     cout << hex << setw(2) << (int)hash[i];
    // cout << '\n';

    stringstream ss;
    for (int i = 0; i < hash_len; i++)
        ss << hex << setw(2) << (int)hash[i];
    return ss.str();
}

string blake2s(string &s)
{
    EVP_MD_CTX *mdctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(mdctx, EVP_blake2s256(), nullptr);
    EVP_DigestUpdate(mdctx, s.c_str(), s.size());

    unsigned char hash[SHA256_DIGEST_LENGTH];
    unsigned int hash_len;
    EVP_DigestFinal_ex(mdctx, hash, &hash_len);
    stringstream ss;
    for (int i = 0; i < hash_len; i++)
        ss << hex << setw(2) << (int)hash[i];
    return ss.str();
}

int main()
{
    string data = "Hello, world!";
    sha3_256(data);
    return 0;
}