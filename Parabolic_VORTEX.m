% Author: Kartik B

clc
close all
a=xlsread('coordinates.xlsx','B:B');
b=xlsread('coordinates.xlsx','A:A');
p1=polyfit(a,b,2)       %coefficients of the quadratic ax^2+bx+c
x=[100:7.45:407];
p2=polyval(p1,x);
hold on
plot(x,p2,'r-')
plot(a,b)
%x=[0:0.1:2];
%p2=polyval(p1,x);
%hold on
%plot(p2,x,'y-')