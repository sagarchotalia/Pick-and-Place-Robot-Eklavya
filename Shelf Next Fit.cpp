/*
1)Determine the proper orientation.
	1. If the rectangle is the first rectangle on a new open shelf, store it
	sideways. This is to minimize the height of the new shelf.
	2. If the rectangle fits upright, i.e. if max(w; h) < hs, then store it so.
	This aims to minimize the wasted surface area between the rectangle
	top side and the shelf ceiling.
	3. Otherwise store the rectangle sideways if possible.
2)Try to fit the rectangle onto the current open shelf.
3)If it does not fit, close the current shelf and open a new one.
4)If there is no room for a new shelf, terminate.
*/

#include <iostream>
#include<string>
#include<math.h>

int box_width,box_height,current_x=0,current_y=0,current_slab_ht=0;
/*current x,y stores right bottom corner of a rectangle after placement*/

void CheckForNextShelf(int w)
{
	if(current_x+w>box_width)
	{
		current_x=0;
		current_y+=current_slab_ht;
		current_slab_ht=0;		
	}
}
std::string fit_rectangle(int w,int h)
{
	if(box_height*box_width>=h*w)
	{		
		if(current_y<box_height)
		{
			CheckForNextShelf(w);/*check if current rectangle can occupy the current shelf if not go to the next*/
			if(current_y+h<=box_height)
			{
				if(current_slab_ht!=0)
				{
					if((current_y+std::max(w,h)<=box_height)&&(current_x+std::max(w,h)<=box_width))
					{
						if(std::max(w,h)>current_slab_ht)
							current_slab_ht=std::max(w,h);
						current_x+=std::min(h,w);
						if(h<w)
							std::cout<<"Rectangle has been rotated"<<std::endl;
					}
					else
					{
						if(h>current_slab_ht)
							current_slab_ht=h;
						current_x+=w;
					}
				}
				if(current_slab_ht==0)
				{
					current_slab_ht=std::min(h,w);
					current_x+=std::max(h,w);
					if(h<w)
						std::cout<<"Rectangle has been rotated"<<std::endl;					
				}
				
				return("Rectangle Fit");
			}			
			else
			{
				return("Rectangle cannot be fit");
			}		
		}
		else
		{
			return("Box filled up according to shelf next fit");
		}
	}
	else
	{
		return("Rectangle has greater dimensions than box");
	}
	
}
struct rectangle{
	int width,height;
};

int main()
{
	std::cout<<"Enter the dimensions of box"<<std::endl;
	std::cin>>box_width;
	std::cin>>box_height;
	int num_of_rectangle;
	std::cout<<"Enter number of rectangles"<<std::endl;
	std::cin>>num_of_rectangle;
	rectangle rt[num_of_rectangle];
	std::cout<<"Enter the dimensions of rectangle width and height"<<std::endl;
	for(int i=0;i<num_of_rectangle;i++){
		std::cin>>rt[i].width;
		std::cin>>rt[i].height;
		std::cout<<(fit_rectangle(rt[i].width,rt[i].height))<<std::endl;
		std::cout<<"Current X:"<<current_x<<"\tCurrent Y:"<<current_y<<std::endl;
	}

	return 0;
}
