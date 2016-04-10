#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>

using namespace std;

int choose(int n, int k){
	if(k==0) return 1;
	return (n * choose(n-1,k-1))/k;
}

int count(int n){
	int c=0;

	while(n!=0){
		n=n&(n-1);
		c++;
	}

	return c;
}

int main(int argc, char **argv){
	//argv[1]=number of cities
	//argv[2]=file name of distance matrix
	
	int number_of_cities;
	int i, j, k, z;
	double **distance_matrix, tmpd, *t, *last;
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
	
	k=2;
	z = choose(number_of_cities,k);
	t = (double *) malloc(z * sizeof(double));

	while(k!=number_of_cities){

		last = t;
		k++;
		z = choose(number_of_cities,k);
		free(t);
		t = (double *) malloc(z * sizeof(double));
	}
}
