//CIS 221- Lab 3 0 Phone Call Budgeting
//Instructor - Catherine Stringfellow
//February 1, 1988
#include <string>
#include <iostream>
using namespace std;

const double DAYRATEFIRST = 0.50;
const double EVERATEFIRST = 0.40;
const double EVERATEADD = 0.20;
const double NIGHTRATEFIRST = 0.30;
const double NIGHTRATEADD = 0.15;
const double DAYRATEADD = 0.30;

void introduction ( )
{
	//write brief program description to text window.
	cout<<"\nPHONE BUDGET HELPER\n\n";

	cout<<"This program calculates information concerning long-distance";
	cout<<"telephone charges for calls in Texas.\n";

	cout<<"The program calculates cost when given the  length of call and the hour of day";
	cout<<" the call will be placed.  Or if the user chooses, the maximum call length in minutes";
	cout<<" can be calculated from the time of call and the allowed budget.\n\n";
} //introduction

void main( )
{
	double callCost, budget, rateFirst, rateAdd;
	int callHour, callLength, MilcallHour;
	char callTime, choice;
	string rateName;
	
	introduction( );
	
	//prompt user to choose budget-to-time or time-to-cost conversion.
	cout<<"Do you need to know the charges for a certain length call, or";
	cout<<"the  maximum call length possible on your budget? \n";
	cout<<"Enter c for charges or l for length of call: ";
	cin>>choice;
	
	//prompt for and read the time the call is to be made.
	cout<<"Enter the hour of day the call is to be made. (Example:  4) ";
	cin>>callHour;
	cout<<endl;
	
	//read if am or pm
	cout<<"Is that "<<callHour<<" am or "<<callHour<<" pm?\n";
	cout<<"Enter a for am or p for pm.  Noon is 12pm and midnight is 12am. ";
	cin>>callTime;
	
	//convert to military 24-hour time.
	if( (callTime == 'p') && (callHour != 12)) {
		MilcallHour = callHour + 12;
	}
	else {
		if((callTime == 'a')&&(callHour == 12)) {
			MilcallHour = 24;
		}
		else {
			MilcallHour = callHour;
		}
	}
	
	//determine which rate to use.
	if ((MilcallHour >= 5) && (MilcallHour < 17)){		//day rates needed
		rateFirst  = DAYRATEFIRST;
		rateAdd = DAYRATEADD;
		rateName = "Day Rate";
	}
	else if ((MilcallHour >=17) && (MilcallHour <23)) {	//evening rates needed
		rateFirst = EVERATEFIRST;
		rateAdd = EVERATEADD;
		rateName = "Evening Rate";
	}
	else{				//night rates needed
		rateFirst = NIGHTRATEFIRST;
		rateAdd= NIGHTRATEADD;
		rateName = "Night Rate";
	}
	
	switch(choice)	{
	  case 'c': 	{
		//prompt for and read length of call.
		cout<<"How long was the call?\n";
		cout<<"Enter the length of the call in MINUTES.  Please enter an integer. ";
		cin>>callLength;
		
		//calculate charges for the call.
		callCost = rateFirst + rateAdd * (callLength - 1);
		
		//print results
		cout<<"\nA call lasting "<<callLength<<" minutes at "<<callHour<<" "<<callTime;
		cout<<"m will cost $ "<<callCost;
		cout<<" at the current "<<rateName;
		break;
	  }
	  case 'l':	{
		//prompt for and read budget for call.
		cout<<"How much money do you have for the call?\n";
		cout<<"Enter your budget for the call, example: 1.50: ";
		cin>>budget;
			
		//calculate the maximum call length on budget.
		callLength = int(((budget - rateFirst)/rateAdd)+1);
			
		//print out results.
		if (callLength <=0)	{   //not enough money for call
			cout<<"\n\nYour budget is not enough to make a call at "<<callHour<< " "<<callTime<<"m";
			cout<<" at the current "<<rateName<<".";
		}
		else {	//can afford call
			cout<<"\nYou can afford a call of "<<callLength<<" minutes starting at "<<callHour<<" "<<callTime<<"m";
			cout<<" at the current "<<rateName<<".";
		} //if-then-else
	  }//second case value
	}//switch structure
	
	//write farewell
	cout<<"\n\n\nThank you for using the PHONE BUDGET HELPER!\n";
}