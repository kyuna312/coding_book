#include <string>  
#include <iostream>  
#include <sstream>  
#include <experimental/filesystem>  

using namespace std;
namespace fs = std::experimental::filesystem;

// example adapted from https://docs.microsoft.com/pl-pl/cpp/standard-library/file-system-navigation
void DisplayPathInfo(const fs::path& pathToShow)
{
	int i = 0;	
	cout << "Displaying path info for: " << pathToShow << "\n";
	for (const auto& part : pathToShow)
	{
		cout << "path part: " << i++ << " = " << part << "\n";
	}

	cout << "exists() = " << fs::exists(pathToShow) << "\n"
		<< "root_name() = " << pathToShow.root_name() << "\n"
		<< "root_path() = " << pathToShow.root_path() << "\n"
		<< "relative_path() = " << pathToShow.relative_path() << "\n"
		<< "parent_path() = " << pathToShow.parent_path() << "\n"
		<< "filename() = " << pathToShow.filename() << "\n"
		<< "stem() = " << pathToShow.stem() << "\n"
		<< "extension() = " << pathToShow.extension() << "\n";

	try
	{
		cout << "canonical() = " << fs::canonical(pathToShow) << "\n";
	}
	catch (fs::filesystem_error err)
	{
		cout << "exception: " << err.what() << "\n";
	}
}


int main(int argc, char* argv[])
{
	const fs::path pathToShow{ argc >= 2 ? argv[1] : fs::current_path() };

	DisplayPathInfo(pathToShow);

	cout << "path concat/append:\n";
	fs::path p1("C:\\temp");
	p1 /= "user";
	p1 /= "data";
	cout << p1 << "\n";

	fs::path p2("C:\\temp\\");
	p2 += "user";
	p2 += "data";
	cout << p2 << "\n";
}