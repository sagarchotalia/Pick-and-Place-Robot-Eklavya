#include <iostream>
#include<vector>

struct weights{
	int weight,box_num;
};
int main()
{
	int max_wt_box;
	int num_of_wt;
	std::cout<<"Enter number of weights"<<std::endl;
	std::cin>>num_of_wt;
	weights wt[num_of_wt];
	std::cout<<"Enter the weights"<<std::endl;
	for(int i=0;i<num_of_wt;i++){
		std::cin>>wt[i].weight;
	}
	std::cout<<"Enter max weight capacity of one box"<<std::endl;
	std::cin>>max_wt_box;
	std::vector<int> weight_remaining(num_of_wt,max_wt_box);
	int max_pos=0,pos=0;
	for(int i=0;i<num_of_wt;i++)
	{
		for(pos=0;pos<num_of_wt;pos++)
		{
			if(weight_remaining[pos]-wt[i].weight>=0)
			{
				wt[i].box_num=pos;
				weight_remaining[pos]-=wt[i].weight;
				break;
			}
		}
		if(pos>max_pos)
			max_pos=pos;
	}
	std::cout<<"Number of boxes used:"<<(max_pos+1)<<std::endl;
	for(int i=0;i<(max_pos+1);i++)
	{
		std::cout<<"Weights of box no:"<<(i+1)<<std::endl;
		for(int j=0;j<num_of_wt;j++)
		{
			if(wt[j].box_num==i)
				std::cout<<wt[j].weight<<" ";
		}
		std::cout<<std::endl;
	}
	return 0;
}