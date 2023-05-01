#include <string>
#include <isotream>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



int main()
{
    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);

        long long n = stoi(ltrim(rtrim(n_temp)));
        
        long long N_3 = (n-1)/3;
        long long N_5 = (n-1)/5;
        long long N_15 = (n-1)/15;
        
        
        long long s = 3*(N_3*(N_3+1)/2) + 5*(N_5*(N_5+1)/2) - 15*(N_15*(N_15+1)/2);
        std::cout << s << "\n";
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
