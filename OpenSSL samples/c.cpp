#include <bits/stdc++.h>
using namespace std;
#include <openssl/aes.h>
#include <openssl/rand.h>

#define AES_KEY_LEN 256
#define AES_BLOCK_SIZE 16
#define vc vector<unsigned char>

vc get_random_bytes(int num_bytes)
{
    vc buffer(num_bytes);
    RAND_bytes(buffer.data(), num_bytes);
    return buffer;
}

vc aes_encrypt(vc &msg, vc &key, vc &iv)
{
    AES_KEY encrypt_key;
    AES_set_encrypt_key(key.data(), AES_KEY_LEN, &encrypt_key);
    vc ct(msg.size() + AES_BLOCK_SIZE);
    int n_blocks = msg.size() / AES_BLOCK_SIZE + 1;
    for (int i = 0; i < n_blocks; i++)
    {
        AES_cbc_encrypt(
            msg.data() + i * AES_BLOCK_SIZE,
            ct.data() + i * AES_BLOCK_SIZE,
            min(AES_BLOCK_SIZE, (int)msg.size() - i * AES_BLOCK_SIZE),
            &encrypt_key, (unsigned char *)iv.data(),
            AES_ENCRYPT);
    }
    return ct;
}

vc aes_decrypt(vc &ct, vc &key, vc &iv)
{
    AES_KEY decrypt_key;
    AES_set_decrypt_key(key.data(), AES_KEY_LEN, &decrypt_key);
    vc pt(ct.size());
    int n_blocks = ct.size() / AES_BLOCK_SIZE;
    for (int i = 0; i < n_blocks; i++)
    {
        AES_cbc_encrypt(
            ct.data() + i * AES_BLOCK_SIZE,
            pt.data() + i * AES_BLOCK_SIZE,
            AES_BLOCK_SIZE,
            &decrypt_key, (unsigned char *)iv.data(),
            AES_DECRYPT);
        return pt;
    }
}

int main()
{
    string msg = "Hi, there";
    vc pt(msg.begin(), msg.end());

    int pad_len = AES_BLOCK_SIZE - (pt.size() & AES_BLOCK_SIZE);
    pt.insert(pt.end(), pad_len, (unsigned char)pad_len);

    vc key = get_random_bytes(AES_KEY_LEN / 8);
    vc iv = get_random_bytes(AES_BLOCK_SIZE);

    vc cipher = aes_encrypt(pt, key, iv);
    vc dcipher = aes_decrypt(cipher, key, iv);

    int pad = dcipher.back();
    dcipher.resize(dcipher.size() - pad);
    string plain_text(dcipher.begin(), dcipher.end());

    cout << "Original msg: " << msg << '\n';
    cout << "Decrypted msg: " << plain_text << '\n';

    return 0;
}