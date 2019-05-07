#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(void){
    // se definen las condiciones iniciales, como es c es la prop de la oda rho y tension se utilizan para definir c 
  double RHO = 0.01;
  double TENSION = 40.;
  
    
  double VEL = sqrt(TENSION/RHO);
  double cl = VEL;
  double CONST = VEL*VEL/(cl*cl);

  int nx = 101;
  int nt = 150;
  int counter = 1;
  
  double W[nx][3];
  double WTot[nx][nt];
    
 // recorrido utilizando sin
    
  for(int i=0;i<nx;i++){
      
    for(int j=0;j<3;j++){
      W[i][j]=sin(2*M_PI*i*0.005);
    }
      
    for(int j=0;j<nt;j++){
      WTot[i][j]=0.0;
    }
    WTot[i][0]=W[i][0];
  }
    
  for(int t=1;t<nt;t++){
    if(t==1){
      for(int ix=1; ix<nx-1;ix++){
        W[ix][1] = W[ix][0] + 0.5*CONST*(W[ix+1][0] + W[ix-1][0]-2.*W[ix][0]);
      }
    }
      
      else{
        
      for(int ix=1; ix<nx-1;ix++){
        W[ix][2] = 2.*W[ix][1] - W[ix][0] + CONST*(W[ix+1][1]+W[ix-1][1]-2.*W[ix][1]);
      }
    }
    for(int j=1;j<nx;j++){
      WTot[j][counter]=W[j][2];
    }
    counter = counter + 1;
    for(int ix=1;ix<nx-1;ix++){
      W[ix][0]=W[ix][1];
      W[ix][1]=W[ix][2];
    }
  }
  ofstream Archivo("Archivo.dat");
    
  for(int ix = 0; ix<nx; ix++){
      
    for(int it = 0; it < counter; it++)
    
    {
      Archivo << WTot[ix][it] << endl;
    }
  }
  return 0;
}
