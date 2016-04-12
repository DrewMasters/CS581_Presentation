#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>

using namespace std;

int main(int argc, char **argv){
	int size=atoi(argv[1]);
	string filename = argv[2];
	int seed=atoi(argv[3]);
	int i, j;
	int **tmp;
	ofstream file;

	tmp = (int **) malloc(size*sizeof(int*));
	for (i=0; i<size;i++) tmp[i]=(int *) malloc(size*sizeof(int));

	srand(seed);
	file.open(filename.c_str());

	for (i=0; i<size; i++){
		for (j=0; j<size; j++){
			if (i!=j) {
				tmp[i][j]=rand()%50+1;
				tmp[j][i]=tmp[i][j];
			}
			else tmp[i][j]=0;
		}
	}
			
	for (i=0; i<size; i++){
		for (j=0; j<size; j++){
			if (j!=size-1) file << tmp[i][j] << " ";
			else file << tmp[i][j];
		}
		file << endl;
	}


}
