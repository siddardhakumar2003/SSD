#include<stdio.h>
#include<point.h>
#include<math.h>

int distance(Point p1,Point p2){
	return abs(p1.x-p2.x)+abs(p1.y-p2.y);
}
