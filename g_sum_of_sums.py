# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:50:51 2019

@author: Naveen Gunasekaran
"""
result_List = [];
sum_list = [];

input_file = "test.in";
#input_file = "D-small-practice.in";
#output_file = "solution_set.txt";
output_file = "solution_test.txt";
file_in = open (input_file, "r");
file_out = open (output_file, "w");

def gen_sub_array (long_list, n):
    list_len = n;
    for k in range (1,list_len+1):
        for j in range (list_len-k+1):
            i =0;
            temp_List = [];
            while i < k:
                temp_List.append(long_list[j+i]); 
                i = i+1;
            result_List.append(temp_List);
    del temp_List;
    return result_List;

def gen_sum_of_list (result_List):
    temp_sum = 0;
    for items in result_List:
        temp_sum = temp_sum + items;
    return temp_sum;


line = "";
line = file_in.readline();
no_test_cases = int(line);
test_case_no = 1;

while no_test_cases != 0:
    x_list = [];
    line = file_in.readline();
    for each in line.split():
        x_list.append(each);
    
    N = int(x_list[0]);
    Q = int(x_list[1]);        
    del x_list;

    x_list = [];
    line = file_in.readline();
    for each in line.split():
        x_list.append(int(each));
    
    test_list = x_list.copy();
    del x_list;
    result_List = gen_sub_array (test_list,N);

    i =0;
    for i in range (len(result_List)):
        sum_of_list = gen_sum_of_list (result_List[i]);
        sum_list.append(sum_of_list);

    sum_list.sort();
    
    file_out.write("Case #"+ str(test_case_no) + ":");
    file_out.write("\n");
    
    while Q != 0:
        x_list = [];
        line = file_in.readline();
        for each in line.split():
            x_list.append(int(each));
        li = int(x_list[0]);
        ri = int(x_list[1]);    
        del x_list;
        
        file_out.write(str(sum(sum_list[li-1:ri])));       
        file_out.write("\n");
        
        Q = Q - 1;

    test_case_no = test_case_no + 1;
    no_test_cases = no_test_cases - 1;
 
file_in.close();
file_out.close();
          