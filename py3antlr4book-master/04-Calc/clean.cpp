#include <iostream>
#include <filesystem>
using namespace std;
namespace fs = filesystem;

int main()
{
    cout << "Enter file name: ";
    string s;
    cin >> s;
    for (auto itr : fs::directory_iterator(fs::current_path()))
    {
        if (itr.path().filename() == s && itr.path().extension() != "g4")
            fs::remove(itr.path());
    }

    return 0;
}