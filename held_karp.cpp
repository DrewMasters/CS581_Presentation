#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>

using namespace std;

int main(int argc, char **argv){
	//argv[1]=number of cities
	//argv[2]=file name of distance matrix
	
	int number_of_cities;
	int i, j;
	double **distance_matrix, tmpd;
	string fn;
	string tmp;
	istringstream iss;

	if(argc!=3){
		cout << "Usage: executable number_of_cities file_name_of_distance_matrix\n";
		exit(1);
	}

	number_of_cities=atoi(argv[1]);
	fn=argv[2];

	distance_matrix = (double **) malloc(number_of_cities * sizeof(double *));
	for (i=0; i < number_of_cities; i++){
		distance_matrix[i] = (double *) malloc(number_of_cities * sizeof(double));
	}

	ifstream datafile(fn.c_str());

	for (i=0; i < number_of_cities; i++){
		getline(datafile,tmp);
		iss.clear();
		iss.str(tmp);
		
		for (j=0; j < number_of_cities; j++){
			iss >> tmpd;
			distance_matrix[i][j]=tmpd;
		}
	}

	for (i=0; i < number_of_cities; i++){
		for (j=0; j < number_of_cities; j++){
			cout << distance_matrix[i][j] << " ";
		}
		cout << endl;
	}

	datafile.close();
}
