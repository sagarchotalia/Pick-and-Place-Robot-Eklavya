#include <iostream>
using namespace std;
int firstFit(int,int);
int main(){
  int boxes,count_of_bins=0,temp,i;
  float bincap;
  cout<<"Enter the number of boxes: ";
  cin>>boxes;
  cout<<"Enter the capacity of a bin: ";
  cin>>bincap;
  int boxdims[boxes];
  cout<<"Enter the dimensions of the boxes: \n";
  for(i=0;i<boxes;i++){
    cin>>boxdims[i];
  }
  temp = bincap;
  for(i=0;i<boxes;i++){
      if(temp-boxdims[i]>=0){
          temp -= boxdims[i];
      }
      else{
          count_of_bins+=1;
      }
  }
  cout<<count_of_bins;
}