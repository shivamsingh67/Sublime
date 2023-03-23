#include <bits/stdc++.h>
using namespace std;

int first_occurance(string str, char target){
	int n = str.length();
    int ans = -1;
	int st = 0;
	int en = n - 1;

	while(st <= en){
		int mid = st + (en - st)/2;

		if(str[mid] == target){
            ans = mid;
            en = mid - 1;
		}else if(str[mid] > target){
			en = mid - 1;
		}else{
			st = mid + 1;
		}
	}
	return ans;
}

int last_occurance(string str, char target){
	int n = str.length();
    int ans = -1;
	int st = 0;
	int en = n - 1;

	while(st <= en){
		int mid = st + (en - st)/2;

		if(str[mid] == target){
            ans = mid;
            st = mid + 1;
		}else if(str[mid] > target){
			en = mid - 1;
		}else{
			st = mid + 1;
		}
	}
	return ans;
}


vector<int>search_element(string str, char target){
	int first = first_occurance(str, target);
	int last = last_occurance(str, target);

	vector<int>ans;

	ans.push_back(first);
	ans.push_back(last);

	return ans;
}

int main(int argc, char const *argv[]) {
	string str;
	char target;
	cin >> str >> target;

	vector<int>ans;
	ans = search_element(str, target);

	for(int i = 0;i < ans.size(); i++){
		cout << ans[i] << " ";
	}

	return 0;
}